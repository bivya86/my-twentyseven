from django.shortcuts import render

# Create your views here.
import datetime

def filters(request):
    t=datetime.datetime.now
    d={'data':'hai FILTers how r You','t':t,'c':2}
    return render(request,'filters.html',d)