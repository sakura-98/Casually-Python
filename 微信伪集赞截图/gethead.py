import itchat
import os

try:
    os.mkdir('res')
except Exception:
    pass

itchat.auto_login()
index = 1
for friend in itchat.get_friends():
    img = itchat.get_head_img(userName=friend["UserName"])
    path = "./res/%d.png"%index
    index += 1
    with open(path,'wb') as f:
        f.write(img)
itchat.logout()
