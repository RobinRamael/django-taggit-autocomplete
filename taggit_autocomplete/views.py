from django.http import HttpResponse
from django.core import serializers
from django.utils.datastructures import MultiValueDictKeyError


from taggit.models import Tag


import json

def list_tags(request):

	try:
		tags = Tag.objects.filter(name__istartswith=request.GET['term']).values_list('name', flat=True)
	except MultiValueDictKeyError:
		tags = []

	tag_dicts = [dict([('label', tag)]) for tag in tags]

	return HttpResponse(json.dumps(tag_dicts), mimetype='application/json')
