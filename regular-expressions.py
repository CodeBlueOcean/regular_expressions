import re

pattern = re.compile('search this inside of this text please! Andrei')
string = 'search this inside of this text please! Andrei'

# print('search' in string)
# print(re.search('this', string))
# this not work 

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a)
print(b)
print(d)
print(c)

# a = re.search('thIs', string) #this not work, can't read the above string.
a = re.search('this', string)
print(a.span())
print(a.start())
print(a.group())
print(a.end())

re.search('this', string)


