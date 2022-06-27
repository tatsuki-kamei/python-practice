dictionary ={}
for i in range(1,31):
    if i % 3 ==0:
        a = f"{i//3}番目"
        dictionary[a] = i
print(f"作成したリスト{dictionary}")
