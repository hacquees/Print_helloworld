#This is General 
class stack:
    def __init__(self,n) -> None:
        self.n=n
        self.l =[0]*(self.n+1)
        self.t=-1
    def isFull(self):
        return self.t==self.n-1
        
    def isEmpty(self):
        return  self.t==-1

    def peak(self):
        if self.isEmpty():
            print("UnderFlow")
        else:
            print(self.l[self.t])

    def push(self,ele):
        if self.isFull():   
            print("OverFlow")
            
        else:
            self.t+=1
            self.l[self.t]=ele
    def pop(self):
        if  self.isEmpty():
            print("UnderFlow")
            
        else:
            print(self.l[self.t])
            self.t-=1

s=stack(10)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop()
s.peak()