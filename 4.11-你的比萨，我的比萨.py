pizzas = ["pizza1","pizza2","pizza3"]
for pizza in pizzas:
    print(f"I like {pizza}")
print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append("pizazazazaza")
friend_pizzas.append("pizza4")
print(f"“My favorite pizzas are:{pizzas}")
for friend_pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are:{friend_pizza}")