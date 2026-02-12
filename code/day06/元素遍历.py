"""
元素的遍历

version: 1.0
author: Ryan
"""

#如果想逐个取出列表中的元素，有以下两种做法

languages = ['python','java','c++','php']
for index in range(len(languages)):
    print(languages[index])

for language in languages:
    print(language)