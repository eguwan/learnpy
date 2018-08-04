# 用一行命令完成ex17.py程序的功能！我做到了！！！！
# ___________________________________________________________________
# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
# in_file = open(from_file)  # assign the 打开文件 赋值给 变量 in_file
# indata = in_file.read()  # 把读取的文件内容赋值给 indata
# indata = open(from_file).read()

# input(f"""The input file is {len(open(from_file).read())} bytes long.
#     Does the output file exist? {exists(to_file)}.
#     Ready, hit RETURN to continue, CTRL-C to abort.""")  # 打印读取的文件长度 bit

# print(f"Does the output file exist? {exists(to_file)}")  # 检查要写入的文件是否存在
# print(f"Ready, hit RETURN to continue, CTRL-C to abort.")


# out_file = open(to_file, 'w')  # 以写入模式打开目标文件，并将此方法赋值给 out_file
# out_file.write(indata)  # 把indata的值写入到out_file
open(input("要写入的文件："), "w").write((open(input("要复制的文件："))).read())
print("Alright, all done.")

# print("to_file:", repr(open(to_file)))
# open(to_file).close()
# open(from_file).close()

# 心得，文件名赋值的变量只能代表文件名字，不能直接对内容进行操作和关闭文件名，的打开后在操作
