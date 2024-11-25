books = {}

def add_book(author, title, genre, year, publisher):
    books[title] = {
        'author': author,
        'genre': genre,
        'year': year,
        'publisher': publisher
    }
    print(f"Kniha '{title}' byla přidána.")

def delete_book(title):
    if title in books:
        del books[title]
        print(f"Kniha '{title}' byla odstraněna.")
    else:
        print(f"Kniha '{title}' nebyla nalezena.")

def search_book(title):
    if title in books:
        book = books[title]
        print(f"Nalezená kniha: {title}, Autor: {book['author']}, Žánr: {book['genre']}, Rok: {book['year']}, Vydavatel: {book['publisher']}")
    else:
        print(f"Kniha '{title}' nebyla nalezena.")

def search_by_author(author):
    found = False
    for title, book in books.items():
        if book['author'].lower() == author.lower():
            print(f"Nalezená kniha: {title}, Autor: {book['author']}, Žánr: {book['genre']}, Rok: {book['year']}, Vydavatel: {book['publisher']}")
            found = True
    if not found:
        print(f"Autor '{author}' nebyl nalezen.")

def replace_book(old_title, new_author, new_title, new_genre, new_year, new_publisher):
    if old_title in books:
        delete_book(old_title)
        add_book(new_author, new_title, new_genre, new_year, new_publisher)
        print(f"Kniha '{old_title}' byla nahrazena knihou '{new_title}'.")
    else:
        print(f"Kniha '{old_title}' nebyla nalezena.")

def list_books():
    if books:
        print("\nSeznam knih:")
        for title, book in books.items():
            print(f"Název: {title}, Autor: {book['author']}, Žánr: {book['genre']}, Rok: {book['year']}, Vydavatel: {book['publisher']}")
    else:
        print("Knihovna je prázdná.")

def list_authors():
    authors = set(book['author'] for book in books.values())
    if authors:
        print("\nSeznam autorů:")
        for author in authors:
            print(author)
    else:
        print("Žádní autoři nebyli nalezeni.")

def list_publishers():
    publishers = set(book['publisher'] for book in books.values())
    if publishers:
        print("\nSeznam nakladatelství:")
        for publisher in publishers:
            print(publisher)
    else:
        print("Žádná nakladatelství nebyla nalezena.")

add_book("Robert Bryndza", "Dívka v ledu", "Krimi", 2016, "Grada")
add_book("Robert Bryndza", "Noční lov", "Krimi", 2017, "Grada")
add_book("Robert Bryndza", "Temné hlubiny", "Krimi", 2017, "Grada")
add_book("Robert Bryndza", "Do posledního dechu", "Krimi", 2018, "Grada")
add_book("Robert Bryndza", "Studená krev", "Krimi", 2018, "Grada")
add_book("Peter May", "Černý dům", "Detektivka", 2011, "Host")
add_book("Peter May", "Šachové figurky", "Detektivka", 2012, "Host")
add_book("Peter May", "Muž z ostrova Lewis", "Detektivka", 2013, "Host")
add_book("Peter May", "Pán ohně", "Detektivka (Čína)", 2005, "Motto")
add_book("Peter May", "Čínské jezero", "Detektivka (Čína)", 2006, "Motto")
add_book("Peter May", "Čínské stíny", "Detektivka (Čína)", 2007, "Motto")
add_book("Peter May", "Čtvrtá oběť", "Detektivka (Čína)", 2008, "Motto")
add_book("Peter May", "Pán světla", "Detektivka (Čína)", 2009, "Motto")
add_book("Peter May", "Čínský thriller", "Detektivka (Čína)", 2010, "Motto")

if __name__ == "__main__":
    while True:
        print("\nMožnosti:")
        print("1. Přidat knihu")
        print("2. Odstranit knihu")
        print("3. Vyhledat knihu podle názvu")
        print("4. Vyhledat knihy podle autora")
        print("5. Nahradit knihu")
        print("6. Zobrazit všechny knihy")
        print("7. Zobrazit seznam autorů")
        print("8. Zobrazit seznam nakladatelství")
        print("9. Ukončit")
        choice = input("Zadejte číslo možnosti: ")

        if choice == "1":
            author = input("Zadejte autora: ")
            title = input("Zadejte název knihy: ")
            genre = input("Zadejte žánr: ")
            year = int(input("Zadejte rok vydání: "))
            publisher = input("Zadejte vydavatele: ")
            add_book(author, title, genre, year, publisher)
        elif choice == "2":
            title = input("Zadejte název knihy, kterou chcete odstranit: ")
            delete_book(title)
        elif choice == "3":
            title = input("Zadejte název knihy, kterou chcete vyhledat: ")
            search_book(title)
        elif choice == "4":
            author = input("Zadejte autora, jehož knihy chcete vyhledat: ")
            search_by_author(author)
        elif choice == "5":
            old_title = input("Zadejte název knihy, kterou chcete nahradit: ")
            new_author = input("Zadejte nového autora: ")
            new_title = input("Zadejte nový název knihy: ")
            new_genre = input("Zadejte nový žánr: ")
            new_year = int(input("Zadejte nový rok vydání: "))
            new_publisher = input("Zadejte nového vydavatele: ")
            replace_book(old_title, new_author, new_title, new_genre, new_year, new_publisher)
        elif choice == "6":
            list_books()
        elif choice == "7":
            list_authors()
        elif choice == "8":
            list_publishers()
        elif choice == "9":
            break
        else:
            print("Neplatná volba, zkuste to znovu.")
