class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Input Data Diri Kalian
aul = Mahasiswa("Aulia Azizah","B","Pendikom","FKIP","Alam Segar 3","Kab. Paser"
)

# Menampilkan informasi mahasiswa
print(f"Nama: {aul.nama}")
print(f"Kelas: {aul.kelas}")
print(f"Prodi: {aul.prodi}")
print(f"Fakultas: {aul.fakultas}")
print(f"Tempat Tinggal: {aul.tempat_tinggal}")
print(f"Asal: {aul.asal}")

