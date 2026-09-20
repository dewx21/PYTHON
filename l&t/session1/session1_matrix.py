import numpy as np
print(np.matrix(np.arange(1,10).reshape(3,3))) #normal matrix
print(np.matrix(np.arange(1,10).reshape(3,3)).T) #transpose of that matrix
print(np.linalg.matrix_rank(np.arange(1,10).reshape(3,3))) #can find rank of the matrix using this
print(np.linalg.det(np.arange(1,10).reshape(3,3))) #can find determinant of the matrix using this