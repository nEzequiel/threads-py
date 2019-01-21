#algum arquivo a ser alterado
class NewFile():
    def __init__(self,nome=None,extensao=None,):
        self._nome=nome
        self._extensao=extensao
        self._file=None
    

    def create_file(self):
        if self._file is not None:
            self._file=open(self._nome+self._extensao)
        else:
            print("This file has already been created.")
    def close_file(self):
        self._file.close()
    
    def read_file(self):
        self._file=open(self._nome+"."+self._extensao,"r")
        return self._file.read()
        
    
    def write_file(self,text):
        self._file=open(self._nome+"."+self._extensao,"w")
        self._file.write(text)
        self.close_file()
        print("The file was writed with sucess.")
    
    def append_file(self,text):
        self._file=open(self._nome+"."+self._extensao,"a+")
        self._file.write(text)
        self.close_file()
        print("The file was updated with sucess."+text)
    
    def replace_with(self,old_and_new):
        self._file=open(self._nome+"."+self._extensao,"r+")
        file_string=self._file.read()
        self.close_file()

        self._file=open(self._nome+"."+self._extensao,"w")
        print(file_string)
        for i in old_and_new:
            print(i,old_and_new[i])
            file_string.replace("thread","a")
        self._file.write(file_string)
        self.close_file()
        print("The file was updated.")

    
        


    

