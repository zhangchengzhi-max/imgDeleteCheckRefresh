import logging


class Log:
    def log(Ad):
        #日志输入信息-->时间，py文件名，第几行，日志级别，信息
        logging.basicConfig(level=logging.INFO,
                            filename=Ad,
                            filemode='a',
                            format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
