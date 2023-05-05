from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
   context = {
       'variable':"this is sent"
   }
   return render(request , 'index.html',context)
   #  return HttpResponse("this is home page")

def about(request):
    return render(request , 'about.html')
    #return HttpResponse("this is a about page")

def services(request):
    return render(request , 'services.html')
    #return HttpResponse("thisi is a services page")

def option1(request):
    return render(request , 'option1.html')
def option2(request):
    return render(request , 'option2.html')
def other_options(request):
    return render(request , 'other_options.html')
    
