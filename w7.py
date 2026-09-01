
# Regular Expression
'''
email = input("Whats your email? ").strip()
if "@" in email and "." in email :
    print("Valid")
else:
    print("Invalid")
'''
'''
email = input("Whats your email? ").strip()
username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("Invalid")
'''
'''
email = input("Whats your email? ").strip()
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else:
    print("Invalid")
'''
# re library
'''
import re
email = input("Whats your email? ").strip()
#username, domain = email.split("@")

#if username and domain.endswith(".edu"):
if re.search("@", email):
    print("valid")
else:
    print("Invalid")
'''

'''
import re
email = input("Whats your email? ").strip()

#if re.search(".+@.+", email):
#if re.search("..*@.+", email):
#if re.search(r".+@.+\\.edu", email):
    print("valid")
else:
    print("Invalid")
'''
'''
import re
email = input("Whats your email? ").strip()

if re.search(r"^.+@.+\\.edu$", email):
    print("valid")
else:
    print("Invalid")
'''

'''
import re
email = input("Whats your email? ").strip()

if re.search(rf"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("Invalid")
'''

import re
email = input("Whats your email? ").strip()

if re.search(rf"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("Invalid")










































































































































































































