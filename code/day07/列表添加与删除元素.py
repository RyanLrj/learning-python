languages = ['python','java','c++']
languages.append('javascript')
print(languages)
languages.insert(0, 'SQL')
print(languages)

if 'swift' in languages:
    languages.remove('swift')
if 'javascript' in languages:
    languages.remove('javascript')
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
print(languages)
languages.clear()
print(languages)

items = [1,2,3,4]
del items[1]
print(items)

