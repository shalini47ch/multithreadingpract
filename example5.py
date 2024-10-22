from threading import Thread,active_count,enumerate

def display():
    for i in range(4):
        print("hello world")
#we will create one thread for the display function and the other thread for the show function

def show():
    for i in range(2):
        print("welcome ")

#creating threads for these two functions 
t1=Thread(target=display)
t2=Thread(target=show)
print("before ",t1.is_alive()) #so here since the thread has not started it is False
t1.start()
print("after ",t1.is_alive()) #here the thread has started so it is true
t2.start()
print("count of active threads ",active_count()) #this returns the total count of the no of running threads
#enumerate will return the lists of all the running threads 
print("list of all running threads",enumerate())
