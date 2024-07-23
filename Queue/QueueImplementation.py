def Enqueue(ele):
    queue.append(ele)
        
def Dequeue():
    if len(queue)==0:
        print("Queue is Empty")
    else:
        return(queue.pop(0))
        
def Peak():
    if len(queue)==0:
        return("Queue is Empty")
    else:
        return queue[0]

queue=[]
Enqueue(10)
Enqueue(20)
Enqueue(30)
Enqueue(40)
print("Dequeued Element: ",Dequeue())
print("Peak Element: ",Peak())
