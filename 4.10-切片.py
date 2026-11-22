list = list(range(1,11))
lifangs = []
for number in list:
    lifang = number**3
    lifangs.append(lifang)
for lifang in lifangs:
    print(lifang)
print(f"The first three items in the list are:{lifangs[:3]}")

print(f"Three items from the middle of the list are:{lifangs[1:4]}")

print(f"The last three items in the list are:{lifangs[-3:]}")