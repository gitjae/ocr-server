from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import *

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        # Not None
        if user :
            login(request, user)
            return redirect('/')
            #return Response({'login' : 'success'})
        else :
            return Response(status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return redirect('/')

class Users(APIView):
    def post(self, request):
        serializer = UserJoinSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            user.set_password(user.password)
            user.save()
            return redirect('/login')
            #return Response(serializer.data)
        return Response(serializer.errors)

class UsersByAdmin(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if not request.user.is_staff:
            raise PermissionDenied
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, request, username):
        try:
            user = User.objects.get(username=username)
            if not user == request.user:
                raise PermissionDenied
            return user
        except User.DoesNotExist:
            return NotFound

    def get(self, request, username):
        user = self.get_object(request, username)

        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        user = self.get_object(request, username)
        if not user == request.user:
            raise PermissionDenied

        serializer = UserJoinSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()

            if 'password' in request.data :
                user.set_password(user.password)
                user.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, username):
        user = self.get_object(request, username)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)
