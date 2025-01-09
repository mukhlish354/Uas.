from data import Barang

class Proses:
    """Class untuk mengelola logika dan operasi pada data barang."""
    def __init__(self):
        self.barang_list = []

    def tambah_barang(self, id_barang, nama, harga):
        try:
            harga = float(harga)  # Validasi harga harus berupa angka
            barang = Barang(id_barang, nama, harga)
            self.barang_list.append(barang)
            return "Barang berhasil ditambahkan."
        except ValueError:
            return "Harga harus berupa angka. Barang tidak ditambahkan."

    def lihat_barang(self):
        return self.barang_list

    def update_barang(self, id_barang, nama_baru, harga_baru):
        for barang in self.barang_list:
            if barang.id_barang == id_barang:
                if nama_baru:
                    barang.nama = nama_baru
                if harga_baru:
                    try:
                        barang.harga = float(harga_baru)  # Validasi harga baru
                    except ValueError:
                        return "Harga baru harus berupa angka. Barang tidak diperbarui."
                return "Barang berhasil diperbarui."
        return "Barang dengan ID tersebut tidak ditemukan."

    def hapus_barang(self, id_barang):
        for barang in self.barang_list:
            if barang.id_barang == id_barang:
                self.barang_list.remove(barang)
                return "Barang berhasil dihapus."
        return "Barang dengan ID tersebut tidak ditemukan."

    def total_harga(self):
        total = sum(barang.harga for barang in self.barang_list)
        return f"Total harga semua barang adalah: {total:.2f}"
