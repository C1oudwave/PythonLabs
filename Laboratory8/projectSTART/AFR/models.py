from django.db import models

class Orendary(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    firm_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # использовать маску ввода для телефона

    def __str__(self):
        return self.firm_name


class Primischennya(models.Model):
    room_number = models.CharField(max_length=20)
    area = models.FloatField()
    rent_cost_per_sqm = models.FloatField()
    floor = models.IntegerField()
    phone_in_room = models.BooleanField()
    decoration_choices = [
        ('ordinary', 'Звичайне'),
        ('improved', 'Поліпшене'),
        ('euro', 'Євро'),
    ]
    decoration = models.CharField(max_length=10, choices=decoration_choices)

    def __str__(self):
        return self.room_number


class Orenda(models.Model):
    contract_number = models.CharField(max_length=20)
    start_date = models.DateField()
    duration_days = models.IntegerField()
    purpose_choices = [
        ('office', 'Офіс'),
        ('kiosk', 'Кіоск'),
        ('warehouse', 'Склад'),
    ]
    purpose = models.CharField(max_length=10, choices=purpose_choices)
    orendary = models.ForeignKey(Orendary, on_delete=models.CASCADE)
    primischennya = models.ForeignKey(Primischennya, on_delete=models.CASCADE)