from book import Book # Mengimport kelas Book dari file book.py
import os # Mengimport modul os untuk operasi sistem

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # Membersihkan layar terminal (Windows: 'cls', Unix: 'clear')

# Fungsi untuk menampilkan menu utama
def show_menu():
    print("=== Sistem Manajemen Buku Perpustakaan ===") # Menampilkan judul sistem
    print("[1] Tambah Buku") # Opsi untuk menambah buku
    print("[2] Lihat Daftar Buku") # Opsi untuk melihat daftar buku
    print("[3] Cari Buku") # Opsi untuk mencari buku
    print("[4] Hapus Buku") # Opsi untuk menghapus buku
    print("[5] Keluar") # Opsi untuk keluar dari program

# Fungsi untuk menambahkan buku
def add_book(books):
    clear_screen() # Membersihkan layar sebelum menambah buku
    title = input("Masukkan judul buku: ") # Meminta input judul buku
    author = input("Masukkan penulis buku: ") # Meminta input penulis buku
    book = Book(title, author) # Membuat objek Book baru
    books.append(book) # Menambahkan buku ke dalam daftar buku
    print(f"Buku '{title}' oleh {author} telah ditambahkan.") # Mengonfirmasi buku telah ditambahkan
    input("Tekan Enter untuk kembali ke menu utama...") # Menunggu input untuk kembali ke menu utama

# Fungsi untuk menampilkan daftar buku
def view_books(books):
    clear_screen() # Membersihkan layar sebelum menampilkan daftar buku
    if not books: # Mengecek apakah daftar buku kosong
        print("Belum ada buku yang ditambahkan.") # Menampilkan pesan jika tidak ada buku
    else:
        print("Daftar Buku:") # Menampilkan judul daftar buku
        for idx, book in enumerate(books): # Mengiterasi daftar buku dengan indeks
            print(f"{idx + 1}. {book.title} oleh {book.author}") # Menampilkan buku dengan nomor, judul, dan penulis
    input("Tekan Enter untuk kembali ke menu utama...") # Menunggu input untuk kembali ke menu utama

# Fungsi untuk mencari buku berdasarkan judul
def search_books(books):
    clear_screen() # Membersihkan layar sebelum mencari buku
    search_title = input("Masukkan judul buku yang dicari: ") # Meminta input judul buku yang dicari
    found_books = [book for book in books if search_title.lower() in book.title.lower()] # Mencari buku yang mengandung judul yang dicari
    if not found_books: # Mengecek apakah ada buku yang ditemukan
        print(f"Tidak ada buku dengan judul '{search_title}'.") # Menampilkan pesan jika tidak ada buku yang ditemukan
    else:
        print("Buku ditemukan:") # Menampilkan pesan jika buku ditemukan
        for book in found_books: # Mengiterasi daftar buku yang ditemukan
            print(f"{book.title} oleh {book.author}") # Menampilkan buku yang ditemukan
    input("Tekan Enter untuk kembali ke menu utama...") # Menunggu input untuk kembali ke menu utama

# Fungsi untuk menghapus buku
def delete_book(books):
    clear_screen() # Membersihkan layar sebelum menghapus buku
    view_books(books) # Menampilkan daftar buku untuk memilih buku yang akan dihapus
    if books: # Mengecek apakah daftar buku tidak kosong
        try:
            book_index = int(input("Masukkan nomor buku yang akan dihapus: ")) - 1 # Meminta input nomor buku yang akan dihapus
            if 0 <= book_index < len(books): # Mengecek apakah nomor buku valid
                deleted_book = books.pop(book_index) # Menghapus buku dari daftar
                print(f"Buku '{deleted_book.title}' oleh {deleted_book.author} telah dihapus.") # Mengonfirmasi buku telah dihapus
            else:
                print("Nomor buku tidak valid.") # Menampilkan pesan jika nomor buku tidak valid
        except ValueError:
            print("Masukkan nomor yang valid.") # Menampilkan pesan jika input bukan nomor
    input("Tekan Enter untuk kembali ke menu utama...") # Menunggu input untuk kembali ke menu utama

# Fungsi utama untuk menjalankan program
def main():
    books = [] # Inisialisasi daftar buku kosong
    while True: # Looping utama program
        clear_screen() # Membersihkan layar setiap kali loop
        show_menu() # Menampilkan menu utama
        choice = input("Pilih menu: ") # Meminta input pilihan menu
        if choice == '1': # Jika pilihan adalah 1
            add_book(books) # Panggil fungsi add_book
        elif choice == '2': # Jika pilihan adalah 2
            view_books(books) # Panggil fungsi view_books
        elif choice == '3': # Jika pilihan adalah 3
            search_books(books) # Panggil fungsi search_books
        elif choice == '4': # Jika pilihan adalah 4
            delete_book(books) # Panggil fungsi delete_book
        elif choice == '5': # Jika pilihan adalah 5
            break # Keluar dari loop dan mengakhiri program
        else:
            input("Pilihan tidak valid. Tekan Enter untuk mencoba lagi...") # Menampilkan pesan jika pilihan tidak valid

if __name__ == "__main__": # Memastikan script dijalankan secara langsung
    main() # Memanggil fungsi utama main