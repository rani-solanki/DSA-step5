class Students:
    
    stream = 'Rani Solanki'                 
    def __init__(self,name,collegeName,subject):
        self.name = name           
        self.collegeName = collegeName
        self.subject = subject     

a = Students('Savnam', "Gov.pg college morena",'pcm')
b = Students('salu', "gov.girls college morena mp","pcb")

print(a.stream)   
print(a.name)   
print(a.collegeName)    
print(a.subject)    

print("********************* ")

Students.stream = 'ece'
print(b.stream) 
print(b.name)
print(b.collegeName)
print(b.subject)
