menu = """
    #1: open tiktok
    #2: open instagram
    #3: play frisbee with dog
    #4: do coding
    #5: exit
"""

def f1():
    pass

def f2():
    pass


def f3():
    pass


def f4():
    pass

def f5():
    pass


print(menu)

options = {
    1: f1,
    2: f2,
    3: f3,
    4: f4
}

while True:
    try:
        choice = int(input("What would you like >>> "))
        if choice > 5 or choice < 1:
            raise Exception("Please choose an option from menu [1-5]")
    except ValueError:
        print("Please enter a number")
        continue
    except Exception as e:
        print(e)
        continue

    if choice == 5:
        break
