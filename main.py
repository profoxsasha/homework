
if __name__ != '__main__':
    pass

else:

    # name = "sasha"
    # age = 10
    # print("Hello my name is %s! i'm %d years old!"%(name,age))

    name1 = "sasha"
    age1 = 10
    name2 = "Vova"
    age2 = 10
    name3 = "Tima"
    age3 = 11
    print("name\t\tage\n%s\t\t%d\n%s\t\t%d\n%s\t\t%d"%(name1,age1,name2,age2,name3,age3))

    a = int(input("введите число"))
    m = int(input("введите месец"))
    y = int(input("введите год"))
    if(a<=0 or a >31):
        print("неверная дата")
    elif(m<=0 or m>12):
        print("неверная дата")
    else:
        print("%d.%d.%d"%(a,m,y))