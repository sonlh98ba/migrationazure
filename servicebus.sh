uniqueId=20220501
resourceGroup="group$uniqueId"
location="australiaeast"
storageAccount="blob$uniqueId" 
serviceBus="servicebus$uniqueId"
quque="notificationqueue"

# create a Service Bus messaging namespace
az servicebus namespace create \
--resource-group $resourceGroup \
--name $serviceBus \
--location $location \
--sku Basic

# create a queue in the namespace
az servicebus queue create \
--resource-group $resourceGroup \
--namespace-name $serviceBus \
--name $quque \
--enable-partitioning true

# get the primary connection string for the namespace
connectionString=$(az servicebus namespace authorization-rule keys list \
--resource-group $resourceGroup \
--namespace-name $serviceBus \
--name RootManageSharedAccessKey \
--query primaryConnectionString \
--output tsv)

echo $connectionString

# # Create a storage account
# az storage account create \
# --name $storageAccount \
# --resource-group $resourceGroup \
# --location $location



