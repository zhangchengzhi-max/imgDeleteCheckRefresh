import threading
import time
import requests
import Config.Configuration
import logging

logging.basicConfig(level=logging.INFO,
                    filename='log/checkLog.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s')

checkfile = Config.Configuration.Config.checkfile
existfile = Config.Configuration.Config.existfile
noexistfile = Config.Configuration.Config.notexist
needalterfile = Config.Configuration.Config.needalter

# lock = threading.Lock()

exist = open(existfile, 'w')
noexist = open(noexistfile, 'w')
needalter = open(needalterfile,'w')
file_size = len(open(checkfile).readlines())



def urlHead(url):

    try:
        # lock.acquire()
        headers = {
            'Connection': 'close',
        }
        response = requests.get(url,headers=headers)

        status_code = response.status_code
        message= str(status_code)+" "+url

        logging.info(message)
        # lock.release()
        if status_code == 200:
            exist.write(url+'\n')
            print(url+'\t')
        if status_code!=200:
            noexist.write(url+'\n')  # -------------------
    except Exception as Exe:
        messageError = str(Exe)+" "+url
        logging.error(messageError)
        print("url",url,"有问题",Exe)
        needalter.write(url+'\n')


def multi_thread(list):
    threads = []  # 放thread对象
    for i in range(len(list)):
        url = list[i]
        threads.append(
            threading.Thread(target=urlHead, args=(url,))
        )
    # 开启多线程
    for thread in threads:

        thread.start()

    for thread in threads:
        thread.join()

def Check(filename):
    t = int(str(file_size)[0])

    block_size = int(file_size/(t*200))
    print("总共分了",t*200,"块，","每一块的行数是",block_size+1)

    start_pos = 0
    end_pos = start_pos+block_size+1

    list_list = []
    while True:
        # print("从第",start_pos,"行开始执行")
        list = []
        # print(start_pos,"---------",end_pos)
        for i in open(filename).readlines()[start_pos:end_pos]:#------取开始和结束位置范围内的元素
            i = i.strip()
            list.append(i)

        if start_pos + block_size < file_size:
            start_pos = end_pos
            end_pos = start_pos + block_size+1
        else:
            start_pos = end_pos
            end_pos = file_size
        list_list.append(list)
        if start_pos >= file_size:
            break
    print("分块完成")

    #开始对每一块的url进行处理
    for k in range(len(list_list)):
        print("第",k+1,"块")
        list2 = list_list[k]

        multi_thread(list2)


if __name__ == '__main__':
    start_time = time.time()
    Check(checkfile)
    endtime = time.time()
    print(endtime-start_time)
