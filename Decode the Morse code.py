def decodeMorse(morseCode):
	morseCode = morseCode.strip
	morseWords = morseCode.split('   ')
	result = ''
	#i = 0
	for i in range (0,len(morseWords)):
		#i+=1
		if i != 0:
			result+=decodeMorseWord(morseWords[i])
	return result

decodeMorse =decodeMorse(morseCode)

# or

def decodeMorseLetter(letter):
	return MORSE_CODE[letter]

def decodeMorseWord(word):
	return word.split(' ').map(decodeMorseLetter).join('')

def decodeMorse(morseCode):
	return morseCode.trim().split('   ').map(decodeMorseWord).join(' ')


#对题目的理解比较困难,没有注意到3'   '和1' '的区别
#区分词,区分字母,反回
#没有意识到测试数据要去边,不熟悉列表的融合和分割
#函数间数据流转不熟悉
#思考方式有问题,用其它语言的方式来实现
