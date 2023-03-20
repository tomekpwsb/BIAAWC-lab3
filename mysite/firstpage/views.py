from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import MyForm



def index(request):
    template = loader.get_template('firstpage/index.html')
    return HttpResponse(template.render({},request))


def hello(request):
    if(request.method == 'POST'):
        form = MyForm(request.POST)
    else:
        form = MyForm(initial={'my_field': ''})

    return render(request, 'firstpage/hello.html', {'form': form})




