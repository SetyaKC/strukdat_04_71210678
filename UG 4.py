import json
with open("mahasiswa.json","r") as file:
    data = json.load(file)
    d = dict()
    masuk = int(input("Masukkan jumlah mahasiswa baru: "))
    for i in range(masuk):
        nama = input ("Masukkan nama anda: ")
        x = []
        h = int(input ("Masukkan jumlah hobi: "))
        for i in range(h):
            hobi = input(f"Masukkan hobi ke-{i+1}:")
            x.append(hobi)
        prestasi = input("Masukkan prestasi anda: ")
        print("=== Data berhasil ditambahkan ====")
        print()

        d[nama] = [{"Biodata":{"Hobi":x, "Prestasi": prestasi}}]

    data.update(d)

with open("mahasiswa.json","w")as file:
    json.dump(data,file)

