from django.shortcuts import render
from datetime import datetime
def home(request):
   
    d={'arif': 'shred',
       'da':[1,2,3,4],
       'current_date': datetime.now() ,
       'x':21,
       'a':['python','is','best']
       
    }
       
    return render(request,'index.html',{'data':d,})
