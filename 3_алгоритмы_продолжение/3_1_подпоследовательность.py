s = input()
t = input()

word_ix = -1

for el in t:
    if el == s[word_ix]:
        word_ix += 1

if word_ix == len(s):
    print(True)
else:
    print(False)
