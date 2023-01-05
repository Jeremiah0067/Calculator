import re

beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search("Hello there!")
print(mo.group())

endsWithWorldRegex = re.compile(r"world!$")
mo_2 = endsWithWorldRegex.search("hello world!")
print(mo_2.group())

allDivgitsRegex = re.compile(r'^\d+$')
mo_3 = allDivgitsRegex.search("3495749537")
print(mo_3.group())

atRegex = re.compile(r'.{1, 2}at')
print(atRegex.findall("the cat in the mat sat on the flat hat"))

print(r"why say so/n")


