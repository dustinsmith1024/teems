from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = “Describe the Command Here”

    def handle_noargs(self, **options):
        print 'suppp'
