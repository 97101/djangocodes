from django.shortcuts import render
import datetime

def home (request):
    d={'autor':'rahim', 'age':15,'lst':['python','is','best'],
       'birthday':datetime.datetime.now() , 'courses':[
        {
            'id':1,
            'name':'python',

        },
        {
            'id':2,
            'name':'react',
            
        },
        {
            'id':3,
            'name':'django',
            
        },
    ]}
    return render(request,'home.html',d)
