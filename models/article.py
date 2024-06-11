from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine



class Article:
    def __init__(self, id, title, content, author_id , magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._save()

    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return Author.get(self._author_id)
    
    @property
    def magazine(self):
        return Magazine.get(self._magazine_id)
    
    def _save(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES(?,?,?,?)', (self._title, self._content, self._author_id, self._magazine_id))
        self._id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()

    def __repr__(self):
        return f'<Article {self.title}>'