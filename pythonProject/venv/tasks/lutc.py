rec = {"name" : "Bob","jobs": ["developer","manager"],
       "web":"www.bobs.org/~Bob",
       "home": {"state": "Overworked", "zip": 12345}}
d=[]
d.append(rec)
print(d)
asd=[1,2,3,4,5,"r","t","y","u","i","o"]
dic={"a":1,"x":2,"c":3}
for i,j in dic.items():
       print(i,j)
for i,j in enumerate(asd):
       print(i,j)

# подсчет колличества вхождений символов в строку
from collections import Counter
c=Counter("fgvn trt ewyfj djdghjetyy ehfgn")
print(c)
