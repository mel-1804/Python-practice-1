# ✅↓ Write your code here ↓✅
line1 = "let it be,"
line2 = "there will be an answer,"
line3 = "whisper words of wisdom, let it be."

def sing():
    for i in range(11):
        if i == 4:
            print(line2)
        elif i == 10:
            print(line3)
        else:
            print(line1)

sing()

