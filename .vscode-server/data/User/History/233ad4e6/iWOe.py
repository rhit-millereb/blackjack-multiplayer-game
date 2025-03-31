import threading
import ctypes
import signal
import os

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
         
    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
 
    def raise_exception(self):
        thread_id = self.get_id()
        print("stopping: "+str(thread_id))
        
        os.kill(thread_id, signal.SIGTERM)