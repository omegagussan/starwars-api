import json
import os.path
import psycopg2

path = "./api/all.json"
port = 5432

with open("./credentials/postgres") as credentials:
    content = credentials.readlines()
content = [x.strip() for x in content]


def drop_if_present():
    drop_if_present = "DROP TABLE IF EXISTS star_wars;"
    try:
        conn = psycopg2.connect(host=content[0], port=port, database=content[1], user=content[2], password=content[3])
        cur = conn.cursor()
        print("dropping table 'star wars'")
        cur.execute(drop_if_present)
        cur.close()
        conn.commit()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1
    finally:
        if conn is not None:
            conn.close()


def insert(object):
    insert_sql = "INSERT INTO star_wars VALUES (%s);"
    try:
        conn = psycopg2.connect(host=content[0], port=port, database=content[1], user=content[2], password=content[3])
        cur = conn.cursor()
        cur.execute(insert_sql)
        print("insert successful")
        cur.close()
        conn.commit()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1
    finally:
        if conn is not None:
            conn.close()


def create_table():
    create_sql = """
    CREATE TABLE star_wars (
            id bigserial PRIMARY KEY,
            _name text NOT NULL,
            height float,
            mass integer,
            gender text, 
            homeworld text,
            wiki text,
            image text,
            born integer,
            bornLocation text,
            died integer,
            diedLocation text,
            species text,
            hairColor text,
            eyeColor text,
            skinColor text,
            cybernetics text,
            affiliations text[],
            masters text[],
            apprentices text[],
            formerAffiliations text[]
            );
    """
    try:
        conn = psycopg2.connect(host=content[0], port=port, database=content[1], user=content[2], password=content[3])
        cur = conn.cursor()
        cur.execute(create_sql)
        print("table 'star wars' created")
        cur.close()
        conn.commit()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1
    finally:
        if conn is not None:
            conn.close()


if create_table() == -1:
    drop_if_present()
    assert create_table() == 0

if os.path.isfile(path):
    print("found file: " + path)

with open(path) as json_file:
    json_data = json.load(json_file)
    for items in json_data:
        items_tuple = tuple(items.items())
        print(len(items_tuple))
        insert(items_tuple)
