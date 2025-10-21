import os
from pathlib import Path


def project_root_dir():
    """
    Возвращает корневую директорию проекта.
    Функция находится в корне, поэтому просто возвращает свою директорию.
    """
    return Path(__file__).parent
