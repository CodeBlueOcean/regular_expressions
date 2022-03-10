# example 1 
# import re

# pattern = re.compile(r"([a-z]).([a])") # ho(w a)re matches the w within the first group/ . matches with space/ a as the first letter of the word (are)
# string = 'search this inside of this text please! Andrei'

# # print('search' in string)
# # print(re.search('this', string))
# # this not work 

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(a.group(2))

# example
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") # ho(w a)re matches the w within the first group/ . matches with space/ a as the first letter of the word (are)
# string = 'b@b.com'
string = 'Andrei'

a = pattern.search(string)
print(a)
