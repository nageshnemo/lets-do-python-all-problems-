#how to call functions of another directory that is in pur.py and sales.py

import sales as s   #if you directly call a fn it looks for stcak wheere references are not ther to put all fn refernces we requires import
import pur as p

#s.create_customer()
print s.a
print s.b
print s.c

#p.create_supplier()
#why we cannot call these fn from here because both these fn are not defined here so thats why if we are executing wwe get a error