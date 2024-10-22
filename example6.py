#here we will add the execution of the join method 
#if a thread wants to wait for the other thread then we can use the .join() method 

from threading import Thread

def display():
    for i in range(5):
        print("Welcome")

#similarly create a helper for show 
def show():
    for i in range(5):
        print("Lets start coding ")

t1=Thread(target=display)
t2=Thread(target=show)
t1.start()
t1.join() #we want t1 to get completed before t2 starts
t2.start()
#now also creating a function for the main thread
for i in range(4):
    print("helloooo")