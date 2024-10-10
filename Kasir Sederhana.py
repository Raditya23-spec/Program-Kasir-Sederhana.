pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    RadityaZzz STORE
    List Menu 
    
    ==============================
    a. Kopi Kapal API : Rp 20.000
    b. Pasta Gigi Pepsodent : Rp 15.000
    c. Sabun Muka Garnier : Rp 27.000
    d. Susu Bearbrand  : Rp 10.000
    e. Beras Sania Premium  : Rp 30.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu  ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Kopi Kapal API"
        harga=(20000*jumlahpesan)
        ppn= int(harga * 0.1)
        diskon =(0)
        totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "Pasta Gigi Pepsodent"
        harga = (12000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = (0)
        totalharga =int(harga+ppn)
    elif pesan == "c":
        listnama= "Sabun Muka Garnier"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "Susu Bearbrand"
        harga=int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "e":
        listnama= "Beras Sania Premium"
        harga=int(30000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("RadityaZzz STORE")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")