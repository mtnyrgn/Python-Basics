for each in range(1,11):
    print(each)
for each in "BEŞİKTAŞ":
    print(each)
    
listt=[2,3213,3214,55,666]

summ=sum(listt)
print(summ)
result=0
for i in listt:
    result+=i
print(result)

i=0
while(i<10):
    print(i)
    i+=1
m=0
dump=len(listt)
while(m<dump):
    print(listt[m])
    m+=1
##### FİND THE MİNİMUM NUMBER İN ELEMENT OF LİST######
minimum=0
list1=[1,5,7,8989,445,-4]
n=int(len(list1))
print(n)
each=0
for each in list1:
    if(each<minimum):
        minimum=each
    else:
        continue
print(minimum)