from rest_framework import serializers
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # user = Employee(
        #     username=validated_data['username'],
        #     email=validated_data['email']
        # )
        user = Employee.objects.create_user(**validated_data)
        return user