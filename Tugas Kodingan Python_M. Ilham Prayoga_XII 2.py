import math

# Fungsi untuk menghitung luas lingkaran
def hitung_luas(jari_jari):
    return math.pi * jari_jari**2

# Fungsi untuk menghitung keliling lingkaran
def hitung_keliling(jari_jari):
    return 2 * math.pi * jari_jari

# Meminta input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas dan keliling
luas = hitung_luas(jari_jari)
keliling = hitung_keliling(jari_jari)

# Menampilkan hasil
print(f"Luas lingkaran: {luas:.2f}")
print(f"Keliling lingkaran: {keliling:.2f}")
