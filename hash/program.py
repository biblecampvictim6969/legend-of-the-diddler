import bcrypt 

password = 'ahoj'

bytes = password.encode('utf-8') 

salt = bcrypt.gensalt() 

hash = bcrypt.hashpw(bytes, salt) 

print(hash)