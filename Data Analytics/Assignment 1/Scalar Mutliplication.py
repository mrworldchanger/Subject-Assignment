import numpy as np
import matplotlib.pyplot as plt


def display(vecs): 
    plt.figure(figsize=(10,10))
    plt.ylabel('Y-axis')
    plt.xlabel('X-axis')
    ax = plt.gca()
    co=['b','g','r','c','m','y','b']
    i=0
    for vec in vecs:
      ax.quiver(0,0,vec[0],vec[1],color=co[i%len(co)],angles='xy',scale_units='xy',scale=1)
      i+=1
    vector=np.array(vecs);
    ax.set_xlim((-10,vector[:,0].max()+1))
    ax.set_ylim((-10,vector[:,1].max()+1))
    ax.set_title('Vector Scalar Multiplication')
    plt.draw()
    plt.show()
    
    
a=input("Enter X Coordinate 1st Vector: ")
a=float(a);
b=input("Enter Y Coordinate 1st Vector: ") 
b=float(b);
c=input("Enter Scalar Value For Multiplication: ") 
c=float(c);
ar1 = np.array([a,b])
ar2 = np.array([a*c,b*c])
print(ar2);
print('')
print('Vector (Blue)') 
print(ar1)
print('Vector After Scalar Multiplication (Green)') 
print(ar2)
display([ar1,ar2])
