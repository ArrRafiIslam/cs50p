
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

if re.search(rf"^[^@]+@[^@]+\\.edu$", email):
    print("valid")
else:
    print("Invalid")
'''
'''
import re
email = input("Whats your email? ").strip()

if re.search(rf"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\\.edu$", email):
    print("valid")
else:
    print("Invalid")
'''
'''
import re
email = input("Whats your email? ").strip()

#if re.search(rf"^\\w+@\\w+\\.edu$", email):
if re.search(rf"^\\w+@\\w+\\.(com|net|edu|gov|org|io)$", email):
    print("valid")
else:
    print("Invalid")
'''
'''
import re
email = input("Whats your email? ").strip()

if re.search(rf"^\\w+@\\w+\\.(com|net|edu|gov|org|io)$", email):
    print("valid")
else:
    print("Invalid")
'''
# Case Sentivity
'''
import re
email = input("Whats your email? ").strip()

if re.search(rf"^\\w+@\\w+\\.(com|net|edu|gov|org|io)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")
'''
'''
import re
email = input("Whats your email? ").strip()

if re.search(rf"^\\w+@(\\w+\\.)?\\w+\\.(com|net|edu|gov|org|io)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")
'''

# clearning Up user input
'''
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
'''
'''
import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first =  matches.groups()
    name = first + " " + last
print(f"hello, {name}")
'''
'''
import re
name = input("What's your name? ").strip()
#matches = re.search(r"^(.+), (.+)$", name)
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
'''
'''
import re
name = input("What's your name? ").strip()
#matches = re.search(r"^(.+), *(.+)$", name)

if matches:= re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
'''


# Extracting user input

'''
url = input("URL: ").strip()
#print(url)
#username = url.replace("https://twitter.com/", "")
username = url.removeprefix("https://twitter.com/")
print(f"username: {username}")
'''

'''
import re
url = input("URL: ").strip()
#username = re.sub(r"https://twitter.com/", "", url)
username = re.sub(r"^(https?://)?(www\\.)?twitter\\.com/", "", url)
print(f"Username: {username}")
'''
'''
import re
url = input("URL: ").strip()
matches = re.search(r"^https?://(www\\.)?twitter\\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(2))
'''
import re
url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))







































































































































































































