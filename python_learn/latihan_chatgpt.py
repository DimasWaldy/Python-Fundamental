from dasar_sintaksis_dictionary import result, users

data_mahasiswa = [
    {
    "nama" : "Dimas",
    "nim" : "1234",
    "jurusan" : "TI"
    },
    {"nama" : "Rania",
    "nim" : "1235",
    "jurusan" : "Ekonomi"
     },
    {
     "nama": "Ikon",
     "nim": "1236",
     "jurusan": "SI"
     },
]
#mencetak data mahasiswa
print(data_mahasiswa)

#ubah ke json
import json
results = json.dumps(data_mahasiswa)

with open('results.json', 'w') as file:
    json.dump(data_mahasiswa, file, indent=4)
