from django.shortcuts import render

# Create your views here.
from doctor_management.models import Doctor
from doctor_management.serializers import DoctorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication,permissions

class DoctorListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]
    def get(self,request):
        qs = Doctor.objects.all()

        serializer_instance = DoctorSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class DoctorRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    
    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs = Doctor.objects.get(id=pk)

        serializer_instance = DoctorSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        doctor_object = Doctor.objects.get(id=pk)

        form_data = request.data

        serializer_instance = DoctorSerializer(data=form_data,instance=doctor_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        qs = Doctor.objects.get(id=pk).delete()

        return Response({"message":"deleted"})