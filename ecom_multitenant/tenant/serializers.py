from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data.get('role') == "administrator":
            validated_data['is_staff'] = True
        user = User.objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        # Custom password validation
        validate_password(value)  # This will raise a ValidationError if the password doesn't meet the default Django password validation rules
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")
        if not any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in value):
            raise serializers.ValidationError("Password must contain at least one special character")
        return value