from django.http import HttpResponse
def homepage(request):
    return HttpResponse("this is home page")
def contact(request):
    return HttpResponse("this is contact page")
def shred(request):
    return HttpResponse("this is shred coder page")