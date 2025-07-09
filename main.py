import sqlite3

# tabela z pliku SQL
conn = sqlite3.connect('fandom.db')
cursor = conn.cursor()

with open('create_tables.sql', 'r') as f:
    sql_script = f.read()

cursor.executescript(sql_script)

print("Tabele zostały utworzone!")

cursor.execute("""
DELETE FROM pages
WHERE id NOT IN (
    SELECT MIN(id)
    FROM pages
    WHERE title = 'The Mandalorian'
)
AND title = 'The Mandalorian'
""")
print("Usunięto duplikaty The Mandalorian! ")

# Lista stron do dodania
pages_to_add = [
    ("The Mandalorian", "https://starwars.fandom.com/wiki/The_Mandalorian", 12345, 67),
    ("The Last of Us", "https://thelastofus.fandom.com/wiki/The_Last_of_Us", 20000, 50),
    ("Game of Thrones", "https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki", 50000, 300),
    ("Breaking Bad", "https://breakingbad.fandom.com/wiki/Breaking_Bad_Wiki", 40000, 150),
    ("Stranger Things", "https://strangerthings.fandom.com/wiki/Stranger_Things_Wiki", 35000, 200)
]

for page in pages_to_add:
    title = page[0]
    cursor.execute("SELECT * FROM pages WHERE title = ?", (title,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(
            "INSERT INTO pages (title, url, views, edits) VALUES (?, ?, ?, ?)",
            page
        )
        print(f"Dodano: {title}")
    else:
        print(f"{title} już istnieje — pominięto.")

cursor.execute("SELECT * FROM pages")
rows = cursor.fetchall()

print("\nZawartość tabeli pages:")
for row in rows:
    print(row)

# TOP 5 wg views
print("\nTOP 5 stron wg liczby wyświetleń:")
cursor.execute("SELECT title, views FROM pages ORDER BY views DESC LIMIT 5")
top_pages = cursor.fetchall()

for page in top_pages:
    print(f"{page[0]} — {page[1]} views")

conn.commit()
conn.close()