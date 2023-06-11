import re

# pattern = "\d{10}"
pattern = "[^]"

text = '''
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPRSTUVWXYZ 1234567890
Ha HaHa
$Ha
Meta Characters need to be escaped:
. $ * + ? { } ( )  | \
tomjerry.com
321-555-4321
123.555.1234
123*555*1234
(999)444-7777
Mr. Vivek
Mr Ankit
Mr. V
Mrs. Meghna
Mrs. Shelly
Ms Sonam
cat mat pat bat
'''

matches = re.findall(pattern, text)

for match in matches:
    print(match)