def hesapla(x):
    return float((x*2)-4*x/x*3)

result=hesapla(5)
print(result)
#Lambda function kullanarak yapalım.
result2=lambda x : float((x*2)-4*x/x*3)
print(result2(5))