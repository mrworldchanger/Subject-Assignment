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
    ax.set_title('Vector Addition')
    plt.draw()
    plt.show()
    
    
a=input("Enter X Coordinate 1st Vector: ")
a=float(a);
b=input("Enter Y Coordinate 1st Vector: ") 
b=float(b); 
c=input("Enter X Coordinate 2nd Vector: ")
c=float(c);
d=input("Enter Y Coordinate 2nd Vector: ")  
d=float(d);
ar1 = np.asarray([a,b])
ar2 = np.asarray([c,d])
add=ar1+ar2
print('')
print('1st Vector (Blue)') 
print(ar1)
print('2nd Vector (Green)') 
print(ar2)
print('Addition of 1st and 2nd Vector (Red)') 
print(add)
print('')
display([ar1,ar2,add])
