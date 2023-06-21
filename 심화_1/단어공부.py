text_input = str(input())
text_input=text_input.upper()


text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_save_number = [0 for i in range(26)]



for i in range(len(text_input)):
    text_save_number[text.find(text_input[i])] += 1


max = int(0)
max_check = int(0)
for i in range(26):
    if(max <= text_save_number[i]):
        max = text_save_number[i]
        max_len = i


duplication = False
for i in range(26):
    if(max == text_save_number[i] and max_len != i):
        duplication = True


if(duplication == True):
    print("?")
else:
    print(text[max_len])