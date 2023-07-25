def Calc(frequency):
    i = 1
    total = 0
    while i <= frequency:
        num = input("Please enter a value: ")
        total += float(num)
        i += 1
    print("The total is " + str(total))
    split = total/4
    print("The cost per person is " + str(split))

Greeting = input("Hello, please enter your name: ")
Response = input("Hello " + Response + "! I hope you have a shitty day!")
items = input("How many items would you like to tally up?: ")
Calc(float(items))
