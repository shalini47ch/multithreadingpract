#print in order 
'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.





'''
from threading import Thread,Lock
class Foo:
    def __init__(self):
        self.secondLock=Lock()
        self.thirdLock=Lock()
        #lock the second and third so that they maintain the order
        self.secondLock.acquire()
        self.thirdLock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.

        printFirst()
        self.secondLock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.secondLock.acquire()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.thirdLock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.thirdLock.acquire()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
foo=Foo()
#now creation of threads
t1=Thread(target=foo.first,args=(lambda:print("first")))
t2=Thread(target=foo.second,args=(lambda:print("second")))
t3=Thread(target=foo.third,args=(lambda:print("third")))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()