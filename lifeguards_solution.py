import os

class Slots:
    def __init__(self,a,b,c):
        self.time = a
        self.isStart = b
        self.index = c

def computetimings(timings,aloneTime,totalTime):
    visited = set()
    cur = 0
    prev = 0

    for slot in timings:
        cur = slot.time
        if  visited and len(visited) == 1:
            for v in visited:
                aloneTime[v] += cur - prev
        if len(visited) > 0:
            totalTime += cur -prev
        
        if slot.isStart == 1:
            visited.add(slot.index)
        else:
            visited.remove(slot.index)
                                
        prev = cur
    
    maxtimecovered = totalTime - min(aloneTime)
    #print("aloneTime",aloneTime)
    #print("maxtimecovered",maxtimecovered)
    return maxtimecovered

def main():
    #list all files
    files  = os.listdir('input')

    #read file and convert to list
    for file in files:
        print(file)

        if '.in' not in file:
            continue
        filenum = file.split('.')[0]

        filepath = os.path.join('input', file)   

        with open(filepath) as f:
            line = f.readline()
            n = int(line)
            timings = [0]*2*n 
            aloneTime = [0]*n
            totalTime = 0

            for i in range(n):
                line = f.readline()
                if not line:
                    break

                l = line.strip()
                l = l.split(' ')

                timings[2*i] =  Slots(int(l[0]), 1,i)
                timings[2*i+1] = Slots(int(l[1]), 0,i)

        timings.sort(key = lambda x:x.time)
        res = computetimings(timings,aloneTime,totalTime)
        out_filepath = os.path.join('output', filenum+'.out') 
        with open(out_filepath, 'w') as f:
            f.write(str(res))

if __name__ == "__main__":
    main()