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



