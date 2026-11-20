name = ['赵耀','贺靖雯','阿米米','李时之','方乐']
print(f"{name[0]}:\n\tGood morning!")
print(f"{name[1]}:\n\tGood morning!")
print(f"{name[2]}:\n\tGood morning!")
print(f"{name[3]}:\n\tGood morning!")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(-1, 'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last1 = motorcycles[-1]
del motorcycles[-1]
print(f"the last one is {last1}")

motorcycles = ['honda', 'yamaha', 'suzuki']
last1 = motorcycles.pop()
print(f"the last one is {last1}")