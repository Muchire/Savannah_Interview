from rest_framework import serializers
from .models import Customer,Order

class OrderSerializer( serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = '__all__'

class CustomerSerializer( serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'