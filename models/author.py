from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        if not isinstance(id, int):
            raise ValueError("id must be an integer")
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non_empty string")
        
        self._id = id
        self._name = name
        self._save()

    def _save(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO authors (id, name) VALUES(?, ?)', (self._id, self._name))
        connection.commit()
        cursor.close()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

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

    # def __repr__(self):
    #     return f'<Author {self.name}>'