from thread import NewThread
from archive import NewFile

### Números a serem calculados
number_list1=[1,2,3,4,5,6,7,8,9,10]
number_list2=[11,12,13,14,15,16,17,18,19]


my_file=NewFile("file","txt")


## Targets para as threads de calculo e substituição
def insert_numbers(number_list,thread):
    for number in number_list:
        my_file.append_file(thread+str(number**2)+"\n")

def replace_thread(**old_and_new):
    my_file.replace_with(old_and_new)


### Iniciando as Threads
thread_1=NewThread(target=insert_numbers,name="insert_calc1",args=(number_list1,"thread 1: ",))
thread_2=NewThread(target=insert_numbers,name="insert_calc2",args=(number_list2,"thread 2: ",))
replace_thread=NewThread(target=replace_thread,name="replace",args=(),kwargs={"thread":"Line: "})

calc_threads=[thread_1,thread_2]


### Calculando e, quando o calculo é finalizado, substituindo a palavra thread
def init_work(threads):
    for thread in calc_threads:
        thread.start()
 
    while True:
        if not threads[0].is_alive() and not threads[1].is_alive():
                replace_thread.start()
                break

      
if __name__=="__main__":
    init_work(calc_threads)

