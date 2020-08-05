import sys

class Fibonacci():
    
    def __init__(self,):
        pass       
    
    def getUserInput(self,):
        n= int(input("how many values do you want to print? "))
        if(n<=0):
            try:
                raise InvalidInputError
            except InvalidInputError:
                print('Invalid Input provided!!!')
        else:
            return n             
    
    def printFibonacci(self,):
        n=self.getUserInput()
        temp_list=[]
        for i in range(0,n):  
            temp_list.append(str(self.processFib(i)))
        return temp_list
    
    def processFib(self,x):        
        if x<=0 or x==1:
            return 1
        else:
            return (self.processFib(x-1)+self.processFib(x-2))

        
class InvalidInputError(Exception):
    pass



class PrintSpiral():
    
    def __init__(self,):
        self.x=0
        self.y=0
        pass   
    
    def callFibonacci(self,):
        fibo=Fibonacci()
        temp_list=fibo.printFibonacci()
        flag="r"
        
        for i in temp_list:
            #print("i: "+i,"flag: ", flag)
            i=int(i)            
            if(flag=="r"):
                self.printRight(i)
                flag="d"
            
            elif(flag=="d"):
                self.printDown(i)
                flag="l"
            
            elif(flag=="l"):
                self.printLeft(i)
                flag="u"
            
            elif(flag=="u"):
                self.printUp(i)
                flag="r"    
            
    def printRight(self,input):
        #print("into R")
        for i in range(self.x, self.x+input):
            for j in range(0,self.y+1):
                self.printScreen(self.x, self.y,"#")
                self.x=self.x+input
                print("self.x: "+str(self.x)+" self.y: "+str(self.y))
            
    
    def printDown(self,input):
        #print("into D")
        for i in range(self.x, self.x+1):
            #y should start from y+1 since the first value should print one level below of the previous line
            for j in range(self.y+1,self.y+1+input):
                self.printScreen(self.x, self.y,"#\n")
                self.y=self.y+1+input
                print("self.x: "+str(self.x)+" self.y: "+str(self.y))
            
    def printLeft(self,input):
        #print("into L")
        for i in range(self.x,0,-1):
            for j in range(0,self.y+1):
                self.printScreen(self.x, self.y,"#")
                self.x=self.x-input
                print("self.x: "+str(self.x)+" self.y: "+str(self.y))
            
    def printUp(self,input):
        #print("into U")
        for i in range(self.x, self.x+1):
            for j in range(self.y,self.y-input,-1):
                self.printScreen(self.x, self.y, "#\n")
                self.y=self.y-input
                print("self.x: "+str(self.x)+" self.y: "+str(self.y))
                
    def printScreen(self, x, y, text):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()
            
if __name__=="__main__":
    pf=PrintSpiral()
    pf1=PrintSpiral()
    pf.callFibonacci()
    #print(str(pf.x)+""+str(pf.y))
    #print(str(pf1.x)+""+str(pf1.y))
