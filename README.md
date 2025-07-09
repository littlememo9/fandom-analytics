# Fandom Wiki Analytics

Hi!   
This is a small side project I made to practice **Python** and **SQL** on something practical and fun - fandom wiki data.

## About this project

This script:
- Creates a simple SQLite database with two tables: `pages` and `users`.
- Adds example pages with title, link, views, and edits.
- Checks if a page already exists to avoid duplicates.
- Removes old duplicates if there are any.
- Shows the full content of the `pages` table.
- Generates a **TOP 5 pages by number of views** ranking.

## Tools used

- **Python 3**
- **SQLite** (no separate server needed - the database is a single file)
- `sqlite3` module (built into Python)

## How to run it

1. Make sure you have Python installed.
2. Open your terminal in the project folder.
3. Run:
   ```bash
   python main.py
