x=[0,2,2,4]
def merge(x):
    i=0
    j=3
    while i<j:
        if(x[i]==0):
            q=i
            while q<j:
                x[q+1]=x[q]
                q+=1
            x[j]=0
        else: