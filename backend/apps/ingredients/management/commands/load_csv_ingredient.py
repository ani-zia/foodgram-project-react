import csv
import os

from apps.ingredients.models import Ingredient
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'load ingredients from csv'

    def add_arguments(self, parser):
        parser.add_argument(
            'filename', default='ingredients.csv', nargs='?', type=str
        )

    def handle(self, *args, **options):
        try:
            with open(
                os.path.join(
                    DATA_ROOT, options['filename']), 'r', encoding='utf-8'
            ) as csv_file:
                data = csv.reader(csv_file)
                for ingredient in data:
                    try:
                        Ingredient.objects.create(
                            name=ingredient[0],
                            measurement_unit=ingredient[1],
                        )
                    except IntegrityError:
                        print(
                            f'{ingredient["name"]} '
                            f'{ingredient["measurement_unit"]} '
                            f'already in table'
                        )
        except FileNotFoundError:
            raise CommandError('file not found')
