

def find_Dist(x1,y1,x2,y2):
	a = abs(x1-x2)+abs(y1-y2)
	return a

def find_cost(dist,cost):
	b = dist*cost
	return b
#现在终于要用超过一个函数了
#这种成本计算的问题idea应该还是比较直接的，一样是通过if语法来判断
inp_arg = sys.argv

print(inp_arg)

n = int(inp_arg[1])

m = int(inp_arg[2])

c = float(inp_arg[3])#注意只有这个变量是有小数点的

x1 = int(inp_arg[4])

y1 = int(inp_arg[5])

x2 = int(inp_arg[6])

y2 = int(inp_arg[7])

if(x1<0 or x1>n or x2<0 or x2>m):
	print("Invalid input input must be in range")

else:
	dist = find_Dist(x1,y1,x2,y2)

cost = find_cost(dist,c)
print("The trip will cost $"+str(cost),"and youwill have travelled",dist,"blocks")
#话说原来“，”本身就是自带空格的，学到了，以后要用format才行

