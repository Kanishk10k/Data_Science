from concurrent.futures import ProcessPoolExecutor
import time

def num(n):
    time.sleep(1)
    return f"Number : {n}"

if __name__=="__main__":

    numb=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

    t=time.time()
    print("Execution starts")

    with ProcessPoolExecutor(max_workers=10) as executor:
        res=executor.map(num,numb)

    for i in res:
        print(i)
        
    fin_time=time.time()-t
    print(fin_time)