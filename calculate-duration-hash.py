# Python 3 code to demonstrate 
# SHA hash algorithms. 
  
import hashlib 
import time
import random
import string

# initializing string 
str = "Webhook Signature"

random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(64)])

start = time.time()
print("start hashing... ")
print ("\r") 
print("random_str", random_str)
# encoding Webhook Signature using encode() 
# then sending to SHA256() 
for num in range (0,10000):
	result = hashlib.sha256(random_str.encode()) 

# calculate current date and time
print("done hashing")
print ("\r") 
done  = time.time()
elapsed = done - start
print("durations", elapsed) # in seconds

  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  
