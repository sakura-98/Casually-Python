from PIL import Image
import os


'''
The size of the original pictures is 2048*2048, we'd like to change it into long ones.
Specially, up enlength 1000 pixels and down 5000 pixels.
'''
up,down = 1000,5000

def do(filename, up, down, depth=5):
    '''
    It seems that if we simply repeat the last column, there is great bias.
    What's more, if we use the center column to repeat, obviously we cannot get satisfied result.
    Therefore we choose column that is the 5th closest to edge.
    '''
    img = Image.open('origin\\'+filename)

    goal = Image.new(mode='RGB',size=(2048,up+2048+down))

    full = img.crop((0,0,2048,2048))
    goal.paste(full,(0,up))

    upline = img.crop((0,depth,2048,depth+1))
    for i in range(up):
        goal.paste(upline,(0,i))

    downline = img.crop((0,2048-depth,2048,2049-depth))
    for i in range(down):
        goal.paste(downline,(0,up+i+2048))

    print(filename+' done!')
    goal.save('deal\\'+filename)

for item in os.listdir('origin'):
    do(item,up,down)