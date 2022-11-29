from pprint import pprint

from django.shortcuts import render

# Create your views here.

def indexPage(request):
	context = {}

	# for dict_row in request.__dict__ : pprint(f"request: {dict_row}")
	pprint(f"request: {request.path }")
	if request.method == 'GET'\
	and request.path == '/':
		return render(
		request=request,
		template_name='apps/index.html',
		context=context,
	)
