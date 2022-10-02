from http.client import HTTPResponse
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
from alpinemuseum.models import user_detail
from django import forms

# Create your views here.


def home(request):
    return render(request,'mitmachen.html')

def Saved(request):
    return render(request,'saved.html')

class AddDetail(forms.ModelForm):
    class Meta:
        model = user_detail
        fields = ('description','surname','first_name','year_of_birth')




class UserDetail(CreateView):
    form_class = AddDetail
    template_name = "rohit.html"
    # success_url = "/saved/"

    def get_success_url(self):
        return reverse('saved')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




# class user_detail_view(View):
#     model = user_detail
#     template_name = 'mitmachen.html'
#
#     def get(self,request, *args, **kwargs):
#         return render(request, self.template_name, model )
#
#     def post(self, request, *args, **kwargs):
#         return render(request, 'mitmachen.html', model)
