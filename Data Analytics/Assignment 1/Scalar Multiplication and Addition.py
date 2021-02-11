import numpy as np
import matplotlib.pyplot as plt


def display(vecs,n2): 
    plt.figure(figsize=(10,10))
    plt.ylabel('Y-axis')
    plt.xlabel('X-axis')
    ax = plt.gca()
    co=['blue','green','red','cyan','magenta','yellow','black','lime','royalblue']
    i=0
    vector=np.array(vecs);
    add=vector[0]+vector[1];
    vector=np.append(vector,add[None, :],axis=0)
    for i in range(1,n2):
        add=vector[0]+vector[1]*i;
        vector=np.append(vector,add[None, :],axis=0)
        i+=1
    for i in range(0,n2+2):
      ax.quiver(0,0,vector[i,0],vector[i,1],color=co[i%len(co)],angles='xy',scale_units='xy',scale=1)
      i+=1
    ax.set_xlim((-10,vector[:,0].max()+1))
    ax.set_ylim((-10,vector[:,1].max()+1))
    ax.set_title('Vector Scalar Multiplication and Addition')
    plt.draw()
    plt.show()
    print('Scalar Multiplication and Addition ')
    print(vector)
    


a=input("Enter X Coordinate 1st Vector: ")
a=float(a);
b=input("Enter Y Coordinate 1st Vector: ") 
b=float(b); 
c=input("Enter X Coordinate 2nd Vector: ")
c=float(c);
d=input("Enter Y Coordinate 2nd Vector: ")  
d=float(d);
e=input("Enter Number of Iterations: ") 
e=int(e);
ar1 = np.array([a,b])
ar2 = np.array([c,d])
display([ar1,ar2],e)
