# At least 8 char logn
# contain any sort letters, numbers $%#@
# has to end with a number
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") # ho(w a)re matches the w within the first group/ . matches with space/ a as the first letter of the word (are)
# string = 'b@b.com'
string = 'Andrei'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'hdjk'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)
print(a)
