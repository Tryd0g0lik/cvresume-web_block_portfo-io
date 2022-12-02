from pprint import pprint
from django.shortcuts import render
# Create your views here.
from apps.experience import Experience_db
import re

from apps.models import PagesModel


def indexPage(request):
	context = Experience_db().db_pulication()

	if request.method == 'GET'\
	and request.path == '/':
		return render(
		request=request,
		template_name='apps/index.html',
		context=context,
	)


def innerPage(request):
	req = str(request.path).strip('/')
	response_content =  PagesModel.objects.get(url_path=req)

	context = {'titleH2': response_content.title,
	           'preview_text': response_content.preview_text,
	           'descriptions': response_content.description,
	           'date_create': response_content.date_created,
	           'date_change': response_content.date_change,
	           'url_path': response_content.url_path,
	           }

	return render(
		request=request,
		template_name='apps/page.html',
		context=context,
	)
