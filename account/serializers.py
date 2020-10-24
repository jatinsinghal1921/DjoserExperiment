from rest_framework.serializers import ModelSerializer
from account.models import customUser


class customUserSerializer(ModelSerializer):

    class Meta:
        model = customUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'birthday', 'password')
