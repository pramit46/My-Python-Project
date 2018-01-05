'''
This is a sample code for stack implementation
'''

class Stack:
    #created a Dataset first
    dataset=[]
    
    #this has been added to address the issue related to self object being passed, although still in vain
    def __init__(self,):
        #Do Nothing Yet
        print()
        
                
       
    #Added @staticmethod in order to ignore the self obejct reference
    #alternatively, you could also add self as the first arguement 
    #in the method signature (e.g. pushdata(self,value=None))
    #@staticmethod
    def pushdata(self,value=None): 
        dataset=self.dataset
        if(value!=None):
            dataset.append(value)
            print("Entered "+str(value)+" in the list")
        else:
            print("The data entered is: NULL")

        print("Current values in the list: "+str(dataset)+"\n")
        
        
    #Added @staticmethod in order to ignore the 'self' obejct reference, 
    #alternatively, you could also add self as the first arguement in the method signature (e.g. popdata(self))
    #@staticmethod
    def popdata(self,):
        dataset=self.dataset
        if(len(dataset)>0):
            value=str(dataset.pop())            
            print("Returned value: "+str(value))
        else:
            value="There is no data present in the list"

        print("Current values in the list: "+str(dataset)+"\n")
        return value
