import multiprocessing
import sys
import math
import time

sys.set_int_max_str_digits(100000)

def fact(n):
    res=math.factorial(n)
    time.sleep(1)
    return res

if __name__=="__main__":
    num=[500,600,700,800]
    st=time.time()
    
    with multiprocessing.Pool() as pool:
        res=pool.map(fact,num)
        
    et=time.time()-st
    
    result={ i:j for i in num for j in res}
    print("Result is :")
    print()
    for key,val in result.items():
        print(f"{key}:{val}")
        print()

    print(f"Time Taken : {et} sec")