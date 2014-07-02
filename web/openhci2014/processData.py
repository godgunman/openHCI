#!/usr/bin/python
with open("data.txt","r") as inputFile:
	with open("output.txt","w") as outputFile:
		numOfLine = 0
		for line in inputFile:
			if numOfLine%12 == 0:
				outputFile.write('<div class="row">\n')
			numOfLine = numOfLine + 1
			if numOfLine%2 == 1:
				outputFile.write('<div class="two columns">\n')
				outputFile.write('<span>')
				outputFile.write(line)
				outputFile.write('</span>\n')
				outputFile.write('</div>\n')

			# if numOfLine%2 == 0:
			# 	outputFile.write('<span>')
			# 	outputFile.write(line)
			# 	outputFile.write('</span>\n')
			# 	outputFile.write('</div>\n')

			if numOfLine%12 == 0:
				outputFile.write('</div>\n')

		# outputFile.write('<div class="row">\n')
		# outputFile.write('<div class="two columns">\n')
		# outputFile.write('<span>')
		# outputFile.write('</span>')
		# outputFile.write('</span><br>')
		# outputFile.write('</div>\n')
		# outputFile.write('</div>\n')
