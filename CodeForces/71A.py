s=int(input())
args=[]
def convert(word):
    return f'{word[0]}{len(word)-2}{word[-1]}' if len(word)>10 else word
for _ in range(s):
    args.append(input())

for i in args:
    print(convert(i))