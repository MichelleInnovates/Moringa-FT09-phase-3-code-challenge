import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.connection import get_db_connection
class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article("Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly","Entertainment")
        self.assertEqual(magazine.name, "Tech Weekly")
    def setUp(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_author_creation(self):
        # Test creating a new author
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertIsNotNone(author.id)

        # Test that the author was saved to the database
        self.cursor.execute("SELECT * FROM authors WHERE name = 'John Doe'")
        db_author = self.cursor.fetchone()
        self.assertIsNotNone(db_author)
        self.assertEqual(db_author['name'], "John Doe")

    def test_author_existence(self):
        # Test that the author exists in the database
        author = Author("Jane Doe")
        self.cursor.execute("SELECT * FROM authors WHERE name = 'Jane Doe'")
        db_author = self.cursor.fetchone()
        self.assertIsNotNone(db_author)
        self.assertEqual(db_author['name'], "Jane Doe")

        # Test that the same author object is returned when created again
        author2 = Author("Jane Doe")
        self.assertEqual(author.id, author2.id)

    def test_author_validation(self):
        # Test that an exception is raised for an empty name
        with self.assertRaises(ValueError):
            Author("")

        # Test that an exception is raised for a non-string name
        with self.assertRaises(ValueError):
            Author(123)

    def test_author_articles(self):
        # Test that the author's articles are retrieved correctly
        author = Author("John Doe")
        articles = author.articles()
        self.assertIsInstance(articles, list)

    def test_author_magazines(self):
        # Test that the author's magazines are retrieved correctly
        author = Author("Jane Doe")
        magazines = author.magazines()
        self.assertIsInstance(magazines, list)
        

    
if __name__ == "__main__":
    unittest.main()