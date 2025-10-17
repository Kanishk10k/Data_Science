import logging

logging.basicConfig(
    filename='app1.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def div(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    
    except ZeroDivisionError:
        logger.error("Division by Zero Error")
        return None
    
print(add(10,15))
print(sub(10,15))
print(mul(10,15))
print(div(10,15))