import requests
import block.BlockPart
import Config
import log.log
from Config.Configuration import Config
import logging




#创建blockpart类的对象,用来给文件分块
blocksize = block.BlockPart.blockpart(Config.RefreshThread)



class Refresh:
    log.log.Log.log(Config.refreshlogfile)
    # logging.basicConfig(level=logging.INFO,
    #                     filename='log/refresh.txt',
    #                     filemode='a',
    #                     format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

    def refresh(i):
        # 获取到要刷新的文件名
        refreshfile = Config.refreshfile
        threadcount = i

        # block（文件名，当前线程）方法来返回i线程要处理的起始位置时start_pos,终点位置是end_pos的这些行url
        start_pos, end_pos = blocksize.block(refreshfile, threadcount)
        # 获取到需要检查的文件中的start_pos至end_pos之间的url,开始处理

        for line in open(refreshfile).readlines()[start_pos:end_pos]:
            line = line.strip()
            # print(type(line))
            try:
                refreshurl = 'https://purge.ws.netease.com/api/purge?url=' + line

                status_code = requests.get(refreshurl).status_code
                message = "刷新" + str(status_code) + '\t' + line
                logging.info(message)
                print(status_code, "\t", line)
            except:
                logging.error("刷新失败", line)
                # print("刷新失败", line)


