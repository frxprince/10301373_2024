from pylab import *

#X=array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
def fzigzag(M):
    h = 0;
    v = 0;
    vmin = 0;
    hmin = 0;
    row,col=M.shape
    hmax=row-1;vmax=col-1
    i = 0;
    output = zeros((row * col));
    while(((v <= vmax) & (h <= hmax))):   
        if((h + v)% 2 == 0):
            if(v == vmin):
                output[i] = M[v, h]
                if (h == hmax):
                  v = v + 1
                else:
                  h = h + 1
                i = i + 1
            elif((h == hmax) & (v < vmax)):
                output[i] = M[v, h]
                v = v + 1
                i = i + 1

            elif ((v > vmin) & (h < hmax)):
                output[i] = M[v, h]
                v = v - 1
                h = h + 1
                i = i + 1      
        else:                                  

           if ((v == vmax) & (h <= hmax)):
                output[i] = M[v, h]
                h = h + 1
                i = i + 1
            
           elif (h == hmin):
                output[i] = M[v, h]
                if (v == vmax):
                  h = h + 1
                else:
                  v = v + 1

                i = i + 1

           elif ((v < vmax) & (h > hmin)):
                output[i] = M[v, h]
                v = v + 1
                h = h - 1
                i = i + 1

        if ((v == vmax) & (h == hmax)):
            output[i] = M[v, h]
            break
    return output

def izigzag(L,rows,cols):
    vmax=cols-1
    hmax=rows-1
    h = 0
    v = 0
    vmin = 0;
    hmin = 0;
    output = zeros((rows, cols))
    i = 0;
    while ((v <= vmax) & (h <= hmax)):
        if (((h + v)% 2) == 0):
            if (v == vmin):
                output[v, h] = L[i]
                if(h == hmax):
                    v = v + 1
                else:
                    h = h + 1
                i = i + 1
            elif ((h == hmax) & (v < vmax)):
                output[v, h] = L[i]            
                v = v + 1;
                i = i + 1;
            elif ((v > vmin) & (h < hmax)):
                output[v, h] = L[i]
                v = v - 1
                h = h + 1
                i = i + 1            
        else:
           if ((v == vmax) & (h <= hmax)):
                output[v, h] = L[i]
                h = h + 1;
                i = i + 1;            
           elif (h == hmin):
                output[v, h] = L[i];
                if (v == vmax):
                  h = h + 1;
                else:
                  v = v + 1;
                i = i + 1;
           elif ((v < vmax) & (h > hmin)):
                output[v, h] = L[i]
                v = v + 1;
                h = h - 1;
                i = i + 1;
        if ((v == vmax) & (h == hmax)):
            output[v, h] = L[i]
            break
    return output
#L=fzigzag(X)
#M=izigzag(L,4,4)


