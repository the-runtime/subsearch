def get_time_stamp(name,text,container):

    fname = name
    ftext = text
    query = "SELECT c.time FROM Movies m JOIN c IN m.data WHERE m.part1 ="+ fname+ " AND c.text LIKE "+ftext


    #query = "SELECT * FROM data FROM part1 WHERE text CONTAINS 'What'd you say?' "
    #query = "SELECT c.time FROM Movies m JOIN c in m.data WHERE c.text LIKE "%NEWS%""

    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    print("output", items)

    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

    print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))
    # </query_items>

    return items
