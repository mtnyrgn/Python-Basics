#Numpy matematiksel operasyonları gerçekleştireceğimiz metodların olduğu bir kütüphanedir.
import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10]) #1x10 Vektör
print(array)
print(array.shape)

r_array=array.reshape(5,2)
print(r_array,"\nShape:",r_array.shape,"Dimension:",r_array.ndim)
print("Size",r_array.size)
print("Tpe:",type(r_array))

n_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
zeros=np.zeros((3,4)) #3 e 4 lük 0 lardan oluşan bir matris oluşur.Listedeki append metodu çok maliyetli.

zeros[0,0]=5
print(zeros)

ones=np.ones((3,5))
print(ones) #3 e 5 lik birim matris

empty=np.empty((2,3))
print(empty)

array=np.arange(10,50,5) #10 dan 50 ye 5 er 5 er artarak gidecek.10 inclusive olduğu için dahil 50 exclusive olduğu için dahil olmayacak..
print(array)

array=np.linspace(10,50,20) #10dan 50 ye kadar araya 20 tane random atarak gelecektir.
print(array)

a=np.array([1,2,3])
b=np.array([3,4,5])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))
print(a<2) #Array içinde 2 den küçük elemanların yerine tru büyük eşit olanların yerine false.

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])


print(a*b) #Element Product
print(a.dot(b.T)) #Matris Product
print(np.exp(a)) #Exponential

a=np.random.random((5,5))
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))
#*****SLİCİNG AND İNDEXİNG*********
array=np.array([1,2,3,4,5,6,7])
print(array[0:4]) #4 exclusive olduğu için dahil değil.0,1,2,3 indexlerini yazdıracak.

reverse_array=array[::-1]
print(reverse_array)
array1=np.array([[1,2,3],[4,5,6]])
print(array1[1,0:2])
print(array[-1:])

#Shape Manipulation

m=np.random.random((3,5))
n=m.ravel() #Array düz hale geldi.
print(m)
print(n)
n=n.reshape(3,5)
print(n)

#Stacking Arrayy

arr=np.random.random((2,3))
arr1=np.random.random((2,3))

#Vertical ve horizontal olarak 2 şekilde birleştirebilirim.
arr2=np.vstack((arr,arr1))
arr3=np.hstack((arr,arr1))

print("\n\n\n")
print(arr2)
print(arr3)

