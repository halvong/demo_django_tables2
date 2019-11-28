from django.core.management.base import BaseCommand
from demo_app.models import Publisher, Source, RevenueRecord
import csv, os.path

class Command(BaseCommand):

    publishers = ['micha', 'mark', 'melanie', 'logan']
    sources = ['yahoo', 'google']

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def insert_source(self):
        Source.objects.bulk_create([Source(name="yahoo"), Source(name="google")])

    def insert_publisher(self):
        Publisher.objects.bulk_create([Publisher(name="micha"), Publisher(name="mark"), Publisher(name="melanie"), Publisher(name="logan")])

    def insert_revenuerecord(self, ffile):
        with open(ffile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1 #skips header
                else:
                    print(f'Inserting data: {", ".join(row)}')
                    RevenueRecord.objects.create(date=row[0], publisher_id=row[1], source_id=row[2], clicks=row[3], revenue=row[4])
                    line_count += 1

    def handle(self, *args, **options):
        print ("Inserting sources")
        self.insert_source()
        print ("Inserting publishers")
        self.insert_publisher()
        print ("Inserting revenues")

        if os.path.isfile(options['file']):
            self.insert_revenuerecord(options['file'])
        else:
            print ("File does not exists.")
