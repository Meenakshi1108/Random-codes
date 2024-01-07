#A

t=int(input())
for _ in range(t):
	a,b=list(map(int,input().split()))
	diff=a-b
	if (diff%2==1):
		print("Alice")
	else:
		print("Bob")



#B

from collections import Counter
t=int(input())
for _ in range(t):
	n=int(input())
	s=input()
	fq=Counter(s)
	# print(fq)
	if(fq['+']==fq['-']):
		print(0)
	else:
		print(abs(fq['+']-fq['-']))





#C
t = int(input())

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	x=(float('inf'))
	y=(float('inf'))
	t=0
	for i in a:
		if(x>y):
			x,y=y,x
		if(i<=x):
			x=i
		elif(i<=y):
			y=i
		else:
			x=i
			t+=1
	print(t)


