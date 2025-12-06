# import multi_processing
import math
# import sys
import time

# sys.set_int_max_str_digits(100000)

def fact(num):
    print(f"Computing Factorial of {num}")
    res=math.factorial(num)
    print(f"Factorial of {num} is {res}")
    return res

if __name__=="__main__":
    
    print("Execution starts")
    
    num=[50000,60000,70000,80000]

    t=time.time()
    
    res=[]
    
    for i in num:
        res.append(fact(i))
    
    fin_time=time.time()-t

    print(f"Results: {res}")
    print(f"Time Taken : {fin_time} seconds")