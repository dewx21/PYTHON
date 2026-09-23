import numpy as np #load the numpy library in source code
# a1=np.array([1,2,3,4,5])
# print(a1)
# print(a1.shape, a1.dtype, a1.ndim, a1.size)

# a2=np.array([[1,3,2,4,],[8,9,10,11],[12,13,14,15]]) #3-d array
# print(a2.shape, a2.dtype, a2.ndim, a2.size)

# a3=np.arange(0,100) #1-d array
# print(len(a3))

# a4=np.arange(1,9).reshape(2,2,2)
# print(a4+10,'\n',a4-10,'\n',a4*10,'\n',a4/10,'\n',a4//10)
# operations and rearranging of arryas

# a5=np.arange(1,9).reshape(2,2,2)
# a6=np.arange(10,18).reshape(2,2,2)
# print(a5+a6,'\n',a5*a6,'\n',a5-a6,'\n',a5/a6,'\n',a5%a6,'\n',a5//a6)
# *(element wise mul), /(float div), //(int div), **(power), @(matrix multiplication)

# print(np.random.randint(1,100)) #returns 1 value
# print(np.random.randint(1,10,size=5)) #returns an array of 5 random values between 1 to 10
# print(np.random.randint(1,10,9).reshape(3,3)) #returns 9 values on random but this time the reshape makes it a 3,3 shape
# print(np.random.randint(1,10,size=(3,3))) #same thing but instead of using reshape we defined the value using size only
# print(np.random.uniform(1,10,size=(3,3)))
# print(np.random.randn(10))


# print(np.random.choice(np.arange(1,6),5,replace=False))
# print(np.random.choice(np.arange(1,5),5,replace=True))

# print(np.random.normal(50000,5000,100)) #average of 100 should be 50k and standard deviation should be 5k
# print(np.random.normal(60,3,50)) #this is related to some sort of bell curve

# print(np.random.binomial(n=10, p=0.5, size=10)) #simple binomial distribution for n number of events for size times

# print(np.random.poisson(lam=3, size=10))

print(np.matrix(np.arange(1,10)))