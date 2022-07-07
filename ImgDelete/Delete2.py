import threading
import Config.Configuration
import Service.DeleteService

deletethreadcount = Config.Configuration.Config.DeleteThread

if __name__ == '__main__':

    for i in range(deletethreadcount):
        t = threading.Thread(target=Service.DeleteService.Delete.delete,args=(i,))
        t.start()
