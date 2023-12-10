from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.permissions import AllowAny
from core.models import *
from rest_framework.response import Response
from django.http import JsonResponse
from core.serializers import AuthUserSerializer


# Create your views here.


class IndexView(View):
    template_name = 'preferences/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegistrationView(View):
    def get(self, request):
        return render(request, 'account/register.html')
    # def post(self, request):
    #     return 


class AuthView(APIView):
    """
        For managing user login,  user registration and user logout
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        action = request.data.get('action')
        if action == 'register':
            return self.user_register(request)
        elif action == 'login':
            return self.user_login(request)
        elif action == 'logout':
            return self.user_logout(request)
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)
        


    def user_register(self, request):
        print(request.data)
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registration successful'})
        else:
            return Response({'message': 'User registration failed'})

    

    def user_login(self, request):
        return Response({'message': 'User login successful'})
    
    def user_logout(self, request):
        return Response({'message': 'User logout successful'})
    

