from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import authentication,permissions

from reservation.serializers import AppointmentSerializer
from reservation.models import Appointment

from datetime import datetime,timedelta


# Create your views here.

class AppointmentCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):

        form_data = request.data

        serializer_instance = AppointmentSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            doctor = cleaned_data.get("doctor")

            appointment_date = cleaned_data.get("appointment_date")

            appointment_object = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date
            )

            if not appointment_object.exists():

                token = 1
                appointment_time = datetime.strptime("09:00","%H:%M").time()

            else:
                last_appointment_object = appointment_object.order_by("-token").first()

                if last_appointment_object.token >= 36:

                    return Response({"message":"slot not available after 5pm"})
                
                token = last_appointment_object.token + 1

                appointment_time = (datetime.combine(
                    last_appointment_object.appointment_date,
                    last_appointment_object.appointment_time) + timedelta(minutes=15)).time()

        
            serializer_instance.save(token=token,appointment_time=appointment_time)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)



class AppointmentRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,reuqest,pk=None):

        qs = Appointment.objects.get(id=pk)

        serializer_instance = AppointmentSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        book_object = Appointment.objects.get(id=pk)

        form_data = request.data

        serialized_instance = AppointmentSerializer(data=form_data,instance=book_object)

        if serialized_instance.is_valid():

            serialized_instance.save()

            return Response(serialized_instance.data)

        else:

            return Response(serialized_instance.errors)


    def delete(self,request,pk=None):

        qs = Appointment.objects.get(id=pk).delete()

        return Response({"message":"deleted"})



class AppointmentSummaryView(APIView):

    def post(self,request):

        form_data = request.data

        doctor = form_data.get("doctor")

        appointment_date = form_data.get("appointment_date")

        appointments = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date)

        serializer_instance = AppointmentSerializer(appointments,many=True)

        return Response(serializer_instance.data)