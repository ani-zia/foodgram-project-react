import csv

from django.db.utils import IntegrityError


def print_error(error, row, print_error):
    if print_error:
        print('Error:', error.args, '\nRowID:', row.get('id'))


def create_models(file_path, model, print_error):
    with open(file_path, encoding='utf-8', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        total_rows = 0
        ready_rows = 0
        for row in csv_reader:
            total_rows += 1
            try:
                model.objects.get_or_create(**row)
                ready_rows += 1
            except IntegrityError as error:
                print_error(error, row, print_error)
            except ValueError as error:
                print_error(error, row, print_error)
        errors = total_rows - ready_rows
        print('model:', model.__name__, 'rows:', ready_rows, 'errors:', errors)
