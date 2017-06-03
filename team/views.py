# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
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
        serializer = MembersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def team_detail(request, pk):
    """
    Retrieve, update or delete a team member.
    """
    try:
        members = Members.objects.get(pk=pk)
    except Members.DoesNotExist:
        return HttpResponse(status=404)

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