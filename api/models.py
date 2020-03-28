from django.db import models


class Product(models.Model):
    name = models.CharField(),
    price = models.FloatField(),
    description = models.TextField(),
    count = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
            'description': self.description
        }


class Category(models.Model):
    name = models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
