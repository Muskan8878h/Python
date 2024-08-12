sentence=str(input())
def fun(sentence):
    word=sentence.split()
    capital=(word.capitalize()for word in word)
    return' '.join(capital)
final=fun(sentence)


sentence=input().split()
sentence.reverse()
sentence.join(capital)
print(sentence)