#!/usr/bin/python3
"""Creates a storage object.

If 'HBNB_TYPE_STORAGE' is 'db', creates a DBStorage engine.
Else, creates a FileStorage engine.
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
