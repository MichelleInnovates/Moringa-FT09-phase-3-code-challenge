from database.connection import get_db_connection

class Author:
    def __init__(self, name, id=None):
        self._id = id
        self._name = self.validate_name(name)
        self._save()

    def _save(self):
        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the author name already exists
        cursor.execute('SELECT id FROM authors WHERE name = ?', (self._name,))
        existing_author = cursor.fetchone()
        if existing_author:
            self._id = existing_author['id']
        else:
            cursor.execute('INSERT INTO authors (name) VALUES(?)', (self._name,))
            connection.commit()
            self._id = cursor.lastrowid

        cursor.close()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        return name

    def articles(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM articles
            WHERE author_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        cursor.close()
        connection.close()
        return articles

    def magazines(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        cursor.close()
        connection.close()
        return magazines
