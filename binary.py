# if __name__ == '__main__':
count=0
n = int(input())
while n:
    n=n&n<<1
    count+=1
print(count)