import os
import pyttsx3 as sp

print("ENABLE YOUR DEVICE AUDIO FOR BETTER EXPERIENCE")
sp.speak('Hay whats your name')
name=input('Hay whats your name:')
n='hello '+name
sp.speak(n)
print('Hello',name)

stop=['please','can','you','run','ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
wrd=''

i=0
while(i!=2):
	sp.speak("How can i help you :")
	txt=input("How can i help you :")
	txt=list(txt.split())

	if('dont' in txt):
		sp.speak('ok')
		print('ok')
	else:
		if(('open' in txt) or ('run' in txt)):  
			for i in txt:
				if i not in stop:
					wrd=i
			if wrd=='':
				print('sorry, please try again')
				sp.speak('sorry, please try again')
			else:
				print(wrd)
				os.system(wrd)
		else:
			sp.speak('sorry cant understand:')
			print('sorry cant understand:')

	print('Do you want someting else:')
	sp.speak('Do you want someting else')
	i=input()
	if i in ['no','NO','nope','exit','break','nothing','thanks','thankyou']:
		i=2

