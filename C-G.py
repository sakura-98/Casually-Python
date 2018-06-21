import numpy as np

def j_xyz(l):
    '''
    given the dimension l, calculate the angular momentum components
    '''
    dim = int(2*l+1)
    jp = np.zeros((dim,dim),dtype=complex)
    jn = np.zeros((dim,dim),dtype=complex)
    jz = np.zeros((dim,dim),dtype=complex)
    j2 = np.zeros((dim,dim),dtype=complex)
    for i in range(dim):
        jz[i][i] = l-i
        j2[i][i] = l*(l+1)
    for i in range(dim-1):
        jp[i+1][i] = np.sqrt((2*l-i)*(i+1))
        jn[i][i+1] = np.sqrt((2*l-i)*(i+1))
    #print('jp=\n',jp)
    #print('jn=\n',jn)
    #print('jz=\n',jz)
    #print('j2=\n',j2)
    jx = (jp+jn)/2
    jy = (jp-jn)/(2j)
    return jx, jy, jz

def couple(l1,l2):
    '''
    given the dimension N1 and N2, calculate the coupling angular momentum
    '''
    dim1, dim2 = int(2*l1+1), int(2*l2+1)
    jx1, jy1, jz1 = j_xyz(l1)
    jx2, jy2, jz2 = j_xyz(l2)
    jx = np.kron(jx1,np.eye(dim2,dtype=complex))+np.kron(np.eye(dim1,dtype=complex),jx2)
    jy = np.kron(jy1,np.eye(dim2,dtype=complex))+np.kron(np.eye(dim1,dtype=complex),jy2)
    jz = np.kron(jz1,np.eye(dim2,dtype=complex))+np.kron(np.eye(dim1,dtype=complex),jz2)
    j2 = np.dot(jx,jx)+np.dot(jy,jy)+np.dot(jz,jz)
    return np.real(jz), np.real(j2)

def CG(l1,l2):
    '''
    calculate the common eigenvectors
    '''
    jz,j2 = couple(l1,l2)
    err = 1e-10
    s,a = np.linalg.eig(j2)
    # for i in range(len(a)):
        # for j in range(len(a[0])):
            # if abs(a[i][j])<err:
                # a[i][j]=0
    tmpz = np.dot(jz,a)/(a+1e-20)
    for i in range(len(a)):
        sz = list(set(['%.1f'%k for k in tmpz[:,i] if abs(k)>err]))
        s2 = np.sqrt(0.25+s[i])-0.5
        if len(sz) == 0:
            sz = 0
        elif len(sz) == 1:
            sz = sz[0]
        else:
            print('there is something wrong !J=%.1f,M in %s'%(s2,sz))
            continue 
        vec = ''
        for index,item in enumerate(a[:,i]):
            if abs(item)>err:
                vec += '%s√(%.5f)|%s>|%s>'%({True:'+',False:'-'}[item>0],item**2,l1-index//(2*l2+1),l2-index%(2*l2+1))
        print('J=%.1f,M=%s,vec=%s'%(s2,sz,vec))

if __name__ == '__main__':
  CG(1,1)
  #output:
  #J=2,M=0,vec=+√(0.166667)|1>|-1>+√(0.666667)|0>|0>+√(0.166667)|-1>|1>
  #
  #J=2,M=-1,vec=+√(0.500000)|0>|-1>+√(0.500000)|-1>|0>
  #
  #J=2,M=-2,vec=+√(1.000000)|-1>|-1>
  #
  #J=2,M=2,vec=+√(1.000000)|1>|1>
  #
  #J=2,M=1,vec=-√(0.500000)|1>|0>-√(0.500000)|0>|1>
  #
  #J=1,M=0,vec=+√(0.500000)|1>|-1>-√(0.500000)|-1>|1>
  #
  #J=1,M=1,vec=+√(0.500000)|1>|0>-√(0.500000)|0>|1>
  #
  #J=1,M=-1,vec=-√(0.500000)|0>|-1>+√(0.500000)|-1>|0>
  #
  #J=0,M=0,vec=-√(0.333333)|1>|-1>+√(0.333333)|0>|0>-√(0.333333)|-1>|1>
