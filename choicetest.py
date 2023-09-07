num = int(input())
answerlist = []
solutionlist =[]
count = 0

for a in range(num):
	a = input()
	answerlist.append(a)
for s in range(num):
	s = input()
	solutionlist.append(s)
for m in range(num):
	if answerlist[m] ==solutionlist[m]:
		count += 1
	
print(count)
	

	
	