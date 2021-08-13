
data={0: {'username': 'admin', 'password': 'benjo234', 'role': 'Admin'}, 1: {'username': 'Kumar', 'password': 'Lvnbs:4', 'role': 'Customer'}, 2: {'username': 'Praveen', 'password': 'qsjodf', 'role': 'Customer'}}
for i in data:
     print(data[i],len(data),data[i]['username'])

inventry = {1:{'Item Name':'Dove','Category':'Conditioner','Price/unit':25,'Avaliable quantity':10},2:{'Item Name':'Pantene','Category':'Conditioner','Price/unit':30,'Avaliable quantity':10},3:{'Item Name':'Lux','Category':'Conditioner','Price/unit':25,'Avaliable quantity':10},4:{'Item Name':'Lux','Category':'Soap','Price/unit':15,'Avaliable quantity':10},5:{'Item Name':'Dove','Category':'Soap','Price/unit':30,'Avaliable quantity':10}}


product=dict()                



def hashing(password):
         lis=[]
         for i in range(0,len(password)):
                    lis.append(chr(ord(password[i])+1))
         return ''.join(lis)


def placeorders(id):
                   flag=0
                   print('Item Name   Category   Price  Avaliable quantity')
                   for i in inventry:
                                  prod=inventry[i]
                                  
                                  for j in prod:
                                      print(prod[j],end='  ')
                                  print('\n')
                   step=True
                   while step:
                               i=0
                            
                               productnum=int(input('Enter Product number: '))
                               qnty= int(input('Enter the quantity of prodct: '))
                               if qnty>(inventry[productnum]['Avaliable quantity']):
                                       print('Sorry we dont have enough stocks')
                                       flag=1

                               else:
                                    if(len(product)==0):
                                              product[id]={i:{'Item Name':inventry[productnum]['Item Name'],'quantity':qnty,'amount':qnty*inventry[productnum]['Price/unit']}}
                                              inventry[productnum]['Avaliable quantity']=inventry[productnum]['Avaliable quantity']-qnty

                                              u=int(input('If u wanna stop purchase press 2, u wanna do more press 1'))
                                              if u==2:
                                                     step=False
                                              else:
                                                  pass

                                    else :
                                         for i in product:
                                                 if i==id:
                                                        product[id][len(product[id])+1] = {'Item Name':inventry[productnum]['Item Name'],'quantity':qnty,'amount':qnty*inventry[productnum]['Price/unit']}
                                                        inventry[productnum]['Avaliable quantity']=inventry[productnum]['Avaliable quantity']-qnty
                                                        print(qnty,inventry[productnum]['Avaliable quantity'])
                                                        break
                                         u=int(input('If u wanna stop purchase press 2, u wanna do more press 1'))
                                         if u==2:
                                                     step=False
                                         else:
                                                  pass

                                         
                   if(flag==0):
                                           print('Product purchased by {} are as follow: '.format(data[id]['username']))
                                           print(product[id])
                               
                   
                  
def signup():
            print("Signup")
            name=input("Enter Your Name")
            password = hashing(input("Enter Your password"))
            if(name!='admin'):
                    role="Customer"
            else:
                  role="Admin"
            flag=1
            for i in data:
                  if(data[i]['username']==name):
                                       flag=0
            
            if(flag==0):
                       return "Username Already exist"

            else:
                    data[len(data)+1]={'username': name, 'password': password, 'role': role}
                    return "You have successfully registered"

                  

def login():
           print('Login Form')
           name=input("Enter Your Name")
           password = hashing(input("Enter Your password"))

           for i in data:
                  if(data[i]['username']==name and data[i]['password']==password):
                               return ["You successfully logged in",i]
            
           return "Invalid Username/password"

def viewhistory(num):
         print(product[num])
         sum=0
         for i in product[num]:
              sum+=product[num][i]['amount']

         print('Total amount is ',sum)

         

 
                                    

condition=True
while condition:           
                print('press 1 to signup \n press 2 to login \n press 3 to stop\n\n')
                i=int(input())
                if i ==1:
                                    sign=signup()
                                    print(sign)
                                    
                elif i==2:
                                    log=login()
                                    print(log[0])
                                    con=True
                                    while con:
                                                    print('press 1 to place orders \n 2 to view the order history \n 3 to logout\n\n')
                                                    i=int(input())
                                                    if i==1:
                                                           placeorders(log[1])

                                                    elif i==2:
                                                           viewhistory(log[1])

                                                    else:
                                                         con=False
                                                         print('Logout')
                                    
                                    
                                    
                
                else:
                      condition=False
                      
                
                         
             
                    
             
                
                    
             





