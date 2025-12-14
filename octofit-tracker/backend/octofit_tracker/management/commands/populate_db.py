from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            Leaderboard.objects.all().delete()
            Activity.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create users
            users = [
                User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
                User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel),
                User.objects.create(email='batman@dc.com', name='Batman', team=dc),
                User.objects.create(email='superman@dc.com', name='Superman', team=dc),
            ]

            # Create workouts
            w1 = Workout.objects.create(name='Super Strength', description='Strength workout', suggested_for='DC')
            w2 = Workout.objects.create(name='Tech Endurance', description='Endurance workout', suggested_for='Marvel')

            # Create activities
            Activity.objects.create(user=users[0], type='Run', duration=30, date='2025-12-01')
            Activity.objects.create(user=users[1], type='Swim', duration=45, date='2025-12-02')
            Activity.objects.create(user=users[2], type='Fly', duration=60, date='2025-12-03')
            Activity.objects.create(user=users[3], type='Lift', duration=50, date='2025-12-04')

            # Create leaderboard
            Leaderboard.objects.create(user=users[0], score=100)
            Leaderboard.objects.create(user=users[1], score=90)
            Leaderboard.objects.create(user=users[2], score=110)
            Leaderboard.objects.create(user=users[3], score=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
