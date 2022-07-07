
import math
import Config.Configuration
class blockpart:
    def __init__(self,threadcount):

        self.threadcount = threadcount


    #参数为文件名和线程数，根据线程数量来分块
    def block(self,filename,i):
        filesize = len(open(filename,'rb').readlines())
        block_size = math.ceil(filesize /self.threadcount)
        start_pos = i * block_size
        if start_pos + block_size >= filesize + 1:
            end_pos = filesize + 1
        else:
            end_pos = (i + 1) * block_size
        return start_pos, end_pos
