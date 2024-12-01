from django.urls import reverse
from rest_framework import status  
from rest_framework.test import APITestCase,APIClient
from .models import Customer, Order
from unittest.mock import patch

class CustomerViewSetTest(APITestCase):
    
    def setUp(self):
        self.customer_data = {'name': 'Vivian Muchire', 'code': 'C123', 'phone_number': '254723123456'}
        self.customer_url = reverse('customer-list')  # Ensure your URLs are correctly named

    def test_create_customer(self):
        response = self.client.post(self.customer_url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Vivian Muchire')

class OrderViewSetTest(APITestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(name='Vivian Muchire', code='C123', phone_number='254723123456')
        self.order_data = {
            'customer': self.customer.id,
            'item': 'Laptop',
            'amount': 1200.50,
            'time': '2024-12-01T08:30:00Z'
        }
        self.order_url = reverse('order-list')  # Ensure your URLs are correctly named

    @patch('shoe.send_sms.SMSHandler.send_message')
    def test_create_order_and_send_sms(self, mock_send_message):
        mock_send_message.return_value = {'status': 'Success', 'message': 'Message sent'}

        response = self.client.post(self.order_url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().item, 'Laptop')
        mock_send_message.assert_called_once_with(
            ['254723123456'],
            'Thank you, Vivian Muchire, for your order of Laptop worth 1200.50. Your order is confirmed!'
        )

class OrderViewSetAdditionalTests(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='Vivian Muchire', code='C123', phone_number='254723123456')
        self.order_data = {
            'customer': self.customer.id,
            'item': 'Laptop',
            'amount': 1200.50,
        }
        self.order_url = reverse('order-list')  

    def test_create_order_without_customer(self):
        order_data = {
            'item': 'Laptop',
            'amount': 1200.50,
        }
        response = self.client.post(self.order_url, order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_order_list(self):
        Order.objects.create(customer=self.customer, item='Laptop', amount=1200.50)
        response = self.client.get(self.order_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_order_detail(self):
        order = Order.objects.create(customer=self.customer, item='Laptop', amount=1200.50)
        order_detail_url = reverse('order-detail', args=[order.id]) 
        response = self.client.get(order_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item'], 'Laptop')
