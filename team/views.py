# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from team.models import Members

from team.serializers import MembersSerializer

@csrf_exempt
def team_list(request):
    """
    List all team members, or create a new snippet.
    """
    if request.method == 'GET':
        members = Members.objects.all()
        serializer = MembersSerializer(members, many=True)
        return JsonResponse(serializer.data,safe = False)

    elif request.method == 'POST':
    	data = JSONParser().parse(request)
    	flag =0 
    	"""
    	Checking if data is present or not
    	"""
    	if not(data):
    		return JsonResponse(get_message(flag),status=400)
    	keys=['first_name','last_name','phone','email','role']
    	
    	for key in keys:
    		"""
    		Validating if the keys used are correct or not
    		"""
    		if data.has_key(key):
    			flag=2
    			if data[key]:
    	 			flag=1
    	 			break
    	if flag == 1:
    		serializer = MembersSerializer(data=data)
        	if serializer.is_valid():
        		serializer.save()
           		return JsonResponse(serializer.data, status=201)
        	return JsonResponse(serializer.errors, status=400)
        elif flag == 2:
    		return JsonResponse(get_message(flag),status=400)
        else:
         	return JsonResponse(get_message(3),status=400)

@csrf_exempt
def team_detail(request, pk):
    """
    Retrieve, update or delete a team member.
    """
    try:
        members = Members.objects.get(pk=pk)
    except Members.DoesNotExist:
    	return JsonResponse(get_message(4),status=404)

    if request.method == 'GET':
        serializer = MembersSerializer(members)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
    	data = JSONParser().parse(request)
        serializer = MembersSerializer(members, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        members.delete()
        return HttpResponse(status=204)

def get_message(flag):
	message =  ["Please enter a value","Success","Key with empty value","Correct key not used","Not a correct"]
	return {'error':message[flag]}