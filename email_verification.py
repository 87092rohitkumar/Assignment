import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):
    if (re.search(regex, email)):
        return (email)
lst = []
n = int(input("please enter how many numbers of email to verify: "))

for _ in range(1,n+1):
    lst.append((check(input("please enter your email"))))
for num in lst:
    print(num)