numberDict = dict()
numberDict[0] = "zero"
numberDict[1] = "one"
numberDict[2] = "two"
numberDict[3] = "three"
numberDict[4] = "four"
numberDict[5] = "five"
numberDict[6] = "six"
numberDict[7] = "seven"
numberDict[8] = "eight"
numberDict[9] = "nine"
numberDict[10] = "ten"
numberDict[11] = "eleven"
numberDict[12] = "twelve"
numberDict[13] = "thirteen"
numberDict[14] = "fourteen"
numberDict[15] = "fifteen"
numberDict[16] = "sixteen"
numberDict[17] = "seventeen"
numberDict[18] = "eighteen"
numberDict[19] = "nineteen"
numberDict[20] = "twenty"
numberDict[30] = "thirty"
numberDict[40] = "forty"
numberDict[50] = "fifty"
numberDict[60] = "sixty"
numberDict[70] = "seventy"
numberDict[80] = "eighty"
numberDict[90] = "ninety"

def contaDezenas(num):
	if (num <= 20):
		return len(numberDict[num])
	elif (num % 10 != 0):
		return len(numberDict[((num/10)*10)] + numberDict[(num%10)])
	else:
		return len(numberDict[((num/10)*10)])

def contaCentenas(num):
	if (num % 100 != 0):
		return len(numberDict[(num/100)] + "hundredand") + contaDezenas(num % 100)
	else:
		return len(numberDict[(num/100)] + "hundred")

count = 0
for i in range(1,1001):
	if i <= 99:
		count += contaDezenas(i)
	elif i <= 999:
		count += contaCentenas(i)
count += len("onethousand")
print count
