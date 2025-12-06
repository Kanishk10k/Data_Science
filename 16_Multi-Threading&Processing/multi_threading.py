import threading
import time

def num():
    for i in range(5):
        time.sleep(3)
        print(f"No. : {i}")

def letter():
    for i in "abcde":
        time.sleep(2.5)
        print(f"Letter : {i}")

t1=threading.Thread(target=num)
t2=threading.Thread(target=letter)

t=time.time()

t1.start()
t2.start()

t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)