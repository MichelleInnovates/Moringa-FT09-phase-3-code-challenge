# from database.setup import create_tables
# from database.connection import get_db_connection
# from models.article import Article
# from models.author import Author
# from models.magazine import Magazine

# def main():
#     while True:
#         print("\n1. Add new entry")
#         print("2. Quit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             # Initialize the database and create tables
#             create_tables()

#             # Collect user input
#             author_name = input("Enter author's name: ").strip()
#             magazine_name = input("Enter magazine name: ").strip()
#             magazine_category = input("Enter magazine category: ").strip()
#             article_title = input("Enter article title: ").strip()
#             article_content = input("Enter article content: ").strip()

#             if not author_name:
#                 print("Author name cannot be empty. Please try again.")
#                 continue
#             if not magazine_name:
#                 print("Magazine name cannot be empty. Please try again.")
#                 continue
#             if not magazine_category:
#                 print("Magazine category cannot be empty. Please try again.")
#                 continue
#             if not article_title:
#                 print("Article title cannot be empty. Please try again.")
#                 continue
#             if not article_content:
#                 print("Article content cannot be empty. Please try again.")
#                 continue

#             # Connect to the database
#             conn = get_db_connection()
#             cursor = conn.cursor()

#             try:
#                 # Create an author
#                 cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
#                 author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

#                 # Create a magazine
#                 cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
#                 magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

#                 # Create an article
#                 cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
#                             (article_title, article_content, author_id, magazine_id))

#                 conn.commit()

#                 # Query the database for inserted records. 
#                 # The following fetch functionality should probably be in their respective models

#                 cursor.execute('SELECT * FROM magazines')
#                 magazines = cursor.fetchall()

#                 cursor.execute('SELECT * FROM authors')
#                 authors = cursor.fetchall()

#                 cursor.execute('SELECT * FROM articles')
#                 articles = cursor.fetchall()

#             finally:
#                 conn.close()

#             # Display results
#             print("\nMagazines:")
#             for magazine in magazines:
#                 print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

#             print("\nAuthors:")
#             for author in authors:
#                 try:
#                     print(Author(author["id"], author["name"]))
#                 except ValueError as e:
#                     print(f"Error creating author object: {e}")

#             print("\nArticles:")
#             for article in articles:
#                 print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

#         elif choice == "2":
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()


################################################################

from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")


    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    

if __name__ == "__main__":
    main()