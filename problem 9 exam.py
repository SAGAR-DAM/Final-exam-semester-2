'''
problem 9 final exam
Singular value decomposition of matrix
Name: SAGAR DAM;   DNAP'''

import numpy as np

#for first matrix
A = np.array([[2,1],[1,0],[0,1]])

U = np.linalg.eigh(np.dot(A,np.transpose(A)))[1] 

V  = np.linalg.eigh(np.dot(np.transpose(A),A))[1] 

S = np.dot(np.dot(np.transpose(U),A),V) 
print("FOR THE FIRST MATRIX:")
print("The singular value decompostion is given by: ")
print("U = ",U)
print()
print("S = ",S)
print()
print("V = ",V)

print()
print("From numpy, the decomposition is given by: ")
B = np.linalg.svd(A)
print()
print(B)
print("singular values of matrix 1:  ",np.sqrt(np.linalg.eigvals(np.dot(np.transpose(A),A))))
print()
print()


#for SECOND matrix
A = np.array([[1,1,0],[1,0,1],[0,1,1]])

U = np.linalg.eigh(np.dot(A,np.transpose(A)))[1] 

V = np.linalg.eigh(np.dot(np.transpose(A),A))[1] 

S = np.dot(np.dot(np.transpose(U),A),V) 
print("FOR THE SECOND MATRIX:")
print("The singular value decompostion is given by: ")
print("U = ",U)
print()
print("S = ",S)
print()
print("V = ",V)

print()
print("From numpy, the decomposition is given by: ")
B = np.linalg.svd(A)
print()
print(B)
print("singular values of matrix 2:  ",np.sqrt(np.linalg.eigvals(np.dot(np.transpose(A),A))))