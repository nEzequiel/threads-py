from threading import Thread

class NewThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={}):
        Thread.__init__(self,group,target,name,args,kwargs) ## construtor padrão da Thread
        self._retorno=None

    def run(self):
        if self._target is not None:
            self._retorno =self._target(*self._args,**self._kwargs)

        else:
            print("No target")
    def join(self):
        Thread.join(self)
        return self._retorno


