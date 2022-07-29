from azure.cosmos import exceptions, CosmosClient, PartitionKey
import os
#import family



def get_container():

        # Initialize the Cosmos client
        endpoint = os.getenv(COSMOS_DATABASE_ENDPOINT)
        key = os.getenv(COSMOS_DATABASE_KEY)
        # <create_cosmos_client>
        client = CosmosClient(endpoint, key)
        database_name = 'sub_search'

        database = client.get_database_client(database_name)

        container_name = 'sub_search_con1'

        container = database.get_container_client(container_name)

        return container
