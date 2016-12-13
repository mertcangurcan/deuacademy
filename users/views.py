from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
#from .models import Courses
from IPython import embed

# Create your views here.


# /users/
class Users(View):
    def get(self,request):
        return render(request, 'users/create.html',)
    def post(self, request):
        params = request.POST
        paramters = [params['password'],params['name'],params['phone_no'],params['email']]
        embed()