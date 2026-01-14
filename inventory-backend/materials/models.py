from django.db import models

class Material(models.Model):
    name = models.CharField(max_length = 100)
    unit = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Variant(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name = "variants"
    )
    size = models.CharField(max_length = 10)
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.material.name} - {self.size}"
# Create your models here.
