for i in range(1,31):
    if i % 3 == 0:
        if i % 5 ==0:
            print("fizbuzz")
        else:
            print("fizz")
    elif i % 5 ==0:
        print("buzz")
    else:
        print(i)