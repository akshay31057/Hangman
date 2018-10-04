import random

def hangman_graphic(guesses):
		if guesses == 0:
			print "              "
			print "              "
			print "________      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 1:
			print "              "
			print "              "
			print "________      "
			print "|      |     "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 2:
			print "              "
			print "              "
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 3:
			print "              "
			print "              "
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "
		elif guesses == 4:
			print "              "
			print "              "
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "
		elif guesses == 5:
			print "              "
			print "              "
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "
		elif guesses == 6:
			print "              "
			print "              "
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "
		elif guesses == 7:
			print "              "
			print "              "
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "



words=["refrigerator","Conservatorium","autosuggestionist","giovanni","outrivalled"
 		"mastoparietal", "diakonikon","overdredge","irresoluteness","liverishness"
 		"downer","spoilt","exsiccator", 
 		"synechia","nonpromiscuous", "procrastinator", "ruthlessness", "bewilderment"] 
word=random.choice(words)
#print word
abc=int(len(word))
print "Please Enter Your Name!!!!!"
name=raw_input()
print "Hello,%s Welcome To Hangman!!!"%name
print 
print
alpha="abcdefghijklmnopqrstuvwxyz"
guesses=-1
answer="aeiou"
while guesses<8:
	mylen=0
	for i in word:
		if i in answer:
			print i,
			mylen=mylen+1
		else:
			print "_",

	
	if (mylen==abc):
		print "You Win"
		break

    

	hangman_graphic(guesses)
	print
	print "Please Enter A Letter"
	x=raw_input()
	#print x
	if x in answer:
		print "You Have Already Entered"
	elif x not in alpha:
		print "Please Enter A Valid Character"
	else:
		answer+=x

	if(x not in word):
		guesses=guesses+1
		print "You Entered A Wrong Character"
	elif(x in word):
		print "Woohoo!!You Guesses A Correct Letter"
	

if (guesses==8):  
	print "You Lost"
	
	


