import os

DOWN, UP, LEFT, RIGHT, FRONT, BACK = 'y', 'w', 'g', 'b', 'r', 'o'

def gs():
    # 侧面
    cube[1],cube[2],cube[3],cube[4] = cube[2],cube[3],cube[4],cube[1]
    
    # 顶面
    cube[0][0][0],cube[0][2][0],cube[0][2][2],cube[0][0][2] = \
    cube[0][2][0],cube[0][2][2],cube[0][0][2],cube[0][0][0]
    
    cube[0][0][1],cube[0][1][0],cube[0][2][1],cube[0][1][2] = \
    cube[0][1][0],cube[0][2][1],cube[0][1][2],cube[0][0][1]
    
    # 底面
    cube[5][0][0],cube[5][0][2],cube[5][2][2],cube[5][2][0] = \
    cube[5][0][2],cube[5][2][2],cube[5][2][0],cube[5][0][0]
    
    cube[5][0][1],cube[5][1][2],cube[5][2][1],cube[5][1][0] = \
    cube[5][1][2],cube[5][2][1],cube[5][1][0],cube[5][0][1]

def gn():
    gs();gs();gs()

def Us():
    # 正面
    cube[0][0][0],cube[0][2][0],cube[0][2][2],cube[0][0][2] = \
    cube[0][2][0],cube[0][2][2],cube[0][0][2],cube[0][0][0]
    
    cube[0][0][1],cube[0][1][0],cube[0][2][1],cube[0][1][2] = \
    cube[0][1][0],cube[0][2][1],cube[0][1][2],cube[0][0][1]
    
    # 侧面
    cube[1][0],cube[2][0],cube[3][0],cube[4][0] = \
    cube[2][0],cube[3][0],cube[4][0],cube[1][0]

def Un():
    Us();Us();Us()

def Ds():
    # 底面
    cube[5][0][0],cube[5][0][2],cube[5][2][2],cube[5][2][0] = \
    cube[5][0][2],cube[5][2][2],cube[5][2][0],cube[5][0][0]
    
    cube[5][0][1],cube[5][1][2],cube[5][2][1],cube[5][1][0] = \
    cube[5][1][2],cube[5][2][1],cube[5][1][0],cube[5][0][1]
    
    # 侧面
    cube[1][2],cube[2][2],cube[3][2],cube[4][2] = \
    cube[2][2],cube[3][2],cube[4][2],cube[1][2]

def Dn():
    Ds();Ds();Ds()

def Ls():
    # 左侧
    cube[1][0][0],cube[1][0][2],cube[1][2][2],cube[1][2][0] = \
    cube[1][0][2],cube[1][2][2],cube[1][2][0],cube[1][0][0]
    
    cube[1][0][1],cube[1][1][2],cube[1][2][1],cube[1][1][0] = \
    cube[1][1][2],cube[1][2][1],cube[1][1][0],cube[1][0][1]
    
    # 侧面
    cube[0][0][0],cube[2][0][0],cube[5][0][0],cube[4][2][2] = \
    cube[2][0][0],cube[5][0][0],cube[4][2][2],cube[0][0][0]
    
    cube[0][1][0],cube[2][1][0],cube[5][1][0],cube[4][1][2] = \
    cube[2][1][0],cube[5][1][0],cube[4][1][2],cube[0][1][0]
    
    cube[0][2][0],cube[2][2][0],cube[5][2][0],cube[4][0][2] = \
    cube[2][2][0],cube[5][2][0],cube[4][0][2],cube[0][2][0]

def Ln():
    Ls();Ls();Ls()

def Rs():
    gs();gs()
    Ln()
    gs();gs()

def Rn():
    gs();gs()
    Ls()
    gs();gs()

def Fs():
    gs()
    Ln()
    gn()

def Fn():
    gs()
    Ls()
    gn()

def Bs():
    gn()
    Ls()
    gs()

def Bn():
    gn()
    Ln()
    gs()

def show():
    print("\n展开图:\n\n")
    print("    %s"%''.join(cube[0][0]))
    print("    %s"%''.join(cube[0][1]))
    print("    %s"%''.join(cube[0][2]))
    print("%s %s %s %s"%(''.join(cube[1][0]),''.join(cube[2][0]),''.join(cube[3][0]),''.join(cube[4][0])))
    print("%s %s %s %s"%(''.join(cube[1][1]),''.join(cube[2][1]),''.join(cube[3][1]),''.join(cube[4][1])))
    print("%s %s %s %s"%(''.join(cube[1][2]),''.join(cube[2][2]),''.join(cube[3][2]),''.join(cube[4][2])))
    print("    %s"%''.join(cube[5][0]))
    print("    %s"%''.join(cube[5][1]))
    print("    %s"%''.join(cube[5][2]))
    os.system("pause&cls")

def OmakeTen():
    print("右逆、上逆、前逆、上顺、前顺、右顺")
    Rn();Un();Fn()
    Us();Fs();Rs()

def makeTen():
    t = (cube[0][0][1]==UP)+(cube[0][1][0]==UP)+(cube[0][2][1]==UP)+(cube[0][1][2]==UP)
    if t == 0:
        OmakeTen()
        OmakeTen()
        print("顶部旋转两次")
        Us();Us()
        OmakeTen()
    elif t == 2:
        while cube[0][0][1]!=UP or cube[0][1][2]==UP:
            print("顶部顺时针旋转")
            Us()
        OmakeTen()
        show()
        if cube[0][1][2]!=UP:
            OmakeTen()
    print("已搭好十字\n")
    show()

def OrecUpTen():
    print("右顺、上顺、右逆、上顺、右顺、上顺、上顺、右逆")
    Rs();Us()
    Rn();Us()
    Rs();Us();Us();Rn()

def recUpTen():
    def color2int(c):
        try:
            return {LEFT:0, FRONT:1, RIGHT:2, BACK:3}[c]
        except KeyError:
            print("你一定哪里弄错了,重来一遍！")
            return 4
    
    delta = [(4+i-color2int(cube[i+1][0][1]))%4 for i in range(4)]
    #已对齐
    if(delta[0]==delta[1]and delta[0]==delta[2] and delta[0]==delta[3]):
        pass
    #对位
    elif(delta[0]==delta[2]):
        OrecUpTen()
        print("顶部逆时针旋转 1 次")
        Un()
        OrecUpTen()
    elif(delta[1]==delta[3]):
        OrecUpTen()
        print("顶部逆时针旋转 1 次")
        Un()
        OrecUpTen()
    #邻位
    elif(delta[0]==delta[1]):
        print("顶部旋转两次")
        Un();Un()
        OrecUpTen()
    elif(delta[1]==delta[2]):
        print("顶部逆时针旋转")
        Un()
        OrecUpTen()
    elif(delta[2]==delta[3]):
        OrecUpTen()
        print("顶部顺时针旋转")
        Us()
    elif(delta[3]==delta[0]):
        print("顶部顺时针旋转")
        Us()
        OrecUpTen()
    delta[0] = (4-color2int(cube[1][0][1]))%4
    print("顶部顺时针旋转 %d 次"%delta[0])
    for i in range(delta[0]): Us()
    print("十字已对齐\n")
    show()

def OrecL():
    print("左顺、右顺、上顺、右逆、上逆、左逆、上顺、右顺、上逆、右逆")
    Ls();Rs();Us();Rn();Un()
    Ln();Us();Rs();Un();Rn()

def OrecR():
    print("左顺、右顺、上逆、左逆、上顺、右逆、上逆、左顺、上顺、左逆")
    Ls();Rs();Un();Ln();Us()
    Rn();Un();Ls();Us();Ln()

def recOne():
    if({cube[0][2][0],cube[1][0][2],cube[2][0][0]}=={UP,LEFT,FRONT}):
        if(cube[1][0][2]==UP):
            print("整体逆时针旋转")
            gn()
            OrecR()
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体旋转两次")
            gn();gn()
        elif(cube[2][0][0]==UP):
            OrecL()
            print("整体顺时针旋转")
            gs()
            OrecR()
            print("整体逆时针旋转")
            gn()
    elif({cube[0][2][2],cube[2][0][2],cube[3][0][0]}=={UP,LEFT,FRONT}):
        if(cube[0][2][2]==UP):
            print("整体旋转两次")
            gn();gn()
            OrecL()
            print("整体旋转两次")
            gn();gn()
        elif(cube[2][0][2]==UP):
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体旋转两次")
            gn();gn()
            OrecR()
            print("整体逆时针旋转")
            gn()
        elif(cube[3][0][0]==UP):
            print("整体顺时针旋转")
            gs()
            OrecL()
            print("整体逆时针旋转")
            gn()
    elif({cube[0][0][2],cube[3][0][2],cube[4][0][0]}=={UP,LEFT,FRONT}):
        if(cube[0][0][2]==UP):
            OrecR()
            print("整体顺时针转动")
            gs()
            OrecR()
            print("整体逆时针转动")
            gn()
        elif(cube[3][0][2]==UP):
            OrecL()
        else:
            print("整体逆时针转动")
            gn()
            OrecR()
            print("整体顺时针转动")
            gs()
    elif({cube[0][0][0],cube[4][0][2],cube[1][0][0]}=={UP,LEFT,FRONT}):
        if(cube[0][0][0]==UP):
            print("整体顺时针转动")
            gs()
            OrecR()
            print("整体逆时针转动")
            gn()
        elif(cube[4][0][2]==UP):
            print("整体转动两次")
            gs();gs()
            OrecR()
            print("整体转动两次")
            gs();gs()
        else:
            OrecR()
            print("整体转动两次")
            gs();gs()
            OrecL()
            print("整体转动两次")
            gs();gs()
    else:
        print("出错了！")
    print("已拼好左前角")
    show()

def recTwo():
    if({cube[0][2][2],cube[2][0][2],cube[3][0][0]}=={UP,LEFT,BACK}):
        if(cube[0][2][2]==UP):
            print("整体逆时针旋转")
            gn()
            OrecL();OrecL()
            print("整体顺时针旋转")
            gs()
            OrecR()
        elif(cube[2][0][2]==UP):
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体顺时针旋转")
            gs()
        elif(cube[3][0][0]==UP):
            OrecR()
            print("整体逆时针旋转")
            gn()
            OrecL();OrecL()
            print("整体顺时针旋转")
            gs()
    elif({cube[0][0][2],cube[3][0][2],cube[4][0][0]}=={UP,LEFT,BACK}):
        if(cube[0][0][2]==UP):
            OrecR()
        elif(cube[3][0][2]==UP):
            print("整体逆时针旋转")
            gn()
            OrecL();OrecL()
            print("整体顺时针旋转")
            gs()
        else:
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体顺时针旋转")
            gs()
            OrecR()
            print("整体逆时针旋转")
            gn()
            OrecL();OrecL()
            print("整体顺时针旋转")
            gs()
    elif({cube[0][0][0],cube[4][0][2],cube[1][0][0]}=={UP,LEFT,BACK}):
        if(cube[4][0][2]==UP):
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体顺时针转动")
            gs()
            OrecR()
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体顺时针转动")
            gs()
            OrecR()
        elif (cube[1][0][0]==UP):
            print("整体逆时针旋转")
            gn()
            OrecL()
            print("整体顺时针转动")
            gs()
            OrecR()
    else:
        print("出问题了")
    print("已拼好左后角")
    show()

def recAll():
    while(cube[0][2][2]!=UP):
        OrecR()
        print("整体逆时针旋转")
        gn()
        OrecL()
        print("整体顺时针旋转")
        gn()
    print("已拼完")
    show()

os.system('chcp 65001&cls')

print("请拿着你的魔方,使得红色面对你,白色(黑色)在顶部,绿色在左手边(若不愿意,请修改源码第三行)\n\n")
print("此时橙色在后面,黄色在下面,蓝色在右手边\n\n")
print("'y' 代表 yellow, 'r' 代表 red ,blue,white,orange,green也类似。请按照要求输入\n\n")

cube = []
cube.append([[UP]*3]+[[UP]*3]+[[UP]*3])
cube.append([[LEFT]*3]+[[LEFT]*3]+[[LEFT]*3])
cube.append([[FRONT]*3]+[[FRONT]*3]+[[FRONT]*3])
cube.append([[RIGHT]*3]+[[RIGHT]*3]+[[RIGHT]*3])
cube.append([[BACK]*3]+[[BACK]*3]+[[BACK]*3])
cube.append([[DOWN]*3]+[[DOWN]*3]+[[DOWN]*3])

def sp(s):
    return [s[0],s[1],s[2]]
cube[0][0] = sp(input("顶部远离你三个元素,从左往右:"))
cube[0][1] = sp(input("顶部中间的三个元素,从左往右:"))
cube[0][2] = sp(input("顶部靠近你三个元素,从左往右:"))
cube[1][0] = sp(input("左手边顶部三个元素,从远往近:"))
cube[2][0] = sp(input("正面前顶部三个元素,从左往右:"))
cube[3][0] = sp(input("右手边顶部三个元素,从近往远:"))
cube[4][0] = sp(input("背面处顶部三个元素,从右往左:"))
print("以下步骤描述中,顺、逆时针为从上往下看、从前往后看、从右往左看")
os.system('pause&cls')

makeTen()
recUpTen()
print("\n警告:以下死板地先拼左前、再拼左后\n")
recOne()
recTwo()
recAll()
