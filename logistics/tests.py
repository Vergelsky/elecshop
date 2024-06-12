from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from logistics.models import SupplyChainParticipant, Product


# Create your tests here.
class SupplierTestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='TestProduct',
                                              model='TestModel',
                                              date='2024-06-01')
        self.test_supplier = SupplyChainParticipant.objects.create(name="TestName",
                                                                   country="TestCountry",
                                                                   city="TestCity",
                                                                   street="TestStreet",
                                                                   building="TestBuild",
                                                                   debt="1234.12",
                                                                   is_factory=True,
                                                                   product=self.product)
        self.user = User.objects.create(username='TestUser',
                                        is_staff=True)
        self.user.set_password('testPassword')
        self.client.force_authenticate(user=self.user)
        self.data = {'name': "TestName2",
                     'country': "TestCountry2",
                     'city': "TestCity2",
                     'street': "TestStreet2",
                     'building': "TestBuild2",
                     'debt': "1234.12",
                     'is_factory': True,
                     'product': 1}

    def test_create_supplier(self):
        """Тестируем создание поставщика"""
        self.client.force_authenticate(user=self.user)

        response = self.client.post(reverse('logistics:logistics-list'),
                                    data=self.data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_read_documents(self):
        """ Тестируем чтение списка поставщиков """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('logistics:logistics-list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_read_document(self):
        """ Тестируем чтение одного поставщика """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('logistics:logistics-list'), args=[self.test_supplier.pk])
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_document(self):
        """ Тестируем обновление поставщика"""

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('logistics:logistics-detail', args=[self.test_supplier.pk]),
                                     data={'city': 'TestCity3'})
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_document(self):
        """ Тестируем удаление поставщика """

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('logistics:logistics-detail',
                                              args=[self.test_supplier.pk]))
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
