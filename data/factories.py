import factory
from factory.django import DjangoModelFactory

from .models import User

# Defining a factory
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("first_name")

# Using a factory with auto-generated data
u = UserFactory()
u.name # Kimberly
u.id # 51

# You can optionally pass in your own data
u = UserFactory(name="Alice")
u.name # Alice
u.id # 52