def test(p):
	doubles = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

	prev_c = p[0]
	for i in range(1,len(p)):
		c = p[i]
		if int(c) < int(prev_c):
                        return False

		if prev_c == c:
			doubles[c] += 1
		
		prev_c = c

	# Find all characters which fit only two adjacent doubles (e.g 111122 => 2)
	fits = {k: v for k, v in doubles.items() if v == 1}
	return sum(map(len, fits)) > 0

count = 0
for i in range(136760, 595730):
	if test(str(i)):
		count += 1
print(count)
