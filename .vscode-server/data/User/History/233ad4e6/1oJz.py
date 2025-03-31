import threading
import ctypes

class KillThread(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self, target=target)
        self.target = target

    def run(self):
        # target function of the thread class
        try:
            while True:
                self.target()
        finally:
            print('ended')

 
    def stop(self):
        raise Exception("STOPPING")