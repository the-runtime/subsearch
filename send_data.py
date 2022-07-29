import sub_search

def create_data(srt_name, container):
    sub_lis = sub_search.main(srt_name)
    print("hello2")

    container.create_item(body=sub_lis)
