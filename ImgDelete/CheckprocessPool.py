import concurrent.futures
import logging
from multiprocessing import Pool
import requests
import Config.Configuration
import log.log

log.log.Log.log(Config.Configuration.Config.checklogfile)

exist = open(Config.Configuration.Config.existfile,'w')
noexist = open(Config.Configuration.Config.notexist,'w')
needalter = open(Config.Configuration.Config.needalter,'w')

def head(url):
    response = requests.head(url)
    # print(response.status_code)
    try:
        status_code = response.status_code
        if status_code == 200:
            exist.write(url)
        else:
            noexist.write(url)
        message = "检查" + str(status_code) + '\t' + url
        logging.info(message)
    except Exception as ex:
        print(ex)
        logging.error("错误", ex)

    # return response.status_code


def lis(file_size,filename):
    t = int(str(file_size)[0])

    block_size = int(file_size / (t * 300))
    print("总共分了", t * 300, "块，", "每一块的行数是", block_size + 1)

    start_pos = 0
    end_pos = start_pos + block_size + 1

    list_list = []
    while True:
        # print("从第",start_pos,"行开始执行")
        list = []
        # print(start_pos,"---------",end_pos)
        for i in open(filename).readlines()[start_pos:end_pos]:  # ------取开始和结束位置范围内的元素
            i = i.strip()
            list.append(i)

        if start_pos + block_size < file_size:
            start_pos = end_pos
            end_pos = start_pos + block_size + 1
        else:
            start_pos = end_pos
            end_pos = file_size
        list_list.append(list)
        if start_pos >= file_size:
            break
    print("分块完成")
    # print("list_list",list_list)
    return list_list




if __name__ == '__main__':
    filename = Config.Configuration.Config.checkfile
    filesize = len(open(filename).readlines())
    print(filesize)
    list_list = lis(filesize,filename)
    # 开始对每一块的url进行处理
    for k in range(len(list_list)):
        print("第", k + 1, "块")
        list2 = list_list[k]
        pool = Pool(processes=50)
        pool.map(head,list2)






