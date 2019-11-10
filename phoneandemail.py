#! python3
#Goal, fetch phone numbers and email addresses from a pdf file

import re, pyperclip

#TODO:
# *Create a regex object for phone numbers

example_string = """
DIRECTOR'S OFFICE Phone Fax E-Mail
Shane Broadway 501-371-2031 501-371-2003 UShane.Broadway@adhe.edu
Director
Harold Criswell 501-371-2029 501-371-2003 Harold.Criswell@adhe.edu
Deputy Director
Nichole Abernathy 501-371-2030 501-371-2003 UNichole.Abernathy@adhe.eduU
(501) 372 5020
321-2423
#Phone nums look like: 555-555-5555, 555-5555, (555) 555-5555 555-5555 ext 12334, ext 12345, x12345
"""

#re.VERBOSE makes it easier to split things over severa lines
#Phone nums look like: 555-555-5555, 555-5555, (555) 555-5555 555-5555 ext 12334, ext 12345, x12345
oldphonere = re.compile(r'''
(\d\d\d)*
(\s|-)*
\d\d\d
(\s|-)
\d\d\d\d
((\s)?(ext|x)(\.))*
((\s)?(\d{2,5}))*
'''
,re.VERBOSE)

# Om man skriver (...) sa blir det en "capture group"
# Istallet kan man skriva (?:...) for att bara gruppera utan att paverka vad som hamtas ut
phonere = re.compile(r'''
(?:\(?\d{3}\)?(?:\s|-)*)?
(?:\d{3}(?:\s|-)*)?
\d{4}?
(?:\s*(?:ext\s*|x)\d{2,5})?
''', re.VERBOSE)

# *Crete a regex object for emails
mailre = re.compile(r'''
[a-zA-Z0-9_.+]*
@
[a-zA-Z0-9_.+]*
'''
, re.VERBOSE)
# * Get the text off the clipboard
text = pyperclip.paste()
# * Extract emails and phone
allphonenums = phonere.findall(text)
allemails = mailre.findall(text)

print(allphonenums)
print(allemails)


# * Copy extracted data to clipboard
