from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
   context = {
       'variable':"this is sent"
   }
   return render(request , 'index.html',context)
   #  return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is a about page")

def services(request):
    return HttpResponse("thisi is a services page")