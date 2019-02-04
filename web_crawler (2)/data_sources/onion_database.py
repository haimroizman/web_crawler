import os
import sqlite3

import utility.config
import utility.fs_utils


class OnionDatabase(object):
    def __init__(self):
        onion_database_dir_path = os.path.dirname(utility.config.onion_database_path)
        utility.fs_utils.ensure_directory(onion_database_dir_path)

        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.connection = self.get_connection(utility.config.onion_database_path)
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def get_connection(database_path):
        return sqlite3.connect(database_path)

    def close(self):
        try:
            self.connection.commit()
        finally:
            self.cursor.close()
            self.connection.close()
