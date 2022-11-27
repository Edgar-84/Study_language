import os
from time import time
from openpyxl import load_workbook

from slugify import slugify

from django.core.exceptions import ValidationError


def create_slug(user: str, title: str, category: str):
    unix_timestamp = str(time()).split('.')
    slug = '-'.join((slugify(str(user)),
                     slugify(str(title)),
                     slugify(str(category)),
                     slugify(unix_timestamp[0] + unix_timestamp[1])))

    return slug


def validate_file_extension(value, max_size: int = 5242880):
    """
    Checking type and size file
    """
    type_file = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx', ]
    file_size = value._file.size

    if not type_file.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

    if file_size > max_size:
        raise ValidationError(f'Please keep filesize under {max_size}. Current filesize {file_size}')


def get_maximum_rows(sheet_object):
    rows = 0
    for max_row, row in enumerate(sheet_object, 1):
        if not all(col.value is None for col in row):
            rows += 1
    return rows


def get_user_wordlist(path: str) -> list:
    """
    Take path from list in 'xlsx' format and
    get words, translate, descriptions
    """

    book = load_workbook(path, read_only=True)
    sheet = book.active
    max_rows = get_maximum_rows(sheet_object=sheet)
    list_words = []

    for row in range(1, max_rows + 1):
        try:
            word = sheet[row][0].value
            translate = sheet[row][1].value
        except Exception as ex:   # TODO add logger
            print(f'Mistake with word - translate: {ex}')
            continue
        try:
            description = sheet[row][2].value
        except Exception as ex:
            print(f'Mistake with description: {ex}')
            description = ''

        if word is None or translate is None:
            continue
        else:
            info = {
                'word': str(word),
                'translate': str(translate),
                'description': str(description)}

            list_words.append(info)

    return list_words
