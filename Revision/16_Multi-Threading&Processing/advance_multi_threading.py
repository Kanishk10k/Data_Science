from concurrent.futures import ThreadPoolExecutor
import time

def num(n):
    time.sleep(1)
    return f"Number : {n}"

numb=[1,2,3,4,5,6,1,2,3,4,5,6,7,8,9,0,8,7,6,5,3,2,2,3,4,5,1,2,4,0]

t=time.time()
print("Execution starts")

with ThreadPoolExecutor(max_workers=10) as executor:
    res=executor.map(num,numb)

for i in res:
    print(i)
    
fin_time=time.time()-t
print(fin_time)