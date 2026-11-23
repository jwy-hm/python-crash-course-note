info1 = {"name":"ybz","pet":"dog"}
info2 = {"name":"yz","pet":"dog"}
info3 = {"name":"jwh","pet":"cat"}
pets = [info1,info2,info3]
for info in pets:
    print(f"My name is {info["name"]}, and my pet is a {info["pet"]}")