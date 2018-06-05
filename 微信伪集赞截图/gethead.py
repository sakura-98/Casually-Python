import itchat
import os

try:
    os.mkdir('res')
except Exception:
    pass

itchat.auto_login()
for friend in itchat.get_friends():
    img = itchat.get_head_img(userName=friend["UserName"])
    path = "./res/"+friend['NickName']+".png"
    with open(path,'wb') as f:
        f.write(img)
itchat.logout()