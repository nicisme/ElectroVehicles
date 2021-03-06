from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class Cart(models.Model):
    cart_id = models.CharField(max_length=10, null=True)
    serial_number = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=200, null=True)
    cartLocation = models.ForeignKey(Location, blank=True, default=1)
    running_hours = models.IntegerField(blank=True, null=True)
    #cart_pic_one = models.ImageField(blank=True, null=True)
    #cart_pic_two = models.ImageField(blank=True, null=True)
    #scart_pic_three = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.cart_id)

class Service(models.Model):
    cart = models.ForeignKey(Cart, blank=True, default=1)
    technician = models.TextField(blank=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    battery = models.CharField(max_length=4, null=True)
    tyres = models.CharField(max_length=4, null=True)
    upholstery = models.CharField(max_length=4, null=True)
    serviced = models.BooleanField(blank=False, null=False, default=False)
    breakdown = models.BooleanField(blank=False, null=False, default=False)
    accident = models.BooleanField(blank=False, null=False, default=False)
    battery_percentage = models.IntegerField(null=True)
    problem = models.TextField(blank=True)
    repaired_replaced = models.TextField(blank=True)
    concerns = models.TextField(blank=True)
    parts_ordered = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.cart.cart_id)

class Spares(models.Model):
    part_number = models.TextField(blank=True)
    part_name = models.TextField(blank=True)
    part_description = models.TextField(blank=True)
    cart_used = models.ForeignKey(Cart, blank=True, default=None)


    def __str__(self):
        return str(self.part_number + " : " + self.part_name)



