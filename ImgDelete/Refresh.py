import threading
import Config.Configuration
import Service.RefreshService

refreshthreadcount = Config.Configuration.Config.RefreshThread

if __name__ == '__main__':

    for i in range(refreshthreadcount):
        t = threading.Thread(target=Service.RefreshService.Refresh.refresh,args=(i,))
        t.start()
