import bcrypt
#Store password:
password = str(input("input passowrd:"))
#store username
username = str(input("input username"))
#Encode password:
password = password.encode('utf-8')
#Encode username
username = username.encode('utf-8')
#Encrypt password
hashed = bcrypt.haspw(password, bcrypt.gensalt(10))
#Encrypt username
hashed = bcrypt.haspw(username,bcrypt.gensalt(10))
#create an authenticating password input field
check = str(input("check password: "))
#Create an authenticating username input field
check = str(input("check username"))
# Encode the authenticating password
check = check.encode('uft-8')
# Encode the authenticating username
check = check.encode('utf-8')
#use coditions to compare the aut password with stored password
if bcrypt.checkpw(check, hashed):
     print("login success")
else:
     print("incorrect password or username")
     quit()   



