import re

test_string = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPRSTUVWXYZ

1234567890

Ha HaHa

$Ha

Meta Characters need to be escaped:
. $ * + ? { } ( )  | \

tomjerry.com

321-555-4321
123.555.1234
123*555*1234

Mr. Vivek
Mr Ankit
Mr. V

Mrs. Meghna
Mrs. Shelly
Ms Sonam

cat
mat
pat
bat

'''

Sentance = 'Start a sentance and then bring it to the end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
#pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#pattern = re.compile(r'[A-Za-z0-9.-]+@[A-Za-z-]+\.(com|edu|net)')


matches = pattern.findall(urls)

for match in matches:
    print(match)






"""
.    - Matches any character except new line
\d   - Digit (0-9)   
\D   - Not a Digit (0-9)
\w   - word character (a-z, A-Z, 0-9, _)
\W   - not a word character
\s   - whitespace (space, tab, newline)
\S   - not white space

ANCORS

\b   - word boundry (starts with white space or non alphanumeric char)
\B   - not a word boundry
^    - beginning of a string
$    - end of a string

[]   - matches characters in brackets
[^ ] - matches characters not in brackets


QUANTIFIERS

*   - 0 or more
+   - 1 or more
?   - 0 or 1
{3} - Exact Number
{3, 4} - Range of Numbers (Minimum, Maximum)    
"""