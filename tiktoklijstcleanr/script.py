import urllib.request
from cleantext import clean
import re

import wget

text = open('./toktiklijst.txt', 'r', encoding="utf8")
text = text.read()
filtered = clean(text, no_emoji=True)

new = open('toktiklijst-filtered.txt', 'w')
new.write(filtered)
new.close()

with open('toktiklijst-filtered.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('toktiklijst-filtered.txt', 'w') as fout:
    fout.writelines(data[1:])


file1 = open('toktiklijst-filtered.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    name = line.strip().split(',')[1]
    url = line.strip().split(',')[0]

    re.match(r'girl', name, re.IGNORECASE)
    if name == 'girl':
        continue

    files = f'./output_directory/{name}.xml'
    # print(f'{count}. {name} - {url}')
    urllib.request.urlretrieve(url, files)

    def convert(lst):
        return ' '.join(lst)
    with open(files, 'r', encoding="utf8" ) as f:
        for lines in f:
            test = convert(lines)
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', lines)
    filtered_lists = list(filter(lambda x: (".jpg" in x), urls))

    print (f'{count}. {filtered_lists}')

    # if count == 10:
    break
