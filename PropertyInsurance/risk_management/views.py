# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from risk_management.models import Risks,RisksType,RisksSubType
from risk_management.serializers import RiskSerializer,RiskTypeSerializer,RiskSubTypeSerializer

from rest_framework import status
from rest_framework.views import APIView,View
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RiskslistView(View):
    """    List all Risks , or create a new Risk."""
    def get(self, request, format=None):
        return render(request,'index.html')

class RiskslistView1(View):
    """ List all Risks , or create a new Risk. """
    def get(self,request,format=None):
	
	context = { 
		'ntitle':'Risk Management List',
	        'name': [1,2,3,4],
	    }
	return render(request,'risk_list.html',context)


class Riskslist(APIView):
    """ List all Risks , or create a new Risk."""
    def get(self, request, format=None):
        risk = Risks.objects.all()
        serializer = RiskSerializer(risk, many=True)
	return Response(serializer.data)
  
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RisksDetail(APIView):
    """ Retrieve, update or delete a Risk."""
    def get_object(self, pk):
	    try:
	        risk = Risks.objects.get(pk=pk)
	    except Risks.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
    	risk = self.get_object(pk)
        serializer = RiskSerializer(risk)
	return Response(serializer.data)

    def put(self, request, pk, format=None):
    	risk = self.get_object(pk)
        serializer = RiskSerializer(risk, data=request.data)
        if serializer.is_valid():
            serializer.save()
	    return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):    
	risk = self.get_object(pk)
        risk.delete()
	return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def risk_list_type(request,format=None):
    """
    List all code Risks Type , or create a new Risk Type.
    """
    if request.method == 'GET':
        risk = RisksType.objects.all()
        serializer = RiskTypeSerializer(risk, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RiskTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def risk_list_sub_type(request,format=None):
    """
    List all code Risk-Sub Type , or create a new Risk-Sub Type.
    """
    if request.method == 'GET':
        risk = RisksSubType.objects.all()
        serializer = RiskSubTypeSerializer(risk, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RiskSubTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


