import re

text='my phone number is 9717067624.. don\'t call me on 1234567890.. it\'s a \
wrong number!'

regexObj=re.compile(r'\d{10}')
matchObj=regexObj.findall(text)
if matchObj:
    print('phone numbers found in text: '+str(matchObj))
else:
    print('no phone numbers found!')



text='Agent Somesh told Agent AP that Agent Soham knew Agent Baba was a double agent!'

regexObj=re.compile(r'Agent \w+')
print(regexObj.sub(r'CENSORED',text))

regexObj=re.compile(r'Agent (\w)\w*')
print(regexObj.sub(r'Agent \1****', text))


regexObj=re.compile(r'Agent AP.*')
print(regexObj.search(text).group())
input()
