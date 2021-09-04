from django.shortcuts import render

#from http import HttpResponse
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello world")
    my_dict  = {'insert_me': "This is the point"}
    return render(request, 'first_app/index.html', context=my_dict)
# Create your views here.
def help(request):
    return render(request,'first_app/help.html')
