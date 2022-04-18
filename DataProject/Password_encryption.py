import bcrypt
#Store password:
password = str(input("input passowrd:"))
#Encode password:
password = password.encode('utf-8')
#Encrypt password
hashed = bcrypt.haspw(password, bcrypt.gensalt(10))
#create an authenticating password input field
check = str(input("check password: "))
# Encode the authenticating password
check = check.encode('uft-8')
#use coditions to compare the aut password with stored password
if bcrypt.checkpw(check, hashed):
     print("login success")
else:
     print("incorrect password")
     quit()    



