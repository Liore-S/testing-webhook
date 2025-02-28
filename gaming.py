import random

def generate_username(name):
    # Menghasilkan angka acak antara 100 dan 999
    random_number = random.randint(100, 999)
    # Menggabungkan nama dengan angka acak
    username = f"{name}{random_number}"
    return username

# Contoh penggunaan
nama_pengguna = "Player"
username_game = generate_username(nama_pengguna)
print(f"Username game Anda adalah: {username_game}")