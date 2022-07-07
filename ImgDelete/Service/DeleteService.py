import threading

import requests
import block.BlockPart
import Config
import log.log
from Config.Configuration import Config
import logging
import First
import json

lock = threading.Lock()


#创建blockpart类的对象,用来给文件分块
blocksize = block.BlockPart.blockpart(Config.DeleteThread)



class Delete:
    log.log.Log.log(Config.deletelogfile)
    # lock.acquire()
    def delete(i):
        # 获取到要刷新的文件名
        deletefile = Config.deletefile
        threadcount = i

        # block（文件名，当前线程）方法来返回i线程要处理的起始位置时start_pos,终点位置是end_pos的这些行url
        start_pos, end_pos = blocksize.block(deletefile, threadcount)
        print(start_pos,"     ",end_pos)
        # 获取到需要检查的文件中的start_pos至end_pos之间的url,开始处理
        # for line in open(deletefile).readlines()[start_pos:end_pos]:
        startpos = start_pos
        endpos = startpos+10
        while True:
            list = []
            for line in open(deletefile).readlines()[startpos:endpos]:  # -----先处理10条数据
                line.strip()
                line = line.strip()

                result = First.Filter.filter(line)
                if result != "白名单":
                    # line = line.strip()
                    list.append(line)
                else:
                    print("白名单：", line)
            a = {'from': 'cdn', 'uid': 'liushaowei', 'urls': list}
            if startpos + 10 > endpos:
                startpos = end_pos
                endpos = end_pos
            if startpos + 10 <= endpos:
                startpos = endpos
                endpos += 10
            # 调用接口删除图片
            try:
                # response = requests.post(Config.Configuration.Config.deleteAddress, json.dumps(a))
                response = requests.post('http://upload.ws.126.net/api/img/delete', json.dumps(a))
                # status_code = requests.head(a)
                print(a)
                # 添加日志
                message = "删除"+response.text+str(a)
                logging.info(message)

            except Exception as ex:
                print(a)
                print("删除错误")
                message = "删除错误"+str(a)
                logging.error(message)

            if startpos >= end_pos:
                break
    # lock.release()

