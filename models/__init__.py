#!/usr/bin/python3

""" Initialized the package magic method for models directory """

from models.engine.file_storage import FileStorage
"""
Storage instance
"""
storage = FileStorage()
storage.reload()
