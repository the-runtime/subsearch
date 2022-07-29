import subprocess
import os


from  get_database import get_container
#import sub_search
import send_data
from save_to_blob import save_blob

def is_empty(filename):
    if os.stat(filename).st_size == 0:
        return True

    else:
        return False



def process_vid(vid_name, container=get_container()):
    srt_name = f'{vid_name}.srt'
    output_process = subprocess.run(
        ["ccextractor",vid_name,"-o",srt_name],
        capture_output=True
        )
    err = output_process.stderr
    out = output_process.stdout.decode("utf-8")
    print(out)

    if not is_empty(srt_name):
        #sub_lis = sub_search.main(f"{vid_name}.srt")
        send_data.create_data(srt_name,container)

    save_blob(vid_name)
    print("video saved in cloud")



    #return f"{vid_name}.srt"
