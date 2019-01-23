#algum arquivo a ser alterado
class NewFile():
    """  """

    def __init__(self,nome=None,extensao=None,):
        self._nome=nome
        self._extensao=extensao
        self._file=None
    
    def close_file(self):
        self._file.close()
    
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
        file_string_replaced=""
        
        for word_to_replace in old_and_new:
            file_string_replaced=file_string.replace(word_to_replace,old_and_new[word_to_replace])
        self._file.write(file_string_replaced)
        self.close_file()
        print("The file was updated.")

    
        


    

