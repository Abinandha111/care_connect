from django.shortcuts import render

from accounts.serializers import AdminSerializer,PatientSerializer
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response


class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serialized_instance = AdminSerializer(data=form_data)

        if serialized_instance.is_valid():

            serialized_instance.save()

            return Response(serialized_instance.data)


        else:

            return Response(serialized_instance.errors)


class UserCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = PatientSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


        

