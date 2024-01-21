import sqlite3
from faker import Faker


def generate_fake_names():
    fake = Faker()
    names = [fake.name().split() for i in range(100)]
    names = [name for name in names if len(name) == 2]
    return names


def create_table(connection):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT
    )
    '''
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()


def insert_data(connection, names):
    insert_query = 'INSERT INTO people(name, surname) VALUES(?, ?)'
    cursor = connection.cursor()
    for name in names:
        cursor.execute(insert_query, name)
    connection.commit()


def retrieve_data(connection):
    select_query = 'SELECT * FROM people LIMIT 10'
    cursor = connection.cursor()
    for row in cursor.execute(select_query):
        print(row)


def search_name(connection, name_to_search):
    search_query = 'SELECT * FROM people WHERE name = ?'
    cursor = connection.cursor()
    cursor.execute(search_query, (name_to_search,))
    result = cursor.fetchall()
    if result:
        print(f"Search results for {name_to_search}: {result}")
    else:
        print(f"{name_to_search} not found in the database.")


def main():
    connection = sqlite3.connect('sample.db')

    # Create table if not exists
    create_table(connection)

    # Generate fake names and insert into the database
    names = generate_fake_names()
    insert_data(connection, names)

    # Retrieve and print data
    retrieve_data(connection)

    # Search for a name in the database
    name_to_search = input("Enter a name to search: ")
    search_name(connection, name_to_search)

    # Close the database connection
    connection.close()


if __name__ == "__main__":
    main()
