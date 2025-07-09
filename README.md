# Fandom Wiki Analytics

Cześć!  
To jest mój mały projekt, w którym chciałam poćwiczyć **Pythona** i **SQL** na czymś praktycznym, co pasuje do świata fanowskich wiki.

## O projekcie

Ten skrypt:
- Tworzy prostą bazę danych SQLite z tabelami dla stron (`pages`) i użytkowników (`users`).
- Dodaje przykładowe rekordy stron z tytułem, linkiem, liczbą wyświetleń i edycji.
- Sprawdza, czy strona już istnieje, żeby nie tworzyć duplikatów.
- Czyści stare duplikaty, jeśli są.
- Pokazuje całą zawartość tabeli.
- Generuje ranking **TOP 5 stron według liczby wyświetleń**.

## Użyte narzędzia

- **Python 3**
- **SQLite** (bez dodatkowego serwera — baza działa jako plik)
- Moduł `sqlite3` (wbudowany w Pythona)

## Jak to uruchomić

1. Upewnij się, że masz zainstalowanego Pythona.
2. Otwórz terminal w folderze projektu.
3. Wpisz:
   ```bash
   python main.py