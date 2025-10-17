from logger import logging

def add(a,s):
    logging.debug("Debug before addition")
    return a+s

logging.debug("Debug after addition")
add(5,4)