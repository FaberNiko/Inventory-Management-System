from django.test import TestCase
from .models import Material, Variant
from django.core.exceptions import ValidationError

class MaterialModelTest(TestCase):

    def test_create_material(self):
        material = Material.objects.create(
            name = "Test material",
            unit = "m2"

        )

        self.assertEqual(material.name, "Test material")
        self.assertEqual(material.unit, "m2")

class VariantValidationTest(TestCase):
    def setUp(self):
        self.material = Material.objects.create(
            name="Test material",
            unit="m2"
        )

    def test_variant_cannot_have_negative_quantity(self):
        variant = Variant(
            material=self.material,
            size="36",
            color="black",
            quantity=-10
        )

        with self.assertRaises(ValidationError):
            variant.full_clean()

def test_variant_size_must_be_unique_per_material(self):
    Variant.objects.create(
        material=self.material,
        size="36",
        color="black",
        quantity=10
    )

    duplicate = Variant(
        material=self.material,
        size="36",
        color="black",
        quantity=5
    )

    with self.assertRaises(Exception):
        duplicate.save()

