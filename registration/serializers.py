from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    # new_password = serializers.CharField(required=True)


    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'is_staff']

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
