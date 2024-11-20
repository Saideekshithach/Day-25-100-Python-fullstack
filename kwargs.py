#kwargs(**)->keyword variable length arguments
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],
   "names":["phani","bhavan","gowtham"],
   "status":["P","A","P"]}
details(**d)'''

'''
def Data(**a):
    print(a)
    print(type(a))
    for i in a.keys():
    #for i in a:
        print(i)#It will return only keys
    #for i in a.values():
        print(i)
    for i in a:
        print(a[i])#only values will return
    #for i in a:
        #print(i,a[i])
    for i in a.items():
        print(i)#both keys and values will return
    
Data()
b={"names":["jayachandra","jajendra","rajesh"],
   "places":["vja","hyd","vzg"]}
Data(**b)

'''

def final(*a,**b):
    d=2
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    for i in a:
        if type(i) in (int,float):
             d=d+i
             print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,4,3,5,4.2,5.3,"python",3+8j,True,False)
final(*data)
details={"names":["pooja","bhanu","divya"],
         "places":["vja","hyd","bng"]}
final(*data,**details)
final(**details)
        
        
    
