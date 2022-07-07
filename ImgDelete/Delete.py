import json
import math
import threading
import logging
import requests

import Config.Configuration
import First

#日志输入信息-->时间，py文件名，第几行，日志级别，信息
logging.basicConfig(level=logging.INFO,
                    filename='log/deleteLog.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')


deletefile = Config.Configuration.Config.deletefile


#文件行数
filesize = len(open(deletefile,'r+',errors='ignore').readlines())

filesize2 = math.ceil(filesize/2)

class myThread (threading.Thread):
    def __init__(self, threadID, name,startpos,endpos):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.startpos = startpos
        self.endpos = endpos
        self.name = name
    def run(self):
        # print ("开始线程：" + self.name)
        start_pos = self.startpos
        end_pos = start_pos + 10
        fileend = self.endpos

        while True:
            list = []
            for line in open(deletefile,errors='ignore').readlines()[start_pos:end_pos]:  # -----先处理10条数据
                line.strip()
                line = line.strip()
                # print(line)
                result = First.Filter.filter(line)
                if result != "白名单":
                #     line = line.strip()
                    list.append(line)
                else:
                    print("白名单：",line)
            a = {'from': 'cdn', 'uid': 'liushaowei', 'urls': list}
            if start_pos + 10 > fileend:
                start_pos = end_pos
                end_pos = fileend
            if start_pos + 10 <= fileend:
                start_pos = end_pos
                end_pos += 10

            # 调用接口删除图片
            try:

                response = requests.post('http://upload.ws.126.net/api/img/delete', json.dumps(a))
                print(response.text,a)
                # 添加日志
                logging.info(list)

            except Exception as ex:
                logging.error(list)

            if start_pos >= fileend:
                break





if __name__ == '__main__':


    thread1 = myThread(1, "deleteThread1", 0, filesize2)
    thread2 = myThread(2, "deleteThread2", filesize2, filesize + 1)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
