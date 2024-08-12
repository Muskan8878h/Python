def minion_game(string):
    # your code goes here
    vowels ="AEIOU"
    kevin_scores = stuart_score = 0
    length=len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin_scores += length-i
        else:
            stuart_score += length-i
    if stuart_score >= kevin_scores:
        print(f'Stuart {stuart_score}')
    elif kevin_scores >= stuart_score:
        print(f'Kevin { kevin_scores}')
    else:
        print(Draw)


if __name__ == '__main__':
    s = input()
    minion_game(s)