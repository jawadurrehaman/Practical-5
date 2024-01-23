fh = open('practical5.txt','w')
a=int(input('Enter year: ')) 
if(a%4==0): 
    fh.write('It is a leap year') 
else: 
    fh.write('Not a leap year') 
fh.close()