from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers
# Create your views here.
# from .models import User
User = get_user_model()


class UserViewSet(ModelViewSet):

    http_method_names = ['get', 'put',]
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)

    # @action(detail=False, methods=['GET', 'PUT',], permission_classes=[IsAuthenticated])
    # def me(self, request):
    #     user = User.objects.get(id=request.user.id)
    #     if request.method == 'GET':
    #         serializer = serializers.UserSerializer(user)
    #         return Response(serializer.data)

    #     elif request.method == 'PUT':
    #         serializer = serializers.UserSerializer(
    #             user, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
