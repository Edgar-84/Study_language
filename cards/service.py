import os
from django.core.exceptions import ValidationError


def validate_file_extension(value, max_size: int = 5242880):
    """
    Checking type and size file
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx', ]
    file_size = value._file.size

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

    if file_size > max_size:
        raise ValidationError(f'Please keep filesize under {max_size}. Current filesize {file_size}')
