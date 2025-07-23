print("\nPerintah del dengan list comprehension")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
del daftar_buku[0:2]
# 0 (digunakan untuk memulai menghapusnya mulai dari mana) : 2 buku yang dihapus dari urutan 0 ada 2
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking', 'Matematika']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat List Baru")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking', 'Matematika']
daftar_buku_baru = daftar_buku [:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat List Baru")
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat List Baru dengan Comprehension : ganjil")
daftar_buku = ['1 Harry potter', '2 Game of Thrones', '3 Cooking', '4 Matematika']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat List Baru dengan Comprehension : genap")
daftar_buku = ['1 Harry potter', '2 Game of Thrones', '3 Cooking', '4 Matematika']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])