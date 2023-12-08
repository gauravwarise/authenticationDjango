from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.permissions import AllowAny
from core.models import *
from rest_framework.response import Response
from django.http import JsonResponse


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
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)


    def user_register(self, request):
        print("user registration done!!!!")
        return Response({'message': 'User registration successful'})

