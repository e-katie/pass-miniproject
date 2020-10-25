from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from . import passwd

def index(request):
    template = loader.get_template('mypasswd/index.html')
    return HttpResponse(template.render({}, request))

def generated(request):
	template = loader.get_template('mypasswd/generated.html')
	context = {
        'generated_passwd': passwd.generate(),
    }
	return HttpResponse(template.render(context, request))
