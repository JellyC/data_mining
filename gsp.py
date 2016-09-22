import sys
import threading
class myThread (threading.Thread):
    def __init__(self,tables,minSup,candidate,size,result,begin,end):
        threading.Thread.__init__(self)
        self.tables = tables
        self.minSup = minSup
        self.candidate = candidate
        self.size = size
        self.result = result
        self.begin=begin
        self.end=end
    def run(self):
        # Get lock to synchronize threads
        threadLock.acquire()
        frequentSet_k(self.tables,self.minSup,self.candidate,self.size,self.result,self.begin,self.end)
        # Free lock to release next thread
        threadLock.release()
def frequentSet_k(tables,minSup,candidate,size,result,begin,end):
        frequentSeq={}
        print "============"
        print len(tables),len(candidate)
        for line in tables:
            for i in range(begin,end):
                key = list(candidate)[i]

                num = line.count(key)
                if num == 0 :
                    continue
                if frequentSeq.has_key(key):
                    frequentSeq[key]+=num
                else:
                    frequentSeq[key]=num
        print frequentSeq

        for key in frequentSeq:
            if frequentSeq[key]>=minSup*size:
                result.append(key)
def frequentSet_1(tables,minSup):
    frequentSeq = {}
    result1={}
    for line in tables:
        for key in line.split():
            if frequentSeq.has_key(key):
                frequentSeq[key]+=1
            else:
                frequentSeq[key]=0
    size = len(frequentSeq)
    print size
    for key in frequentSeq:
        if frequentSeq[key]>=minSup*size:
            result1[key]=frequentSeq[key]
    return result1,size
def genCandidate(frequentSeqs,K):
    candidate = set()

    for fkey in frequentSeqs[K-1]:
        for skey in frequentSeqs[0]:
            elem = fkey+' '+skey
            candidate.add(elem)
    return candidate
threadLock = threading.Lock()
threads = []
tables=[]

#def main():
with open('hw2.txt','r') as f:
    for line in f:
        tables.append(line)
frequentSeqs=[]
frequentSeq1,size=frequentSet_1(tables,0.01)
frequentSeqs.append(frequentSeq1)
candidate = genCandidate(frequentSeqs,1)
results=[]
minSup=0.01
unit = 300
for i in range(0,len(candidate)/unit):
    result=[]
    results.append(result)
    length = len(candidate)
    begin = min(length-length%unit,i*unit)
    end = min(length,(i+1)*unit)
    print begin,end,len(candidate)
    thread = myThread(tables,0.01,candidate,size,result,begin,end)
    threads.append(thread)
    thread.start()
for t in threads:
    t.join()
   # frequentSeqs.append(frequentSet_k(tables,0.01,candidate,size))
print (results)

#if __name__ == '__main__':
#    main()