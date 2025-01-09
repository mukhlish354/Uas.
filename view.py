class View:
    """Class untuk menampilkan dan mengelola interaksi dengan pengguna."""
    @staticmethod
    def tampilkan_menu():
        print("\n=== Menu Barang ===")
        print("1. Tambah Barang")
        print("2. Lihat Semua Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Hitung Total Harga")
        print("6. Keluar")
        return input("Pilih menu (1-6): ")

    @staticmethod
    def input_barang():
        id_barang = input("Masukkan ID Barang: ")
        nama = input("Masukkan Nama Barang: ")
        harga = input("Masukkan Harga Barang: ")
        return id_barang, nama, harga

    @staticmethod
    def tampilkan_barang(barang_list):
        if not barang_list:
            print("Tidak ada barang dalam daftar.")
            return
        print("\nDaftar Barang:")
        print("{:<10} {:<20} {:<10}".format('ID', 'Nama', 'Harga'))
        print("-" * 40)
        for barang in barang_list:
            print("{:<10} {:<20} {:<10}".format(barang.id_barang, barang.nama, barang.harga))

    @staticmethod
    def input_update():
        id_barang = input("Masukkan ID Barang yang ingin diupdate: ")
        nama = input("Masukkan Nama Baru (kosongkan untuk tidak mengubah): ")
        harga = input("Masukkan Harga Baru (kosongkan untuk tidak mengubah): ")
        return id_barang, nama, harga

    @staticmethod
    def input_hapus():
        return input("Masukkan ID Barang yang ingin dihapus: ")

    @staticmethod
    def tampilkan_pesan(pesan):
        print(pesan)
