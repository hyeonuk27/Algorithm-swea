import sys
sys.stdin = open('input.txt')

headline = input()

new_headline = ''
for i in headline:
    if ord(i) < 97:
        new_headline += i
    elif ord(i) >= 97:
        new_headline += chr(ord(i)-32)

print(new_headline)