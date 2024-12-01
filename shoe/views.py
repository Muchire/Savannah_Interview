from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from shoe.send_sms import SMSHandler
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class= OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()  
        customer = order.customer

        if customer.phone_number: 
            sms_handler = SMSHandler()
            message = f"Thank you, {customer.name}, for your order of {order.item} worth {order.amount}. Your order is confirmed!"
            sms_handler.send_message([customer.phone_number], message)
