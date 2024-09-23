import json

# Načtení JSON souboru
with open('books.json') as f:
    data = json.load(f)

# Počet znaků JSON
pocetZnaku = 0
for book in data['books']:
    for klic, hodnota in book.items():
        pocetZnaku += len(str(klic)) + len(str(hodnota))

print(f"\nCelkový počet znaků: {len(str(data))}")
print(f"Počet znaků pouze hodnot a klíčů: {pocetZnaku}\n")

# Print JSON souboru
for book in data['books']:
    print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Status: {book['status']}")

# Přidání, odebrání knihy do JSON
def bookAdding():
    title = input("\nNázev: ")
    author = input("Autor: ")
    isbn = input("ISBN: ")

    return {
        "title": title,
        "author": author,
        "isbn": isbn,
        "status": "Available"
    }

def bookRemoving():
    title = input("\nNázev knihy: ")
    for book in data['books']:
        if book['title'] == title:
            return book
    print("\nKniha nebyla nalezena.")

choice = input("\n[1 - Přidat, 2 - Odebrat, 3 - Nic]: ")
if choice == '1':
    data['books'].append(bookAdding())
elif choice == '2':
    data['books'].remove(bookRemoving())

# Finální přepsání JSON
with open("books.json", "w") as f:
    json.dump(data, f, indent=2)

print("\nDone!")