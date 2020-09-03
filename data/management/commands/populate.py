# from django.core.management.base import BaseCommand
# import factory
# import factory.django
# from ...models import User_data


# class UserFactory(factory.django.DjangoModelFactory):  
#     class Meta:
#         model = User_data

#     #id = factory.Faker('id')
#     real_name = factory.Faker('name')
#     tz = factory.Faker('city')
#     #activity_periods = factory.Faker('')


# class Command(BaseCommand):
#     help = 'Populate the database.'

#     def add_arguments(self, parser):
#         parser.add_argument('--users',
#             default=200,
#             type=int,
#             help='The number of users to create.')

#     def handle(self, *args, **options):
#         for _ in range(options['users']):
#             UserFactory.create()
import random
from django.db import transaction
from django.core.management.base import BaseCommand
from forum.models import User, Thread, Club, Comment
from forum.factories import (
    UserFactory,
    ThreadFactory,
    ClubFactory,
    CommentFactory
)

NUM_USERS = 50
NUM_CLUBS = 10
NUM_THREADS = 12
COMMENTS_PER_THREAD = 25
USERS_PER_CLUB = 8

class Command(BaseCommand):
    help = "Generates test data"

    # @transaction.atomic
    # def handle(self, *args, **kwargs):
    #     self.stdout.write("Deleting old data...")
    #     models = [User, Thread, Comment, Club]
    #     for m in models:
    #         m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            people.append(person)

        # Add some users to clubs
        for _ in range(NUM_CLUBS):
            club = ClubFactory()
            members = random.choices(
                people,
                k=USERS_PER_CLUB
            )
            club.user.add(*members)

        # Create all the threads
        for _ in range(NUM_THREADS):
            creator = random.choice(people)
            thread = ThreadFactory(creator=creator)
            # Create comments for each thread
            for _ in range(COMMENTS_PER_THREAD):
                commentor = random.choice(people)
                CommentFactory(
                    user=commentor,
                    thread=thread
                )
