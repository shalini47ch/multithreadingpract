import threading 

print(threading.current_thread()) #this is the default thread that is created by the operating system

print(threading.current_thread().is_alive()) #this is meant to check whether the thread is alive or not
 