cities = {"Chongqing":{"country":"China","population":"10000","fact":"lala"},
          "Beijing":{"country":"China","population":"10","fact":"lal212a"},
          "Shanghai":{"country":"China","population":"9998882","fact":"lal999a"}}
for city,info in cities.items():
    print(f"This city is {city}")
    country = info["country"]
    population = info["population"]
    fact = info["fact"]
    print(f"This city belongs to {country},has {population} populations and fact is {fact}.")