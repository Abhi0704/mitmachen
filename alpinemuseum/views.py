from http.client import HTTPResponse
from pyexpat import model
from django.shortcuts import render
from django.views import View
from alpinemuseum.models import user_detail

# Create your views here.


def home(request):
    return render(request,'mitmachen.html')

class user_detail_view(View):
    model = user_detail
    template_name = 'mitmachen.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, model )

    def post(self, request, *args, **kwargs):
        return render(request, 'mitmachen.html', model)    
