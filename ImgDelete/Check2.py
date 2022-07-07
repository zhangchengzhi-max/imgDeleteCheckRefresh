import threading
import Config.Configuration
import Service.CheckService
import time
checkthreascount = Config.Configuration.Config.CheckThread

if __name__ == '__main__':
    start = time.time()


    for i in range(checkthreascount):
        t = threading.Thread(target=Service.CheckService.check.check,args=(i,))
        t.start()

    end = time.time()

    print(end-start)

