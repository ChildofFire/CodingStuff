import pdfkit,os, threading


os.makedirs(r'C:\Users\Assassin123\Documents\ArtificialNeuralNets',exist_ok=True)

os.chdir(r'C:\Users\Assassin123\Documents\ArtificialNeuralNets')


def downloader(start, end):
    for i in range(start,end+1):
        pdfkit.from_url('http://neuralnetworksanddeeplearning.com/chap%s.html'\
                        %str(i), 'ANN%s.pdf'%str(i))

threadList=[]
for i in range(0,5,2):
    thread=threading.Thread(target=downloader, args=[i+1,i+2])
    thread.start()
    threadList.append(thread)

for i in threadList:
    i.join()

print('download complete!')
    
