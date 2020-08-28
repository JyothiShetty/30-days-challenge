n=int(input())
name_number=[input().split() for _ in range(n)]
phoneBook={k:v for k,v in name_number}

while True:
    try:
        name=input()
        if name in phoneBook:
            print(str(name) +'=' + phoneBook[name])
        else:
            print('Not found')
    except:
        break