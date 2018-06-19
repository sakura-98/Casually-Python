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

def common(l1,l2):
    '''
    calculate the common eigenvectors
    '''
    jz,j2 = couple(l1,l2)
    err = 1e-10
    a,s,b = np.linalg.svd(j2)
    tmp = np.dot(jz,a)/a
    for i in range(len(a)):
        sq = int(np.sqrt(s[i]))
        z = next((k for k in tmp[:,i] if not np.isnan(k)))
        vec = ''
        for index,item in enumerate(b[i]):
            if abs(item)>err:
                vec += '%s√(%f)|%d>|%d>'%({True:'+',False:'-'}[item>0],item**2,l1-index//(2*l2+1),l2-index%(2*l2+1))
        print('J=%d,M=%d,vec=%s\n'%(sq,z,vec))

if __name__ == '__main__':
  common(1,1)
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
