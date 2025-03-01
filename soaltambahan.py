class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

# Membuat objek
mhs = Mahasiswa("Axel")

# Menampilkan nama
print("Nama:", mhs.nama)

# Menghapus atribut 'nama'
del mhs.nama

# Coba akses atribut yang sudah dihapus
try:
    print(mhs.nama)
except AttributeError:
    print("Atribut 'nama' sudah dihapus!")

# Menghapus objek 'mhs'
del mhs

# Coba akses objek yang sudah dihapus
try:
    print(mhs)
except NameError:
    print("Objek 'mhs' sudah dihapus!")
