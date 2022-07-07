此项目包含删除，刷新，检查三个部分
--------------------------------------------------------------------------
（IO密集型，使用多线程处理）

**删除**：（两个线程就可以，多了服务器会挂掉）
1. Delete.py:删除代码，固定2个线程不可更改
2. Delete2.py:删除代码，线程数量可以自己设定

**检查**：（试了试加多少线程都没问题，之前甚至试过5000多个线程）

1. Check.py:主线程对文件分块，分块大小可以在程序设置，分完块后，存到列表中，遍历列表，每一项有多少url，就加多少线程
2. Check2.py:同样先分块，每一块设一个线程，分多少块就有多少线程
3. CheckprocessPool.py: 和2一样的思路，只不过用的线程池
4. CheckAsyncion.py:多协程操作，实现单线程内的高并发

**刷新**：（六个线程就可以）
Refresh.py
---------------------------------------------------------------------------

其他说明： 
1. First.py:  过滤白名单，不需要独立运行，程序里会自动去调用
2. block/BlockPart.py: 分块程序
3. Config/Configuration.py: 路径，线程数量之类的配置
4. log/log.py:设置日志程序
5. log/xxxLog.txt: 输出后的日志文件

--------------------------------------------------------------------------
其他注意事项：

http://doc.ws.netease.com/pages/viewpage.action?pageId=334659961


先检查，再删除，再检查，再刷新存在的，然后再处理后续的
替换----- A域名替换为B域名，删除含B的url，刷新含A的url，，，，如果遇到删不掉的，则再试试删除AUrl

1.cimg的--------------- cimg.163.com 替换成 img163.nos2-i.service.163.org/cimg

                                 cimgx.163.com 替换成 img1.cache.netease.com

                                

2.vimg 的------------- vimgx.163.com 替换成 img163.nos.netease.com/vimg



不能删除的：
nos.netease.com/hot-pic
nie.res.netease.com
img.bimg.126.net-
nie.res.netease.com
muimages.nos-eastchina1.126.net
res.nie.netease.com
hot-pic.nosdn.127.net
flv15.bn.netease.com

其他：
http://img1.cache.netease.com/catchpic/5/58/58D10C8FEF97174A4CBD143D6BCF2467.jpg-----------后边加个/删除，然后刷新使用原来的url

http://cms-bucket.nosdn.127.net/catchpic/c/cb/cb56960c8a619eb3edb77a4ef0b92cd8.bmp?imageView&thumbnail=550x0   -------------   删除时去掉问号，刷新时带着问好并且encode.      (下次再试试，之前删除时直接encode不去掉问号好像也能删除)






