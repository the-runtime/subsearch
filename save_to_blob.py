import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

def save_blob(name:str):

    connect_str= os.getenv("BLOB_CONNECT")
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "newcontainer"

    # get the container
    #container_client = blob_service_client.get_container(container_name)

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=name)

    with open(name,'rb') as f:
        blob_client.upload_blob(f)
    f.close()
    os.remove(name)
