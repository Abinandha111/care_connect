
from rest_framework import serializers
from doctor_management.models import Doctor

class DoctorSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    specialization = serializers.CharField()

    contact = serializers.CharField()

    email = serializers.EmailField() 

    experience = serializers.IntegerField()

    fee = serializers.DecimalField(max_digits=10,decimal_places=2)

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)


    def update(self, instance, validated_data):

        for attribute,values in validated_data.items():

            setattr(instance,attribute,values)

        return instance