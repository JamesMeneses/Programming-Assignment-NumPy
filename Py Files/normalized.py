import numpy as np
X=np.random.random((5,5))
XBar=np.mean(X)
XSum=np.std(X)
Z=(X-XBar)/XSum
np.save('X_normalized.npy',Z)