def condition2(l):
	check =[abs(l[i]-l[i+1])>=1 and abs(l[i]-l[i+1])<=3 for i in range(len(l)-1)]
	return all(check)

def is_good(l):
    return (sorted(l)==l or sorted(l,reverse=True)==l) and condition2(l)
with open("input.txt",'r') as f:
	lines= f.readlines()
	count=0
	for line in lines:
		l=[int(i) for i in line.split()]
		if is_good(l):
			count+=1

		#part2
		else:
			li=[]
			for el in range(len(l)):
				temp=l.copy()
				temp.pop(el)
				li.append(is_good(temp))
			if any(li):
				count+=1

	print(count)