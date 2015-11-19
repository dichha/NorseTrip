from django.http import HttpResponse

from django.shortcuts import render


from .models import Lodge
# Create your views here.

def lodge_list(request):
    #lodge = Lodge.objects.all()
    return render(request, 'tripadvise/base.html')

 #return render(request, 'tripadvise/lodge_list.html', {'lodge' : lodge})