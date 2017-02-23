from django.db import models
from django.utils.encoding import smart_unicode


class Ship(models.Model):
    name = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=5)
    issue = models.IntegerField(default=0)

    def __unicode__(self):
        return smart_unicode(self.name)


class Plate(models.Model):
    name = models.CharField(max_length=6)
    edition = models.CharField(max_length=3)
    ship = models.ForeignKey(Ship, default="")

    def __unicode__(self):
        return smart_unicode(self.name)

    def delete(self, *args, **kwargs):
        ship = Ship.objects.filter(id=self.ship.id)
        issues = ship[0].issue
        if issues == 0:
            issues = 1
        ship = Ship.objects.filter(id=self.ship.id).update(issue=issues-1)







class Item(models.Model):
    plate = models.ForeignKey(Plate, default="")
    name = models.IntegerField(default=0)
    order_number = models.IntegerField(default=0)
    status = models.CharField(max_length=200)


    def __unicode__(self):
        return smart_unicode(self.name)




