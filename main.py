from thread import NewThread
from archive import NewFile

number_list1=[1,2,3,4,5,6,7,8,9,10]
number_list2=[11,12,13,14,15,16,17,18,19]

my_file=NewFile("file","txt")

def insert_numbers(number_list,thread):
    for number in number_list:
        my_file.append_file(thread+str(number*2)+"\n")


def replace_number2(**old_and_new):
    my_file.replace_with(old_and_new)


thread_1=NewThread(target=insert_numbers,name="insert_calc1",args=(number_list1,"thread 1: ",))
thread_2=NewThread(target=insert_numbers,name="insert_calc2",args=(number_list2,"thread 2: ",))
thread_3=NewThread(target=replace_number2,name="replace_calc1",args=(),kwargs={"2":"Thread 3 New"})

threads=[thread_1,thread_2,thread_3]

def init_work(threads):
    for i in threads[0:1]:
        i.start()
    thread_3.start()
        
    


if __name__=="__main__":
    init_work(threads)

