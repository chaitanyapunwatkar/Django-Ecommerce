from rest_framework import serializers
from .models import Outlet, Product
from django.core.exceptions import ValidationError

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

class OutletSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Outlet
        fields = '__all__'
    
    def validate(self, attrs):
        if len(attrs.get('contact')) != 10:
            raise ValidationError("Contact number must be 10 digits")
        return super().validate(attrs)
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        