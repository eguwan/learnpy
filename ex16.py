from sys import argv
script = str(input("输入要打开的py文件"))
filename = str(input("要编辑的文件是什么？"))
# print(script, repr(script))
# print(filename, repr(filename))

argv = script, filename  # 这样的话加上上面的头子就可以了
# script, filename = argv  书上这么写老提示有错，但程序能运行，但是加上上面的头子，就不行了
# argv 在等号 左边 和右边有什么区别？
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^c).")
print("If you do want that, hit RETURN.")

input("?")

print("opening the file...")
target = open(filename, 'x')


print("runcating the file. Goodbye!")
print("How I'm going to ask you for three lines.")

line1 = input("line1 :")
line2 = input("line2: ")
line3 = input("line3: ")


print("I'm going to write those to the file. ")

target.write(f"{line1}\n{line2}\n{line3}")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
print("And finally, we close it.")
target.close
print(repr(target))
