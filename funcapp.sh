# Variables for MongoDB API resources
uniqueId=20220501
resourceGroup="group$uniqueId"
location='australiaeast'
storageAccount="blob$uniqueId" 
funcApp="funcapp$uniqueId"

# Create a storage account
az storage account create \
    --name $storageAccount \
    --resource-group $resourceGroup \
    --location $location

# Creat a function app
az functionapp create \
    --resource-group $resourceGroup \
    --name $funcApp \
    --storage-account $storageAccount \
    --os-type Linux \
    --consumption-plan-location $location \
    --runtime python

# Deploy the function 
# func azure functionapp publish funcapp20210405
