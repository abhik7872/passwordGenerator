from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import JSONParser
from password.models import Passwords
import logging
import random
import string

logger = logging.getLogger(__name__)

# Create your views here.
class GeneratePassword(APIView):
    logger.warning('test')
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        user_id = request.user.id

        length = request.data.get("length")
        label = str(request.data.get("label"))

        logger.info(f"Storing password for user: {user_id}, label: {label}")

        if length > 16 or length < 6:
            return Response({"error": "Length should be between 6 to 16"}, status=status.HTTP_400_BAD_REQUEST)

        password = get_random_string(length=length, allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$%^&*()")

        passwordStore = Passwords.objects.create(user_id=user_id, label=label, password=password)
        passwordStore.save()

        return Response({"password": password, "id": user_id, "label": label})