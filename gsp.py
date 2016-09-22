import sys

def frequentSet_k(tables,minSup,candidate,size):
    result={}
    frequentSeq={}
    print "============"
    cnt=0
    for line in tables:
        for key in candidate:

            num = line.count(key)
            if num == 0 :
                continue
            if frequentSeq.has_key(key):
                frequentSeq[key]+=num
            else:
                frequentSeq[key]=num
        cnt+=1
        if cnt%200==0:
            print cnt        

    for key in frequentSeq:
        if frequentSeq[key]>=minSup*size:
                result[key]=frequentSeq[key]
    return result
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
#threadLock = threading.Lock()
threads = []
tables=[]

def main():
    with open('hw2.txt','r') as f:
        for line in f:
            tables.append(line)
    frequentSeqs=[]
    frequentSeq1,size=frequentSet_1(tables,0.01)
    frequentSeqs.append(frequentSeq1)
    k=0
    while len(frequentSeqs[k])>0:
        candidate = genCandidate(frequentSeqs,k+1)
        frequentSeqs.append(frequentSet_k(tables,0.01,candidate,size))
        k+=1
        print frequentSeqs[k]

if __name__ == '__main__':
    main()