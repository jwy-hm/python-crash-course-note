favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

yinggaidiaocha = ["jen","phil","ybz","yz",]

for name in favorite_languages.keys():
    if name in yinggaidiaocha:
        print(f"感谢:{name}")
    else:
        print(f"求你来:{name}")