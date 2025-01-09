from view import View
from proses import Proses

def main():
    proses = Proses()
    while True:
        pilihan = View.tampilkan_menu()
        if pilihan == '1':
            id_barang, nama, harga = View.input_barang()
            pesan = proses.tambah_barang(id_barang, nama, harga)
            View.tampilkan_pesan(pesan)
        elif pilihan == '2':
            barang_list = proses.lihat_barang()
            View.tampilkan_barang(barang_list)
        elif pilihan == '3':
            id_barang, nama, harga = View.input_update()
            pesan = proses.update_barang(id_barang, nama, harga)
            View.tampilkan_pesan(pesan)
        elif pilihan == '4':
            id_barang = View.input_hapus()
            pesan = proses.hapus_barang(id_barang)
            View.tampilkan_pesan(pesan)
        elif pilihan == '5':
            pesan = proses.total_harga()
            View.tampilkan_pesan(pesan)
        elif pilihan == '6':
            View.tampilkan_pesan("Keluar dari program. Terima kasih!")
            break
        else:
            View.tampilkan_pesan("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
