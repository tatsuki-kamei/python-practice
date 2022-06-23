input_number=int(input("好きな整数を入力してください >"))
if type(input_number) is int:
    print(input_number**2)
else:
    print("error")