name = "yubo zhao"
print(name.title())
print(name.upper())
print(name.lower())
first_name = 'yubo'
last_name = 'zhao'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
# 2.3.3 使用制表符或换行符来添加空白
print("第一列\t第二列\t第三列")
print("第一列\t第二列\n第二行第一列\t第二行第二列")
# 2.3.4 删除空白
favorite_language = 'python '
favorite_language
favorite_language.rstrip()
favorite_language
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
# lstrip() 删除左边空白 rstrip() 删除右边空白 strip() 删除左右两边空白
favorite_language = ' python '
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())
# 2.3.5 删除前缀
my_url = "https://zhzz.safehome.eu.org"
my_url.removeprefix('https://')
print(my_url,my_url.removeprefix('https://'))

#2.3.6 如何在使用字符串时避免语法错误
message = "One of Python's strengths is its diverse community."
print(message)
# 在编写程序时，编辑器的语法高亮功能可帮助你快速找出 某些语法错误。
# 如果看到 Python 代码以普通句子的颜色显示， 
# 或者普通句子以 Python 代码的颜色显示，
# 就可能意味着文件中 存在引号不匹配的情况。

#练习2.3个性化消息
name = "yubo zhao"
print(f"\tHello {name.title()}, would you like to learn some Python today?")

# 练习 2.4：调整名字的大小写　用变量表示一个人的名字，
# 再分别以全小写、全大写和首字母大写的方式显示这个人名。
zy_name = "yao zhao"
print(zy_name.lower(),zy_name.upper(),zy_name.title())

#练习 2.5：名言 1　找到你钦佩的名人说的一句名言，
# 将这个名人的姓名和名言打印出来。输出应类似于下面这样（包括引号）。
#　　Albert Einstein once said, 
# “A person who never made a mistake never tried anything new.”
print("\tAlbert Einstein once said, “A person who never made a mistake never tried anything new.”")

#练习 2.6：名言 2　重复练习 2.5，
# 但用变量 famous_person 表示名人的姓名，
# 再创建要显示的消息并将其赋给变量 message，然后打印这条消息。

famous_person = "Albert Einstein"
message = (f"\t{famous_person} once said, “A person who never made a mistake never tried anything new.”")
print(message)

# 练习 2.7：删除人名中的空白　用变量表示一个人的名字，并在
# 其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和 "\n" 各一次。
#打印这个人名，显示其开头和末尾的空白。然后，分别使用函数
#lstrip()、rstrip() 和 strip() 对人名进行处理，并将结果打印出来。
name = "\t\n yubo zhao \n\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

#练习 2.8：文件扩展名　Python 提供了 removesuffix() 方法，
# 其工作原理与 removeprefix() 很像。
# 请将值'python_notes.txt' 赋给变量 filename，
# 再使用removesuffix() 方法来显示不包含扩展名的文件名，
# 就像文件浏览器所做的那样。
filename = 'python_notes.txt'
print(filename)
print(filename.removesuffix('.txt'))