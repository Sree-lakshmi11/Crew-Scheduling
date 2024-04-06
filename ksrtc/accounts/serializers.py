from rest_framework import serializers
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['username','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employee(
            username=validated_data['username'],
            # email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user