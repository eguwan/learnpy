# 调用 sys 模组中的 arg= 列表
from sys import argv
# 给argv传递参数，第一个{0}是script 列表名，第二个是参数值
script, filename = argv

# 打开filename方法，并讲这个步骤赋值给 txt
txt = open(filename)
print(f"Here's your file {filename}:")  # 打印格式化语句，
print(txt.read())  # 读取打开的文件内容

print("Type the filename again:")
file_again = input("> ")  # 把输入的“> 和上面  应该输入的文件名" 赋值给 变量 file_again

txt_again = open(file_again)  # 把打开刚才输入的文件名赋值给 变量 txt_again

print(txt_again.read())  # 读取 内容并打印
