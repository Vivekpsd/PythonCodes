import re

pattern = '[A-Z]\w+@[a-z]\w+\.[soy]+'

text = '''
CoreyMSchafer@gmail.com
'''

matches = re.findall(pattern, text)

if len(matches) == 0:
    print("No")