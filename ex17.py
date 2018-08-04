from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file)  # assign the 打开文件 赋值给 变量 in_file
indata = in_file.read()  # 把读取的文件内容赋值给 indata

print(f"The input file is {len(indata)} bytes long")  # 打印读取的文件长度 bit

print(f"Does the output file exist? {exists(to_file)}")  # 检查要写入的文件是否存在
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')  # 以写入模式打开目标文件，并将此方法赋值给 out_file
out_file.write(indata)  # 把indata的值写入到out_file

print("Alright, all done.")

out_file.close()
# outdata = to_file.encode

# # print(out_file.read())
in_file.close()
