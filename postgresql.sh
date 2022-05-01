uniqueId=20220501
resourceGroupName="group$uniqueId"
location='australiaeast'
sqlServerName="sqlserver$uniqueId"
sqlDatabaseName="techconfdb"
clientIP=$(curl ifconfig.me)
echo $clientIP

# Create a resource group
az group create \
    --name $resourceGroupName \
    --location $location

# Create a PostgreSQL server
az postgres server create \
    --location $location \
    --resource-group $resourceGroupName \
    --name $sqlServerName \
    --admin-user dbadmin \
    --admin-password p@ssword1234

# Create the firewall rule
az postgres server firewall-rule create \
    --resource-group $resourceGroupName \
    --server $sqlServerName \
    --name azureaccess \
    --start-ip-address 0.0.0.0 \
    --end-ip-address 255.255.255.255

az postgres server firewall-rule create \
    --resource-group $resourceGroupName \
    --server $sqlServerName \
    --name clientip \
    --start-ip-address $clientIP \
    --end-ip-address $clientIP

# Get the connection information
az postgres server show \
    --resource-group $resourceGroupName \
    --name $sqlServerName \

# Create a SQL database
az postgres db create \
    --name $sqlDatabaseName \
    --resource-group $resourceGroupName \
    --server $sqlServerName 