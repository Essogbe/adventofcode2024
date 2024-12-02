with open('input.txt','r') as f:
	a=f.readlines()
	x,y=[],[]
	for i in a:
		e,f=i.split()
		x.append(int(e))
		y.append(int(f))
	# result = sum([abs(i-j) for i,j in zip(sorted(x),sorted(y))])
	dico = sum([y.count(i)*i for i in x]) #part2
	print(dico)
	