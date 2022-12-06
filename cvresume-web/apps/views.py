from pprint import pprint
from django.shortcuts import render
# Create your views here.
from apps.experience import Experience_db
import re

from apps.models import PagesModel, MenuModel


def indexPage(request):

	_menu_porfolio_incidePage = Experience_db().db_pulication()

	_response_menu = Experience_db().main_menu()
	_data_OnPage = _response_menu['page']

	context = {"menu_porfolio_incidePage": _menu_porfolio_incidePage,
	            "data_OnPage": _data_OnPage,
	            }

	if request.method == 'GET'\
	and request.path == '/':
		pprint(f"context: {context}")
		return render(
		request=request,
		template_name='apps/index.html',
		context=context,
	)


def innerPage(request):
	req = str(request.path).strip('/')
	response_content =  PagesModel.objects.get(url_path=req)

	_response_menu = Experience_db().main_menu()
	_data_OnPage = _response_menu['page']


	context = {'titleH2': response_content.title,
	           'preview_text': response_content.preview_text,
	           'descriptions': response_content.description,
	           'date_create': response_content.date_created,
	           'date_change': response_content.date_change,
	           'url_path': response_content.url_path,
	           "data_OnPage": _data_OnPage,
	           }

	return render(
		request=request,
		template_name='apps/page.html',
		context=context,
	)

# def mainMenu(request):

# 	return render(request=request,
# 	              template_name='apps/',
# 	              context=response_menu)