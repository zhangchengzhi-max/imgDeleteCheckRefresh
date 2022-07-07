import threading
import First
import requests
import block.BlockPart
import Config.Configuration
import log.log
import asyncio
import logging

# 日志输出到checklogfile文件
log.log.Log.log(Config.Configuration.Config.checklogfile)


noexistfile = Config.Configuration.Config.notexist
existfile = Config.Configuration.Config.existfile
exist = open(existfile,'w')
noexist = open(noexistfile,'w')



class check:

    # lock.acquire()
    def check(i):

        # 创建blockpart类的对象,用来给文件分块
        blocksize = block.BlockPart.blockpart(Config.Configuration.Config.CheckThread)

        #获取到要检查的文件名
        checkfile = Config.Configuration.Config.checkfile
        threadcount = i

        #block（文件名，当前线程）方法来返回i线程要处理的起始位置时start_pos,终点位置是end_pos的这些行url
        start_pos,end_pos =blocksize.block(checkfile,threadcount)

        #获取到需要检查的文件中的start_pos至end_pos之间的url,开始处理
        for line in open(checkfile).readlines()[start_pos:end_pos]:
            line = line.strip()
            #line 为文件中的url
            result = First.Filter.filter(line)
            if result=="白名单":
                print("白名单：",line)
            else:

                try:
                    status_code = requests.get(line).status_code
                    # print(status_code,"---",line)
                    if status_code==200:
                        print(status_code,"----",line)
                        exist.write(line+'\n')
                    else:
                        noexist.write(line+'\n')
                    message = "检查" + str(status_code) + '\t' + line
                    logging.info(message)
                except Exception as ex:
                    print(ex)
                    logging.error("错误",ex)

    # lock.release()




