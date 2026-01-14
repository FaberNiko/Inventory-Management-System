from django.db import models
from django.core.exceptions import ValidationError


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
    color = models.CharField(max_length = 20, default="unknown")
    size = models.CharField(max_length = 10)
    quantity = models.IntegerField(default = 0)

    class Meta:
        unique_together = ("material", "size", "color")

    def clean(self):
        if self.quantity < 0:
            raise ValidationError("Quantity cannot be negative")

    def __str__(self):
        return f"{self.material.name}"
# Create your models here.
