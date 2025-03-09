from rest_framework import serializers
from .models import UserModel, BookModel
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def validate_username(self, value):
        """Ensure username only contains letters, numbers, and underscores, and is unique if changed."""
        instance = getattr(self, 'instance', None)  # Get the current instance safely

        # Skip uniqueness check if the username hasn't changed (for updates)
        if instance and instance.username == value:
            return value  

        # Check if username contains only allowed characters
        if not re.match(r'^\w+$', value):
            raise serializers.ValidationError("Username can only contain letters, numbers, and underscores.")

        # Check for uniqueness only when instance exists (for updates) or in general (for new users)
        user_exists = UserModel.objects.filter(username=value)
        if instance:
            user_exists = user_exists.exclude(id=instance.id)  # Avoid checking the same user

        if user_exists.exists():
            raise serializers.ValidationError("This username is already taken. Please choose a different one.")

        return value

    def validate_email(self, value):
        """Ensure email contains '@' and ends with '.com'"""
        if '@' not in value or not value.endswith('.com'):
            raise serializers.ValidationError("Invalid email format. Must contain '@' and end with '.com'.")
        return value
    
    def validate_password(self, value):
        """Ensure password meets security requirements"""
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError("Password must contain at least one special character (!@#$%^&* etc.).")
        
        return value

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =  BookModel
        fields= "__all__"