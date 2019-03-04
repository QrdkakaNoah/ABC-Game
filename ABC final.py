#Noah Gaviña
#2.21.19
#ABC Game
while True:
    name = input("Hello user, what is your name?:")
    if name == "whiteface":
        exit()
    print("Hmm, " +name+ ", interesting...")
    print("I am going to order 3 numbers in order from greatest to least for you.")
    print("ONLY INSERT NUMBERS OR I WILL CRASH AND MY BLOOD WILL BE ON YOUR HANDS.")
    a=int(input("What will number a be?:"))
    b=int(input("What will number b be?:"))
    c=int(input("What will number c be?:"))
    if (a>b) and (a>c) and (b>c):
        print("Then the order is:")
        print(a,b,c)
    if (a>b) and (a>c) and (b<c):
        print("Then the order is:")
        print(a,c,b)
    if (a<b) and (b>c) and (c<a):
        print("Then the order is:")
        print(b,a,c)
    if (a<b) and (b>c) and (c>a):
        print("Then the order is:")
        print(b,c,a)
    if (a<b) and (b<c):
        print("Then the order is:")
        print(c,b,a)
    if (a>b) and (a<c):
        print("Then the order is:")
        print(c,a,b)
    print("Thank you for playing with me, I am going to reset and forget you now, goodbye "+name+".")
