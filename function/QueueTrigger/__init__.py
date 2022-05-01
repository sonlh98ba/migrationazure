import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):

    notification_id = int(float(msg.get_body().decode('utf-8')))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # Get connection to database
    conn = psycopg2.connect(dbname="techconfdb", 
                            user="dbadmin@sqlserver20220501", 
                            password="p@ssword1234", 
                            host="sqlserver20220501.postgres.database.azure.com")
    cur = conn.cursor()
    try:
        # Get notification message and subject from database using the notification_id
        cur.execute("SELECT subject, message FROM notification WHERE id={};".format(notification_id))
        result = cur.fetchall()
        subject, body = result[0][0], result[0][1]

        # Get attendees email and name
        cur.execute("SELECT email, first_name FROM attendee;")
        attendees = cur.fetchall()

        # Loop through each attendee and send an email with a personalized subject
        for (email, first_name) in attendees:
            mail = Mail(
                from_email='sonlh98ba@gmail.com',
                to_emails= email,
                subject= subject,
                plain_text_content= "Hi {}, \n {}".format(first_name, body))
            try:
                SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                response = sg.send(mail)
            except Exception as e:
                logging.error(e)
        status = "Notified {} attendees".format(len(attendees))
        # Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        cur.execute("UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(status, datetime.utcnow(), notification_id))
        
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        conn.rollback()       
    finally:
        # Close connection
        cur.close()
        conn.close()