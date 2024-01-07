
#A
t=int(input())
for _ in range(t):
	p=input()
	col=p[0]
	row=p[1]

	for c in "abcdefgh":
		if c!=col:
			print(c+row)

	for r in "12345678":
		if r!=row:
			print(col+r)
	


#B
t=int(input())

for _ in range(t):
	s=input()
	l=[]
	u=[]
	for i in range(len(s)):
		if(s[i].isupper()):
			if(s[i]=="B"):
				if(len(u)!=0):
					u.pop()
			else:
				u.append(i)			
		elif(s[i].islower()):
			if(s[i]=="b"):
				if(len(l)!=0):
					l.pop()
			else:
				l.append(i)
	l=sorted(l+u)
	for i in l:
			print(s[i],end="")
	print()

	

#C
from collections import Counter
t=int(input())
for _ in range(t):
	n=int(input())
	s=input()
	fq=Counter(s)
	# print(fq)
	fin=0
	l= sorted(list(fq.values()),reverse=True)
	# print(l)
	total=l[0]
	ans=sum(l[1:])
	f=total-ans
	if(f<0):
		if(n%2==0):
			print(0)
		else:
			print(1)
	else:
		print(f)





			

