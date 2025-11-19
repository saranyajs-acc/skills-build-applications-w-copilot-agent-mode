from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        iron_man = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        cap = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
        thor = User.objects.create(name='Thor', email='thor@marvel.com', team='marvel')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
        wonder_woman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='dc')

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, calories=300, date='2025-11-19')
        Activity.objects.create(user='Batman', type='cycle', duration=45, calories=400, date='2025-11-18')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=500, rank=1)
        Leaderboard.objects.create(team='dc', points=450, rank=2)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
