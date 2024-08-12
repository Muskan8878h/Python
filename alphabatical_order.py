my_str=input()
words=[word.capitalize() for word in my_str.split()]
print(words)
words.sort()
for i in words:
    print(i)

