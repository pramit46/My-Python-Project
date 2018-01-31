'''
Binary Tree Implementation
'''

class Node:
    def __init__(self,value):
        self.r=None
        self.l=None
        self.v=value
        
        
class Tree:       
    def __init__(self):
        self.root=None
        
    def printval(self,node):
        print("Data in this node is:"+str(node.v))
    
    def traverse(self,root):
        if(root != None):
            print("into root")
            self.printval(root)
        if(root.l!=None):
            print("into root.l")
            self.traverse(root.l)
        if(root.r!=None):
            print("into root.r")
            self.traverse(root.r)
            
    def insert(self,new_value,node):
        if(node==None):
            node=Node(new_value)
            print("Node created with the value: "+str(node.v))
        else:
            current_val=node.v
            print("new_value: "+str(new_value)+" current_val: "+str(current_val))
            if(new_value<=current_val):
                print("new val is less than current, so going left")
                if(node.l==None):                    
                    node.l=Node(new_value)
                    print("created new left node and put the value")
                else:
                    print("going one step left")
                    self.insert(new_value,node.l)
            elif(new_value>current_val):
                print("new val is greater than current, so going right")  
                if(node.r==None):
                    node.r=Node(new_value)
                    print("created new right node and put the value")
                else:  
                    print("going one step right")
                    self.insert(new_value,node.r)
        return node
    
    def getroot(self,user_value):
            if(self.root==None):
                return self.insert(user_value,self.root)
            else:
                return self.root
    
    def delete(self):
        self.root=None
        
    
if(__name__=="__main__"):
    tree=None
    tree=Tree()
    root=None
    list=[10,12,5,30,'exit']
    for i in list:
        print("\nthe value is: "+str(i))
        #user_value=input("Please enter the value:")
        user_value=i        
        if(user_value == "exit"):
            tree.traverse(root)
            break
        else:        
            if(root==None):
                print('root is empty')
                root=tree.getroot(user_value)
            else:
                print("now the root is not empty")
                node=tree.insert(user_value,root)
    tree.delete()
