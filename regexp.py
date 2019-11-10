import re
message = "call me at 555-555-1111"

#create a regex object
#use .match(STRING) to match
#call the mat ojcets group() to get the matched sttring
#you can also use .findall
phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d')

mo = phoneNumRegEx.findall(message)
print(mo)
#print(mo.group())
