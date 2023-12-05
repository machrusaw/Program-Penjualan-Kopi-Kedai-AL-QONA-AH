def login(username,password):
    berhasil = False
    file = open("databaseakun.txt", "r")
    for f in file:
        a,b = f.split(",")
        b = b.strip()
        if(a==username and b==password):
            berhasil = True
            break
    file.close()
    if(berhasil):
        print("-" * 67)
        print("| Login Berhasil, Silahkan Pesan Sesuai dengan Menu yang Tersedia |")
        print("-" * 67)
    else:
        print("-" * 60)
        print("| Akun anda tidak ditemukan, silahan buat akun anda dahulu |")
        print("-" * 60)
        buat()

def awal():
    print("=" * 80)
    print("        |  Selamat Datang di Program Penjualan Kopi Kedai AL-QONA'AH  |")
    print(" |  Sebelumnya Silahkan untuk Login Terlebih Dahulu untuk Mengakses Program  |")
    print("-" * 80)
    print("")

def menu():
    global pilih
    print("=" * 38)
    print("<< Menu Login Program Al - Qona'ah >>")
    print("  | 1.) Login Akun                |")
    print("  | 2.) Buat Akun Baru            |")
    print("=" * 38)
    pilih = input("silahkan masukkan (1/2): ")
    if (pilih != "1" and pilih != "2"):
        print("Maaf Inputan anda salah... Silahkan Coba Lagi!!")
        menu()
    elif pilih == "2":
        buat()

def register(username, password):
    file = open("databaseakun.txt", "a")
    file.write("\n"+ username + "," + password)

def masuk():
    global username
    if (pilih == "1"):
        print("Anda sedang di halaman login")
        username = input(">> Masukkan Username : ")
        password = input(">> Masukkan Password : ")
        login(username,password)

    else:
        username = input(">> Masukkan Username : ")
        password = input(">> Masukkan Password : ")
        login(username,password)

def buat() :
    global username
    if (pilih == "2"):
        print("| Masukkan Username dan Password baru anda |")
        username = input("> Masukkan Username Baru : ")
        password = input("> Masukkan Password Baru : ")
        register(username, password)
        print("| Register Anda Berhasil, Silahkan Login terlebih dahulu untuk melanjutkan pembelian |")
    else:
        print("Apakah anda ingin membuat akun baru?")
        tanya = input("Jika ingin buat baru ketik (y/Y) atau (t/T) jika tidak : ")
        if tanya == "y" or tanya =="Y":
            print("| Masukkan Username dan Password baru anda |")
            username = input("> Masukkan Username Baru : ")
            password = input("> Masukkan Password Baru : ")
            register(username, password)
            print("| Register Anda Berhasil, Silahkan Masuk dulu untuk melanjutkan pembelian |")
            masuk()
        elif tanya == "t" or tanya =="T":
            masuk()
        else:
            print("Masukkan anda salah.. Coba Lagi!!")
            return buat()

awal()
menu()
masuk()


def get_week_day(date):
    week_day_dict = {
    0 : "senin",
    1 : "selasa",
    2 : "rabu",
    3 : "kamis",
    4 : "jum'at",
    5 : "sabtu",
    6 : "minggu",
    }
    day = date.weekday()
    return week_day_dict[day]

def penjualan():
    global username
    global password
    print("")
    print("========== PROGRAM PENJUALAN KOPI ==========")
    print("============== KEDAI QONA'AH ===============")
    print("")
    print(">> Nama akun anda adalah :", username)
    from datetime import datetime
    now = datetime.now()
    week = get_week_day(now)
    print("<> Hari=", week)
    current_date = now.strftime("%Y-%m-%d")
    print("<> Tanggal = ",current_date)
    current_time = now.strftime("%H:%M:%S")
    print("<> Jam =", current_time)

    print("")

penjualan()

total = 0
jenis = ""
gelas = 0

def fungsimenu():
    global total
    global gelas
    global jenis
    print("===== Menu Minuman Kopi =====")
    print("1. Kopi Susu      >> Rp15.000")
    print("2. Americano      >> Rp19.000")
    print("3. Latte          >> Rp18.000")
    print("4. Cappuccino     >> Rp18.000")
    print("==============================")

    try:
        pilihan = int(input("<> Masukan Pilihan Sesuai dengan Menu : "))
    except ValueError:
        print("Inputan harus berupa angka... Coba lagi!!")
        return fungsimenu()

    try:
        gelas = int(input("<> Pesan Berapa Gelas : "))
    except ValueError:
        print("Inputan harus berupa angka... Coba lagi!!")
        return fungsimenu()

    if gelas < 1:
        print("MAAF INPUTAN YANG ANDA MASUKKAN SALAH, SILAHKAN MASUKKAN KEMBALI!!")
        fungsimenu()

    if pilihan == 1:
        total = gelas * 15000
        print(">>", gelas, " Kopi Susu dengan Harga = Rp", total)
        jenis = ("Kopi Susu")
    elif pilihan == 2:
        total = gelas * 19000
        print(">>", gelas, "American0 dengan Harga = Rp", total)
        jenis = ("Americano")
    elif pilihan == 3:
        total = gelas * 18000
        print(">>", gelas, "Latte dengan Harga = Rp", total)
        jenis = ("Latte")
    elif pilihan == 4:
        total = gelas * 18000
        print(">>", gelas, "Cappucino dengan Harga = Rp", total)
        jenis = ("Cappucino")

    else:
        print("Pilihan Menu Tidak Tersedia, Silahkan Masukkan Lagi!!!")
        return fungsimenu()

fungsimenu()

def menumakan():
    global pesan_makan
    print("")
    print("Ketik (y/Y) jika ingin memesan, (t/T) untuk tidak.. ")
    pesan_makan = input("Apakah anda ingin pesan makanan juga ?")
    if pesan_makan == "y" or pesan_makan == "Y":
        if pesan_makan == "y" or pesan_makan == "Y":
            print("")
            menuMakan = ['Kentang Goreng', 'Pisang Cokelat', 'Roti Bakar Keju', 'Kebab', 'Canai']
            harga = [10000, 8000, 11000, 10000, 8000]
            print("==========================================")
            print(" MENU MAKANAN: ")
            print("==========================================")
            for x in range(len(menuMakan)):
                print(f'{x + 1}. {menuMakan[x]} : {harga[x]}')
            print("")
    elif pesan_makan == "t" or pesan_makan == "T":
        pass
    else:
        print("Anda salah memasukkan inputan... Coba lagi!!")
        menumakan()
menumakan()

def pemesanan():
    global total_mkan
    global jenis2
    global makan
    global porsi
    global harga
    global pesan_makan
    harga = [10000, 8000, 11000, 10000, 8000]
    if pesan_makan == "y" or pesan_makan == "Y":
        try:
            pesanan = int(input(">> Mau pesan makan apa? (masukkan sesuai nomor) : "))
        except ValueError:
            print("Inputan harus berupa angka... Coba lagi!!")
            return pemesanan()

        try:
            porsi = int(input(">> Pesan berapa porsi : "))
        except ValueError:
            print("Inputan harus berupa angka... Coba lagi!!")
            return pemesanan()

        if porsi < 1:
            print("MAAF INPUTAN YANG ANDA MASUKKAN SALAH, SILAHKAN MASUKKAN KEMBALI!!")
            return pemesanan()

        if pesanan == 1:
            total_mkan = harga[pesanan - 1] * porsi
            print(">>", porsi, "Kentang Goreng dengan harga Rp.",total_mkan)
            jenis2 = ("Kentang Goreng")
        elif pesanan == 2:
            total_mkan = harga[pesanan - 1] * porsi
            print(">>", porsi, "Pisang Cokelat dengan harga Rp.",total_mkan)
            jenis2 = ("Pisang Cokelat")
        elif pesanan == 3:
            total_mkan = harga[pesanan - 1] * porsi
            print(">>", porsi, "Roti Bakar Keju dengan harga Rp.", total_mkan)
            jenis2 = ("Roti Bakar Keju")
        elif pesanan == 4:
            total_mkan = harga[pesanan - 1] * porsi
            print(">>", porsi, "Kebab dengan harga Rp.",total_mkan)
            jenis2 = ("Kebab")
        elif pesanan == 5:
            total_mkan = harga[pesanan - 1] * porsi
            print(">>", porsi, "Canai dengan harga Rp.",total_mkan)
            jenis2 = ("Canai")
        else:
            print("Pilihan Menu Tidak Tersedia, Silahkan Masukkan Lagi!!!")
            pemesanan()

pemesanan()

def pembayaran():
    global tunai
    global porsi
    global totalSemua
    global totalSemua1
    global jenis2
    global total_mkan
    if pesan_makan == "y" or pesan_makan == "Y":
        print("")
        print("="*40)
        print("Anda Memesan : ",gelas, jenis, ">> Rp.",total)
        print("               ",porsi, jenis2, ">> Rp.",total_mkan)
        print("")
        totalSemua = total + total_mkan
        print("=> Total yang harus Dibayar: Rp", totalSemua )
        try:
            tunai = int(input("=> Jumlah Uang Tunai Pembeli : Rp."))
        except ValueError:
            print("Inputan Hanya Berupa Angka... Tidak Boleh Huruf atau yang lain.. Coba Lagi!!")
            pembayaran()
        if tunai < totalSemua:
            print("!!! Maaf Uang anda kurang !!! Silahkan Coba Lagi")
            pembayaran()
    elif pesan_makan == "t" or pesan_makan == "T":
        print("")
        print("Anda Memesan : ",gelas, jenis, ">> Rp.",total)
        totalSemua1 = total
        print("=> Total yang harus Dibayar: Rp", totalSemua1 )
        try:
            tunai = int(input("=> Jumlah Uang Tunai Pembeli : Rp."))
        except ValueError:
            print("Inputan Hanya Berupa Angka... Tidak Boleh Huruf atau yang lain.. Coba Lagi!!")
            pembayaran()
        if tunai < totalSemua1:
            print("!!! Maaf Uang anda kurang !!! Silahkan Coba Lagi")
            pembayaran()

pembayaran()

def kembalian():
    global totalSemua
    global totalSemua1
    global kembalian
    global tunai
    if pesan_makan == "y" or pesan_makan == "Y":
        kembalian = int(tunai - totalSemua)
        print("=> Kembalian Uang : Rp.", kembalian)
        print("")
    elif pesan_makan == "t" or pesan_makan == "T":
        kembalian = int(tunai - totalSemua1)
        print("=> Kembalian Uang : Rp.", kembalian)
        print("")
kembalian()

def struk():
    global tunai
    global kembalian
    global porsi
    if pesan_makan == "y" or pesan_makan == "Y":
        print("============================================")
        print("=========== S T R U K   B E L I ============")
        print("============================================")
        from datetime import datetime
        now = datetime.now()
        week = get_week_day(now)
        print("|> Hari Pembayaran =", week)
        current_date = now.strftime("%Y-%m-%d")
        print("|> Tanggal pembayaran =",current_date)
        current_time = now.strftime("%H:%M:%S")
        print("|> Jam pembayaran =", current_time)
        print("============================================")
        print(" Nama         :", username)
        print(" Beli         :", gelas, jenis, "-","Rp.", total)
        print("               ", porsi, jenis2, "-","Rp.", total_mkan)
        print(" Tagihan      : Rp.", totalSemua)
        print("<------------------------------------------>")
        print(" Uang         : Rp.", tunai)
        print(" Kembalian    : Rp.", kembalian)
        print("<------------------------------------------>")
        print("       TERIMAKASIH TELAH MEMBELI MINUM DI")
        print("                KEDAI QONA'AH")
        print("============================================")
        print("============================================")

    elif pesan_makan == "t" or pesan_makan == "T":
        print("========================================")
        print("========= S T R U K   B E L I ==========")
        print("========================================")
        from datetime import datetime
        now = datetime.now()
        week = get_week_day(now)
        print("|> Hari Pembayaran =", week)
        current_date = now.strftime("%Y-%m-%d")
        print("|> Tanggal pembayaran =",current_date)
        current_time = now.strftime("%H:%M:%S")
        print("|> Jam pembayaran =", current_time)
        print("========================================")
        print(" Nama         :", username)
        print(" Beli         :", gelas, jenis, "-","Rp.", total)
        print("               ","Anda tidak memesan makan")
        print(" Tagihan      : Rp.", totalSemua1)
        print("<-------------------------------------->")
        print(" Uang         : Rp.", tunai)
        print(" Kembalian    : Rp.", kembalian)
        print("<------------    -------------------------->")
        print("   TERIMAKASIH TELAH MEMBELI MINUM DI")
        print("             KEDAI QONA'AH")
        print("========================================")
        print("========================================")

struk()
