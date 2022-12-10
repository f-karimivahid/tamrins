def counter(str,num):
    c = str.split()
    count=0
    for i in c:
         if(len(i)==num):
             count+=1
             print(i)
    return count   


tex=str(input("jomle vared konid :"))
number=int(input("adad vared konid :"))
print(counter(tex,number))
