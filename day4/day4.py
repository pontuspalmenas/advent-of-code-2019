def test(p):
	double_digits = False
	prev_c = p[0]
	for i in range(1,len(p)):
		c = p[i]
		if int(c) < int(prev_c):
                        return False

		if prev_c == c:
			double_digits = True
		
		prev_c = c
	return double_digits

count = 0
for i in range(136760, 595730):
	if test(str(i)):
		count += 1
print(count)
