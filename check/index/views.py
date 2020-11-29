from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View

# Create your views here.


class IndexView(View):
    '''トップページを表示'''

    def get(self, request):
        template_name = 'check/index.html'
        return render(request, template_name)
