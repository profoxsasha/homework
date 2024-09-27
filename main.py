# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def area(a,b):
    return a*b

def p(a,b):
    return a+b+a+b

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi("саааааааашшшшшшшшшшшшшаааааааааааааааааааа")
    bars = [(1, 2), (3, 4),(10, 20),(100, 200),(1000, 2000),(7, 9),(123, 123),(15, 25),(16, 99),(66, 11),(100, 1),(177, 2777)]
    for ab in bars:
        a = ab[0]
        b = ab[1]
        print("площадь премауголника со сторанами " + str(a) + " и " + str(b) + " равна " +str(area(a,b)))
        print("перимитр премауголника со сторанами " + str(a) + " и " + str(b) + " равен " + str(p(a, b)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
