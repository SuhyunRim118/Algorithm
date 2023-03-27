grade = {"A+":4.5, "A0":4, "B+":3.5, "B0":3, "C+":2.5, "C0":2, "D+":1.5, "D0":1, "F":0}

sum = 0.0
total_credit = 0

for i in range(20):
	data = list(map(str, input().split()))
	
	if data[2] != "P":
		total_credit += float(data[1])
		sum = sum + float(data[1]) * grade[data[2]]

print(round(sum/total_credit, 6))