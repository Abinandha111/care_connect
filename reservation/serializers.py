from rest_framework import serializers
from reservation.models import Appointment

from doctor_management.models import Doctor

from datetime import datetime

class AppointmentSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    phone = serializers.CharField()

    doctor = serializers.IntegerField()

    appointment_date = serializers.DateField()

    appointment_time = serializers.TimeField(read_only=True)

    token = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)


    def update(self, instance, validated_data):

        for attribute,value in validated_data.items():

            setattr(instance,attribute,value)

        return instance

    def validate(self, validate_data):

        appointment_date = validate_data.get("appointment_date")

        today = datetime.now().date()
        
        if appointment_date < today:
        
            raise serializers.ValidationError("invalid date")

        doctor_id = validate_data.get("doctor")

        if not Doctor.objects.filter(id=doctor_id).exists():

            raise serializers.ValidationError("doctor not exist")

        return validate_data