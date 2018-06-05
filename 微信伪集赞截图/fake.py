from PIL import Image
from random import sample
import numpy as np
import os

img = Image.open('favor.png')
s = img.size  #(1080,1902)
data = np.array(img.getdata()).reshape((s[1],s[0],3))
favor,under = 238,216 # 点赞背景色，评论横线色

# for i in range(s[1]):
    # for j in range(s[0]):
        # if np.dot(data[i][j]-favor,data[i][j]-favor) == 0:
            # print(i,j)
            # #print('(%.2f,%.2f)'%(i*9.11/1080,j*16.22/1920))
            # break

# 竖着搜索左边界（顺便上边界）
def min_xy():
    for j in range(s[0]):
        for i in range(s[1]):
            if not (data[i][j] - favor).any():
                return j,i
# 横着搜索右边界
def max_x():
    for i in range(minx,s[0]):
        if (data[miny][i] - favor).any():
            return i
# 横着搜索块
def block():
    for i in range(miny,s[1]):
        for j in range(minx,maxx):
            if (data[i][j] - favor).any():
                for k in range(j,maxx):
                    if not (data[i][k] -favor).any():
                        return j,i,k-j,i-miny

# 竖着搜索下边界
def max_y():
    for i in range(s[1]-1,miny,-1):
        if not (data[i][minx]-under).any():
            return i

minx,miny = min_xy()
maxx,maxy = max_x(),max_y()
corx,cory,a,ind = block()

#print('minx=%d,miny=%d'%(minx,miny))
#print('maxx=%d,maxy=%d'%(maxx,maxy))
#print('corx=%d,cory=%d'%(corx,cory))
#print('a=%d,ind=%d'%(a,ind))

eachx,eachy = (maxx-corx)//(a+ind),(maxy-cory)//(a+ind)

friends = [f for f in os.listdir('./res') if f[-4:]=='.png']
number = int(input('请输入伪集赞人数(<%d):'%len(friends)))
friends = sample(friends,number)
lines = (number-1)//eachx+1
blank = [[255]*3]*minx+[[favor]*3]*(maxx-minx)+[[255]*3]*(s[0]-maxx)
#print('number=%d,lines=%d'%(number,lines))

if lines <= eachy :
    for i in range(cory+a+ind,cory+(a+ind)*lines):
        data[i]=blank
    goal = Image.new(mode='RGB',size=s)
else: 
    data1,data2,data3 = np.copy(data[:cory+a+ind]),np.array((a+ind)*(lines-1)*[blank]),np.copy(data[maxy:])
    data4 = np.append(data1,data2,axis=0)
    data = np.append(data4,data3,axis=0)
    goal = Image.new(mode='RGB',size=(s[0],cory+(a+ind)*lines+s[1]-maxy))

#print(data.shape)

def insert(png, pos, size, data=data):
    source = Image.open(png).convert('RGB').resize(size).getdata()
    try:
        source = np.array(source).reshape((size[1],size[0],3))
    except Exception :
        print(png)
        print(source.mode)
    for i in range(size[0]):
        for j in range(size[1]):
            data[pos[0]+i][pos[1]+j] = source[i][j]

for line in range(lines):
    for row in range(eachx):
        try:
            insert('./res/%s'%friends[line*eachx+row],(cory+line*(a+ind),corx+row*(a+ind)),(a,a))
        except IndexError:
            break
        except Exception as e:
            print('fail! %s'%e)

# 保存png图片
for j in range(data.shape[0]):
    for i in range(data.shape[1]):
        goal.putpixel((i,j),(data[j][i][0],data[j][i][1],data[j][i][2]))
goal.save('output.png')