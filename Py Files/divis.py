import numpy as np
i=0
X=0
A=np.empty((0))
while i<=99:
    i+=1
    X=i**2
    A=np.append(A,X)
    if i==100:
        A.resize((10,10))
div3=A[A%3==0]
np.save('div_by_3.npy',div3)