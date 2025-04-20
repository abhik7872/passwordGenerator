from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from authentication.models import User
from django.contrib.auth import authenticate


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Missing credentials"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        print(f"Retrieved user: {user.username}, provided password: {user.password}")
        print(f"Password matches: {user.check_password(password)}")

        if not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        })
    
class Register(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(email=email):
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        return Response({"messege": "user created", "username": user.username, "email": user.email})
    
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        userlist = []

        for user in users:
            userlist.append({"id": user.id, "username": user.username, "email": user.email, "password": user.password})
 
        return Response(userlist)