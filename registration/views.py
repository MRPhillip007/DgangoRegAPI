from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


class GetUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Serializer valid", status=status.HTTP_201_CREATED)
        # TODO make user error validation. For exam.pl: "user with that email already exists"
        return Response("Error occurred! Check your credentials!")


class UserByID(APIView):
    permission_classes = [IsAuthenticated]

    def _get_user_by_id(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except ObjectDoesNotExist as error:
            return HttpResponse(error, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self._get_user_by_id(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        updated_user = self._get_user_by_id(pk=pk)
        serializer = UserSerializer(updated_user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response("resource updated successfully", status=status.HTTP_200_OK)

        return Response("Error! check your fields")

    def delete(self, request, pk):
        user = self._get_user_by_id(pk=pk)
        user.delete()
        return Response("User deleted successfully! ", status=status.HTTP_204_NO_CONTENT)