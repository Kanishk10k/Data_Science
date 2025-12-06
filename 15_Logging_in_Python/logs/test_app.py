from logger import logging

def add(a,b):
    
    logging.debug("The addition taking place")
    return a+b

logging.debug("Debug msg before addition operation")
print(add(10,15))