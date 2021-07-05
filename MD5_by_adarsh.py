
#write a programe in python to generate MD5 of string data

import hashlib
m = hashlib.md5()
text = 'Isakai anime are the best'
m.update(text.encode('utf-8'))
print(m.hexdigest())
