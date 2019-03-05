from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from main.models import BanksNew
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
@csrf_exempt
def index(request):
	print("ajax call in server")
	ifsc = request.POST.get('ifsc','')
	bank_name = request.POST.get('bank_name','')
	city = request.POST.get('city','')
	if city == '' and ifsc == '' and bank_name == '':
		results = BanksNew.objects.filter(ifsc__contains=ifsc,city__contains=city,bank_name__contains=bank_name)[:10]
	else:
		results = BanksNew.objects.filter(ifsc__contains=ifsc,city__contains=city,bank_name__contains=bank_name)
	print(len(results))
	# for i in results:
	# 	print(i.city)
	queryset = serializers.serialize('json',results)
	return HttpResponse(queryset,content_type='application/json')


def ifsc(request,pk):
	print(pk)
	results = []
	try:
		results = BanksNew.objects.filter(ifsc__contains=pk)
		print(results)
	except:
		return HttpResponse("error")
	queryset = serializers.serialize('json',results)
	return HttpResponse(queryset,content_type='application/json')

def details(request,pk,dk):
	results = []
	ans = pk.split('-')
	pk = ""
	for l in ans:
		pk = pk+l
		pk = pk + " "
	pk = pk[:-1]

	res = dk.split('-')
	dk = ""
	for l in res:
		dk = dk+l
		dk = dk + " "
	dk = dk[:-1]
	print(dk)
	try:
		results = BanksNew.objects.filter(city__contains=dk,bank_name__contains=pk)
		print(results)
	except:
		return HttpResponse("error")
	
	queryset = serializers.serialize('json',results)
	return HttpResponse(queryset,content_type='application/json')