from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html',{'name':'Deepak Saini'})
def add(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])
    choice=int(request.POST['num3'])
    # s=int(val1)+int(val2)
    if choice==1:
        result=a+b
        re1="addition"
    elif(choice==2):
        result=a-b
        re1='Subtraction'
    elif(choice==3):
        result=a/b
        re1='Divide'
    elif(choice==4):
        result=a*b
        re1='Multiply'
    elif(choice==5):
        result=a**b
        re1='Power'
    else:
        result='Invalid choice'                    
    return render(request,'result.html',{'result':round(result,2),'choice':re1})  
def image(request):
    k=23
    return render(request,'image.html',{'result':k})      
