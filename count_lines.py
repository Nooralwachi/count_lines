import re
def count_lines(filename):
	counter = 0
	seen=False
	with open(filename, 'r') as file:
		for line in file:
			line=line.strip()
			if len(line) > 0:
				if line[0] == '^' and line[-1]== '$':
					line=line[1:-1]
					seen = False
					for char in line:
						if char == '^':
							seen = True
						elif seen == True and char == '$':
							counter +=1
				else:
					counter +=1
	return counter
def count_lines2(filename):
    with open(filename, 'r') as file:
        count=0
        for line in file:
            line= line.strip()
            if line:
                if line[0] == '^' and line[-1] == '$':
                    line = line[1:-1]
                    start = line.count('^')
                    end = line.count('$')
                    if start == end and start !=0:
                        count+=1
                else:
                    count +=1
        return count
def count_lines3(filename):
	counter=0
	try:
		with open(filename, 'r') as f:
			p1 = '^\^.*\$\n$'
			p2 = '^\^\^+.*\$\$+\n$'
			for line in f:
				if line == '\n' or (re.match(p1, line) and not re.match(p2, line)):
					continue
				counter += 1
	except OSError:
		print(f'Cannot open file: {filename}')
	return counter

def counting_lines(filename):
	total_lines = 0
	pattern = r"^\^\w*.*\$$"
	with open(filename, 'r') as file:
		for line in file:
			if re.search(pattern,line):
				total_lines += 1
	return total_lines

print(count_lines('language.txt'))
print(count_lines2('language.txt'))
print(count_lines3('language.txt'))
print(counting_lines('language.txt'))