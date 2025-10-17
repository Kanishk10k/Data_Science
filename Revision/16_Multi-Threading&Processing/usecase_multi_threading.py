'''

https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup
import time

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/tutorials/'

]

def fetch(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

print("Execution starts")

t=time.time()

for url in urls:
    thread=threading.Thread(target=fetch,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

fin_time=time.time()-t

print(fin_time)
print("All web pages fetched")