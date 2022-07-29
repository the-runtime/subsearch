import uuid
import os

def main(srt_name):

    inp_srt = open(srt_name,'r')
    lines = inp_srt.readlines()

    lines.append("/n")

    tem_lis = []
    final_lis = []

    for line in lines:

        if line == "\n":
            if len(tem_lis) != 0:
                final_lis.append(tem_lis)
                tem_lis = []

        else:
            line = line[:len(line)-3]
            tem_lis.append(line)


    final_dict = {}
    final_dict["id"] = srt_name[:len(srt_name)-4]+str(uuid.uuid4())
    final_dict["part1"] = srt_name[:len(srt_name)-4]
    j = 0
    data_lis = []
    for r in final_lis:
        tem_dict = {}
        tem_dict["time"] = r[1]

        i = len(r)
        tem_st =""

        while i-2:
            tem_st=tem_st+" "+r[len(r)-i+2]
            i=i-1
        tem_dict["text"] = tem_st

        data_lis.append(tem_dict)


    final_dict["data"] = data_lis

    inp_srt.close()
    os.remove(srt_name)
    return final_dict
