from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_otp, send_otp_phone
from .models import Employee

class LoginWithOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number', '')
        try:
            user = Employee.objects.get(phone_number=phone_number)
        except Employee.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp_phone(phone_number, otp)

        return Response({'message': 'OTP has been sent to your phone number.'}, status=status.HTTP_200_OK)


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

class ValidateOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number', '')
        otp = request.data.get('otp', '')

        try:
            user = Employee.objects.get(phone_number=phone_number)
        except Employee.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if user.otp == otp:
            user.otp = None  # Reset the OTP field after successful validation
            user.save()

            # Authenticate the user and create or get an authentication token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Invalid OTP
            raise ValidationError('Invalid OTP')

