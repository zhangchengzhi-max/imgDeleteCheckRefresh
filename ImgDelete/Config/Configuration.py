class Config:

    #线程数量
    CheckThread = 8
    RefreshThread = 6
    DeleteThread =2


    #检查文件相关的
    checkfile = 'E:\\0705\\0705.txt'
    existfile = 'E:\\0705\\0705exist.txt'
    needalter = 'E:\\0517\\needalter\\needalter.txt'
    notexist = 'E:\\0517\\noexist\\0517noexist.txt'

    #删除文件
    deletefile = 'E:\\0705\\0705exist.txt'

    #刷新文件
    refreshfile = deletefile


    #日志文件
    deletelogfile = 'log/deleteLog.txt'
    checklogfile  = 'log/checkLog.txt'
    refreshlogfile   = 'log/refreshLog.txt'

