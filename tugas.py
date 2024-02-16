print (">"*30)
i  = 1
count  = 20
space = 20
while True:
    if i  == 20:
        break
    elif i % 2:
        print(" " * (space // 2), "+" * i)
    
    i += 1
    space-=1

i  = 21
count  = 0
space = 0
while True:
    if i  == 0:
        break
    elif i % 2:
        print(" " * (space // 2), "+" * i)
    
    i -= 1
    space+=1

