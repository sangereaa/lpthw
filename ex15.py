from sys import argv #读取argv模块

script, filename = argv #输入参数

txt = open(filename) #打开filename文件 并赋值于txt

print(f"Here's your file {filename}:") # 这是你的文件名
print(txt.read()) #读取并打印

#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())