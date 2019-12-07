from django.shortcuts import render
from .models import Complain


# Create your views here.
def home(request):
    return render(request, 'loginuser.html')
