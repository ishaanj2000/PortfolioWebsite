from django.shortcuts import render
from django.contrib import  messages



def index(request):

    return render(request, 'base/index.html')
        

        
    

    
