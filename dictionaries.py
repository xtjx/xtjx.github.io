def main(): #主函数定义在前，增加可读性
	message()#程序解释
	dic = build_dic()#创建字典
	active = 1 #程序运行状态选项
	while active != 0:
		bar()		
		user_in = input("1,查询,2,增加,3,删除,0,退出:")
		if is_number(user_in) == True : #判断输入的是不是一个数字
			user_inf = float(user_in)
			active = int(user_inf)
			if float(active) != user_inf or len(user_in) != 1 : 
				#判断输入的是不是浮点数或者多位数
				print("请输入正确的选项:")
			else:
				if active > 3 or active < 0 :
					print("请输入正确的选项:")
				if active == 1:
					search_dic(dic) #查找字典
				if active == 2:               
					dic = change_dic(dic) #更改字典
				if active == 3:
					dic = delete_dic(dic) #删除字典
				if active == 0:
					save_dic(dic) #保存字典
		else :
			print("请输入正确的选项:")
def message(): #程序功能解释
	print("==========================================================")
	print("= 这是我编写的第一个python程序!程序的基本功能:           =")          
	print("= 创建一个查询英文单词的字典,并且可以随时添加或删除条目. =")
	print("= 这可以用来保存英文文献中的单词并且随时查询,不错的主意! =")
	print("==========================================================")

def bar(): #这是一条分割线
	print("--------------------------------------------------")

def is_number(s):    #判断输入的是不是一个数
	try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）        
		float(s)        
		return True    
	except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"        
		pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）    
	try:        
		import unicodedata  # 处理ASCii码的包        
		unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数        
		return True    
	except (TypeError, ValueError):        
		pass    
	return False

	
def build_dic(): #创建或者读取词典文件来获取词典
	try:
		fp = open("dictionaries.txt",'r')
		print("找到已有文件，读取已有词典:")
		dic = {}
		for line in fp:
			v = line.strip().split(':')
			dic[v[0]] = v[1]
		fp.close()
	except FileNotFoundError:
		fp = open("dictionaries.txt",'w')
		print("未找到已有的词典文件，新建词典:")
		dic = {}
		fp.close
	return dic

def search_dic(dic): #查找字典中的单词
	key = input("请输入需要查询的单词:").rstrip()
	if key in dic.keys():
		print("已找到单词:"+ str(key) +","+str(dic[key]))
	else:
		print("未找到单词!")
		
def change_dic(dic): #更新字典
	key = "a"
	value = "a"
	print("进入增加单词模式，按q退出:")
	while key != "q" and value != "q" :
		key = input("请输入单词:").rstrip()
		if key != "q" and value != "q" :			
			value = input("请输入词义:").rstrip()
			dic[key] = value
			print("已更新单词:"+ str(key) +","+str(dic[key]))
	return dic

def delete_dic(dic): #删除单词
	key = input("请输入需要删除的单词:").rstrip()
	if key in dic.keys():		
		print("已删除单词:"+ str(key) +","+str(dic[key]))
		del dic[key]
	else:
		print("未找到单词!")
	return dic
		
def save_dic(dic):  #保存词典到文件
	fp = open("dictionaries.txt",'w')
	number = len(dic)
	num = int(1)
	bar()
	print("一共有"+str(number)+"个单词,如下所示:\n\n")
	for key,value in dic.items():
		words = key + ":" + value + "\n"
		word = str(num) + ":	" + key + ":" + value
		print(str(word))
		fp.write(str(words))
		num += 1
	fp.close()
	print("\n")
	bar()

def main_pause():
                main_pause = input( )
	
main()
main_pause()
