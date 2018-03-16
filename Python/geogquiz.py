#! python3
#script to generate 35 random quizzes (with the same questions) and their answer
#keys

import os, random, pyperclip

statescaps= {}
for i in pyperclip.paste().split('\n'): #copy data from:
    strings=list(i.split(' – '))        #https://www.importantindia.com/12430/list-of-states-and-capitals-of-india/
    strings[0].strip()                  #into statescaps dictionary
    strings[1].strip()
    strings2=list(strings[1].split(' '))
    strings2[0].strip()
    statescaps[strings[0]]=strings2[0]

if(not(os.path.isdir(r'C:\Users\Assassin123\Desktop\Quizzes'))):
    os.makedirs(r'C:\Users\Assassin123\Desktop\Quizzes')
os.chdir(r'C:\Users\Assassin123\Desktop\Quizzes')

initials=' '*20
creds='Geography Test\nName:\nGrade:\nRNo:\n\n'
init=initials+creds

for quiznum in range(35):
    quizfile=open('quiz%s.txt'%(quiznum+1),'w')
    keyfile=open(r'keyfile%s.txt'%(quiznum+1),'w')
    quizfile.write(init+'Tick the appropriate capital\n\n')
    keyfile.write(init+'Answer keys\n\n')
    states=list(statescaps.keys())
    random.shuffle(states)
    for quesnum in range(len(states)):
        correctcap=statescaps[states[quesnum]]
        caps=list(statescaps.values())
        del [caps[caps.index(correctcap)]]
        wrongcaps=random.sample(caps,3)
        answer=wrongcaps+[correctcap]
        random.shuffle(answer)
        quizfile.write('Q%s. %s:\n'%(quesnum+1,states[quesnum]))
        for i in range(4):
            quizfile.write('%s) %s  '%('ABCD'[i],answer[i]))
        quizfile.write('\n')
        keyfile.write('Q%s, %s\n'%(quesnum+1,'ABCD'[answer.index(correctcap)]))
    
    quizfile.close()
    keyfile.close()



