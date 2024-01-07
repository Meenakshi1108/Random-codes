import math
tc=int(input())

for _ in range(tc):
	n,p,l,t=map(int,input().split())
 
	max_tasks=((n-1)//7)+1   

	lesson_days=math.ceil(p/(l+(t*2)))
	# print(u)

	task_days=math.ceil(max_tasks/2)

	rem_points=p-(max_tasks*t)

	if(rem_points<=0):
		ans2=math.ceil(p/(l+(t*2)))
		print(n-ans2)
		continue


	temp2=rem_points/l
	
	temp2=math.ceil(temp2)


	if task_days>lesson_days:
		print(n-lesson_days)
		continue

	ans=n-temp2
	print(ans)



	






