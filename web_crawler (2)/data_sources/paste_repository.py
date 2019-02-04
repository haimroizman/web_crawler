import data_sources.onion_database


class PasteRepository(data_sources.onion_database.OnionDatabase):
    def __init__(self):
        super().__init__()

    def ensure_table(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS pastes ('
            'id INTEGER PRIMARY KEY,'
            'title TEXT,'
            'author TEXT,'
            'date DATE,'
            'content TEXT)')

    def insert_paste(self, paste):
        print('Inserting paste...')
        paste.print_paste()

        self.cursor.execute(
            'INSERT INTO pastes (title, author, date, content) VALUES (?,?,?,?)',
            (paste.title, paste.author, paste.publish_date, paste.content))
