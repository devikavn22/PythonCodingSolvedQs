def calculate_unique(M, n):
	ells = [i+1 for i in range(n)]
	for i in range(n):
		row = M[i]
		col = [M[j][i] for j in range(n)]
		for el in ells:
			if (el not in row) or (el not in col):
				return False
	return True
n = int(input())
M = []
for i in range(n):
	row = [int(i) for i in input().split()]
	while len(row) != n:
		row = [int(i) for i in input().split()]
	M.append(row)
print(calculate_unique(M, n))