from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)


class Client(models.Model):
    cpf = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True)
    phone_number = models.CharField(max_length=20)
    accompanied = models.BooleanField(default=False)


class Reserve(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_persons = models.IntegerField()
    checkin_datetime = models.DateTimeField()
    checkout_datetime = models.DateTimeField()
    diary_price = models.FloatField()


class Room(models.Model):
    number = models.IntegerField()
    description = models.CharField(max_length=200)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
