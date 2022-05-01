import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL='sqlserver20220501.postgres.database.azure.com'
    POSTGRES_USER='dbadmin@sqlserver20220501'
    POSTGRES_PW='p@ssword1234'
    POSTGRES_DB='techconfdb'
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://servicebus20220501.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=n/d8zeDrPSxcx/vKtFsH+kGFrt6Lm1O54Z7L+wygQHo='
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    #ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    #SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False