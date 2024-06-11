# from database.connection import get_db_connection

# class Magazine:
#     def __init__(self, name, category):
#         self._id = None
#         self._name = name
#         self._category = category
#         self.save()

#     @property
#     def id(self):
#         return self._id
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#         self.update()

#     @property
#     def category(self):
#         return self._category
    
#     @category.setter
#     def category(self, new_category):
#         self._category = new_category
#         self.update()

#     def save(self):
#         with get_db_connection() as connection:
#             cursor = connection.cursor()
#             cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self._name, self._category))
#             self._id = cursor.lastrowid
#             connection.commit()

#     def update(self):
#         with get_db_connection() as connection:
#             cursor = connection.cursor()
#             cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self._name, self._category, self._id))
#             connection.commit()

#     def articles(self):
#         with get_db_connection() as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT * FROM articles
#                 WHERE magazine_id = ?
#             ''', (self._id,))
#             articles = cursor.fetchall()
#         return articles

#     def contributors(self):
#         with get_db_connection() as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT DISTINCT authors.* FROM authors
#                 JOIN articles ON authors.id = articles.author_id
#                 WHERE articles.magazine_id = ?
#             ''', (self._id,))
#             contributors = cursor.fetchall()
#         return contributors

#     def article_titles(self):
#         with get_db_connection() as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT title FROM articles
#                 WHERE magazine_id = ?
#             ''', (self._id,))
#             titles = [row['title'] for row in cursor.fetchall()]
#         return titles if titles else None

#     def contributing_authors(self):
#         with get_db_connection() as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT authors.*, COUNT(articles.id) as article_count FROM authors
#                 JOIN articles ON authors.id = articles.author_id
#                 WHERE articles.magazine_id = ?
#                 GROUP BY authors.id
#                 HAVING article_count > 2
#             ''', (self._id,))
#             authors = cursor.fetchall()
#         return authors if authors else None

#     def __repr__(self):
#         return f'<Magazine {self.name}>'

from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self._id = id
        self._name = name
        self._category = category
        if id is None:
            self.save()

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        self.update()

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        self._category = new_category
        self.update()

    def save(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self._name, self._category))
            self._id = cursor.lastrowid
            connection.commit()

    def update(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self._name, self._category, self._id))
            connection.commit()

    def articles(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM articles
                WHERE magazine_id = ?
            ''', (self._id,))
            articles = cursor.fetchall()
        return articles

    def contributors(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT DISTINCT authors.* FROM authors
                JOIN articles ON authors.id = articles.author_id
                WHERE articles.magazine_id = ?
            ''', (self._id,))
            contributors = cursor.fetchall()
        return contributors

    def article_titles(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT title FROM articles
                WHERE magazine_id = ?
            ''', (self._id,))
            titles = [row['title'] for row in cursor.fetchall()]
        return titles if titles else None

    def contributing_authors(self):
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT authors.*, COUNT(articles.id) as article_count FROM authors
                JOIN articles ON authors.id = articles.author_id
                WHERE articles.magazine_id = ?
                GROUP BY authors.id
                HAVING article_count > 2
            ''', (self._id,))
            authors = cursor.fetchall()
        return authors if authors else None

    def __repr__(self):
        return f'<Magazine {self.name}>'