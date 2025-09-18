class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.sage=c
    def display(self):
        print("student no:",self.sno)
        print("student name:",self.sname)
        print("student age:",self.sage)
        
x=int(input("Enter roll no:"))
y=input("Enter name:")
z=int(input("Enter age:"))      
         

obj=stud(x,y,z)

