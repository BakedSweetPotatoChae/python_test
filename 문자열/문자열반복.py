count = int(input())


for i in range(count):
    text_1, text = map(str, input().split())
    for j in range(len(text)):
        for k in range(int(text_1)):
            print(text[j],end = "")
    print()