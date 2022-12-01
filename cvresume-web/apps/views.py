from pprint import pprint

from django.shortcuts import render

# Create your views here.
from apps.experience import Experience_db


def indexPage(request):
	context = Experience_db().db_pulication()

	if request.method == 'GET'\
	and request.path == '/':
		return render(
		request=request,
		template_name='apps/index.html',
		context=context,
	)
