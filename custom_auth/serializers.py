from rest_framework import serializers
from .models import AuthModel

class AuthSerializers(serializers.ModelSerializer):
    class Meta:
        model= AuthModel
        fields="__all__"
        extra_kwargs= {"password": {"write_only":True}}

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =AuthModel
        fields = "__all__"

    def create(self, validated_data): # assuming the sent details are validated
        usr = AuthModel.objects.create(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        usr.savePassword(validated_data["password"])
        usr.save()
        return usr
    
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password= serializers.CharField()

