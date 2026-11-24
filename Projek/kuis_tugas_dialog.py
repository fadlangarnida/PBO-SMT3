import time


class People:
    lebar_nama = 0  # lebar kolom nama, menyesuaikan nama terpanjang

    def __init__(self, nama):
        self.nama = nama
        People.lebar_nama = max(People.lebar_nama, len(nama))

    def bicara(self, kalimat, jeda=1.2):
        time.sleep(jeda)  # jeda sebelum berbicara
        print(f"{self.nama.ljust(People.lebar_nama)} : {kalimat}")


def narasi(teks, jeda=1.2):
    time.sleep(jeda)
    # Diberi indentasi agar sejajar dengan kolom kalimat
    print(f"{' ' * (People.lebar_nama + 3)}({teks})")


# Membuat tokoh (semua dibuat dulu agar lebar kolom sudah final)
fadlan = People("Fadlan")
bayu = People("Bayu")
anak = People("Anak Warnet")

# Dialog: (tokoh, kalimat) | ("narasi", keterangan)
dialog = [
    ("narasi", "Fadlan dan Bayu memasuki warnet."),
    (fadlan, "Kepaksa kita ke warnet bay. Komputer kampus belum di-upgrade, laptop juga masih diservis."),
    (bayu, "Nasib mahasiswa, dlan. Belajar teknoligi, tapi fasilitasnya masih zaman batu."),
    (fadlan, "dahlah, yang penting tugas beres. Besok harus dikumpulin."),
    (bayu, "Aman! Hari ini focus tugas, gak ada game!"),
    ("narasi", "Mereka duduk dan mulai mengerjakan tugas. Dari belakang terdengar anak-anak berteriak."),
    (anak, "WOI! MUSUH DI BELAKANG! BANTUIN GUE COK!"),
    (fadlan, "Baru juga nyalain komputer, udah ada yg knock tuh."),
    (bayu, "Namanya juga warnet. banyak bocah sedang memperjuangkan masa depan rank-nya."),

    ("narasi", "Baru setengah jam billing warnet berjalan tiba-tiba listrik padam dan semua komputer mati."),
    (fadlan, "LAH! MATI COK?!"),
    (bayu, "Paling PLN nya meninggal, dlan!"),
    (fadlan, "Tugasnya belum di save jir~"),
    (bayu, "HEBAT! belum lu Ctrl+S?"),
    (fadlan, "belum lah"),
    (bayu, "Mahasiswa Ilmu Komputer, tapi lupa menyimpan dokumen, mainnya hebat"),
    ("narasi", "Beberapa menit kemudian listrik kembali menyala."),
    (fadlan, "Alhamdulillah! tugasnya masih ada!"),
    (bayu, "Untung ada teknologi Bernama autosave."),
    (fadlan, "Dahlah, lanjut nugas. takut mati listrik lagi."),

    ("narasi", "Waktu berjalan. Fadlan dan Bayu mulai merasa bosan mengerjakan tugas."),
    (bayu, "Dlan..."),
    (fadlan, "hah?"),
    (bayu, "Lu nggak bosen?"),
    (fadlan, "Bosen lah, tapi deadline tugasnya besok."),
    (bayu, "Di sebelah ada komputer kosong noh."),
    (fadlan, "Terus?"),
    (bayu, "Ada game baru."),
    (fadlan, "Jangan mulai."),
    (bayu, "Cuma lihat bentar."),
    (fadlan, "Niat ke warnet nya nugas tapi kalah ama pop up game."),
    (bayu, "Se match saja. Biar segar."),
    (fadlan, "Yaudah se match dah. abis tu balik gerjain tugas."),
    (bayu, "Deal!"),
    ("narasi", "Keduanya malah bermain game."),
    (bayu, "DLAN! BANTU DLAN! MUSUH MUSUH!"),
    (fadlan, "Sabar, ini gua backup!"),
    (bayu, "KIRI! KIRI!"),
    (fadlan, "WOI JANGAN NGEBAIT! MANA KIRI, JELAS JELAS MUSUHNYA DI KANAN!"),
    (bayu, "HAHAHA! NOOB BANGET!"),
    (fadlan, "Lu sendiri juga mati bodo!"),
    ("narasi", "Mereka tertawa dan melanjutkan permainan."),

    ("narasi", "Beberapa pertandingan berlalu. Keduanya semakin serius bermain."),
    (bayu, "Se match lagi, Dlan!"),
    (fadlan, "Terakhir ye."),
    ("narasi", "Beberapa menit kemudian."),
    (bayu, "MENANG COY! MENANG!"),
    (fadlan, "Finally up rank!"),
    (bayu, "Lanjut se game?"),
    (fadlan, "gas, beres ini balik ngerjain tugas."),
    ("narasi", "Mereka kembali bermain. namun di tengah permainan Tiba-tiba ponsel Fadlan berbunyi."),
    (fadlan, "Bay, alarm gue bunyi."),
    (bayu, "Alarm apa?"),
    (fadlan, "Alarm tugas."),
    (bayu, "Emang sekarang jam berapa?."),
    ("narasi", "Fadlan melihat ponselnya."),
    (fadlan, "..."),
    (bayu, "napa?"),
    (fadlan, "JAM SETENGAH DUA BELAS MALEM!"),
    (bayu, "HAH?! KITA MAIN DARI TADI?!"),
    (fadlan, "ENGGAK,MAIN DARI TAHUN KEMAREN ! TUGAS BELUM KELAR!"),
    (bayu, "Astagfirullah! lupa waktu!"),
    (fadlan, "Katanya se game"),
    (bayu, "Ternyata se game itu relatif."),
    (fadlan, "Relatif apaan?! Ini udah hampir tengah malem!"),

    ("narasi", "Keduanya buru-buru menutup game dan membuka dokumen tugas."),
    (fadlan, "buru! Kerjain bagian kesimpulan!"),
    (bayu, "aman! Gue cari referensi tambahan."),
    (fadlan, "Jangan buka game lagi!"),
    (bayu, "Tenang. udah gue tutup."),
    ("narasi", "Beberapa menit berlalu. dengan kekuatan kepepet deadline tugas hamper selesai"),
    (fadlan, "Bay, bagian pembahasan udah belum?"),
    (bayu, "udah."),
    (fadlan, "Kesimpulan?"),
    (bayu, "Dikit lagi."),
    (fadlan, "Daftar pustaka?"),
    (bayu, "Lagi gue rapihin."),
    (fadlan, "Bagus. Sekarang kita tinggal kumpulkan."),
    ("narasi", "Bayu menekan tombol kirim."),
    (bayu, "BERHASIL KEKIRIM!"),
    (fadlan, "Alhamdulillah. Kelar juga."),
    (bayu, "Heboh banget ya hari ini."),
    (fadlan, "Hadeh, dari komputer kampus yang belum di-upgrade, laptop rusak, anak warnet berisik, listrik mati, sampai lupa tugas gara-gara game."),
    (bayu, "Tapi setidaknya tugas kita selesai."),
    (fadlan, "Iya. Besok besok kelarin tugas dulu dah baru nge game"),
    (bayu, "Setuju. gak lagi lagi dah main game tengah tengah nugas"),
    ("narasi", "Bayu tiba-tiba melihat layar komputer."),
    (bayu, "Dlan..."),
    (fadlan, "Apa?"),
    (bayu, "Ada diskon paket malam ini."),
    (fadlan, "..."),
    (bayu, "Mau tambah satu jam?"),
    (fadlan, "PULANG!"),
    ("narasi", "Fadlan langsung membereskan tas dan menarik Bayu keluar dari warnet."),
    (bayu, "WOI! TUNGGU! GUE BELUM LOG OUT GAME!"),
    ("narasi", "Keduanya keluar sambil berdebat."),
]


# Judul
print("Niat Mengerjakan Tugas, Malah Main Game")

# Putar dialog satu per satu
for tokoh, isi in dialog:
    if tokoh == "narasi":
        narasi(isi)
    else:
        tokoh.bicara(isi)

print("\n=== TAMAT ===")