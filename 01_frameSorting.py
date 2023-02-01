#frame sort 
import random

class Frame:
    def __init__(self, seqNo, data = None):
        self.seqNo = seqNo;
        self.data = data;

def bubbleSort(frames):
    for i in range(len(frames)):
        flag = 0
        for j in range(len(frames)-i-1):
            if(frames[j].seqNo > frames[j+1].seqNo):
                temp = frames[j]
                frames[j] = frames[j+1]
                frames[j+1] = temp
                flag = 1
        if(flag == 0):
            break

n = int(input("Enter no of frames : "))

seqList = []
for _ in range(n):
    r = random.randint(1, n*100)
    while r in seqList:
        r = random.randint(1, n*100)
    seqList.append(Frame(r))

# frames = []
# for i in range(n):
#     ch = random.choice(seqList)
#     frames.append(Frame(ch))
#     seqList.remove(ch)

for i in range(n):
    seqList[i].data = input(f"Enter data of frame with seqNo {seqList[i].seqNo} : ")

bubbleSort(seqList)

print("Sorted Frames")
for i in range(n):
    print(f"{seqList[i].seqNo} : {seqList[i].data}")