import sys

in_filename = sys.argv[1]
out_filename = sys.argv[2]

label_to_level = {'OBJECTIVE': 0, 'BACKGROUND': 0, 'METHODS': 1,
				  'RESULTS': 2, 'CONCLUSIONS': 3}

level = 0
with open(out_filename, 'w') as outFile:
	with open(in_filename, 'r') as inFile:
		for line in inFile:
			if line.startswith('###'):
				abstract_title = line.strip().split('#')[-1]
				levels = []
				lines = []
				outFile.write(line)
			elif not line.strip():
				lines_cp = lines[:]
				for level, line in zip(levels[::-1], lines_cp[::-1]):
					if level <= 0:
						print(abstract_title+' Wrong line: '+lines.pop())
					elif level == 1 and len(line.strip().split()) < 4:
						print(abstract_title+' Wrong line: '+lines.pop())
					else:
						break
				for line in lines:
					outFile.write(line)
				outFile.write('\n')	
			else:
				curr_level = label_to_level[line.strip().split()[0]]
				lines.append(line)
				levels.append(curr_level)