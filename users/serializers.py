
from rest_framework import serializers
from users.models import User


class UserSerialiazer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['id', 'name', 'email',
                  'password', 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}
