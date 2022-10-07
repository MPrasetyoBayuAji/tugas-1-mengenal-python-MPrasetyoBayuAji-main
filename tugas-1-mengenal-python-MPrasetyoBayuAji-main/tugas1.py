"""
Modul ini berisi fungsi-fungsi tugas 1.
Implementasikan fungsi-fungsi tersebut di bawah ini yang masih kosong,
yaitu fungsi yang memiliki komentar TODO.
"""
import math
from operator import truediv
from re import L


def ucap_salam():
    """Fungsi untuk menampilkan salam.

    Contoh:
        >>> ucap_salam()
        "Assalamu'alaikum"

    Returns:
        str: salam
    """

    return "Assalamu'alaikum"


def beri_salam(nama):
    """Fungsi untuk memberikan salam ke nama seseorang.

    Contoh:
        >>> beri_salam("Budi")
        "Assalamu'alaikum, Budi"
        >>> beri_salam("Andi")
        "Assalamu'alaikum, Andi"

    Args:
        nama (str): nama
    Returns:
        str: salam
    """

    return f"{ucap_salam()}, {nama}"


def cek_ganjil_genap(*angka):
    angka = angka[0]
    if angka % 2 == 0 :
        return ("genap")
    else : 
        return ("ganjil")
    """Fungsi untuk mengecek apakah angka ganjil atau genap.

    Contoh:
        >>> cek_ganjil_genap(1)
        'ganjil'
        >>> cek_ganjil_genap(2)
        'genap'

    Args:
        angka (int): angka
    Returns:
        str: 'ganjil' jika angka ganjil, 'genap' jika angka genap
    """
    # TODO: implementasikan fungsi ini


def cek_tahun_kabisat(*tahun):
    tahun = tahun[0]
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else : 
        return False
    """
    Fungsi untuk mengecek apakah tahun kabisat atau bukan.
    Aturan tahun kabisat adalah sbb:
    <br >1. Jika angka tahun itu habis dibagi 400, maka tahun itu sudah pasti tahun kabisat.
    <br >2. Jika angka tahun itu tidak habis dibagi 400 tetapi habis dibagi 100, maka tahun itu sudah pasti bukan merupakan tahun kabisat.
    <br >3. Jika angka tahun itu tidak habis dibagi 400, tidak habis dibagi 100 akan tetapi habis dibagi 4, maka tahun itu merupakan tahun kabisat.
    <br >4. Jika angka tahun itu tidak habis dibagi 400, tidak habis dibagi 100, dan tidak habis dibagi 4, maka tahun tersebut bukan merupakan tahun kabisat.

    Contoh:
        >>> cek_tahun_kabisat(2019)
        False
        >>> cek_tahun_kabisat(2020)
        True

    Args:
        tahun (int): tahun
    Returns:
        bool: True jika tahun kabisat, False jika bukan
    """
    # TODO: implementasikan fungsi ini


def hitung_luas_lingkaran(*jari_jari):
    jari_jari = jari_jari[0]
    jari_jari = int(jari_jari)
    luas_lingkaran = math.pi*(jari_jari**2)
    return (float(luas_lingkaran))
    """
    Fungsi untuk menghitung luas lingkaran.
    Guna fungsi math.pi untuk menghitung nilai pi.

    Contoh:
        >>> hitung_luas_lingkaran(5)
        78.53981633974483
        >>> hitung_luas_lingkaran(6)
        113.09733552923255

    Args:
        jari_jari (int): jari-jari lingkaran
    Returns:
        float: luas lingkaran
    """
    # TODO: implementasikan fungsi ini


def hitung_volume_kubus(*panjang_rusuk):
    panjang_rusuk = panjang_rusuk[0]
    panjang_rusuk = int(panjang_rusuk)
    volume_kubus = panjang_rusuk ** 3
    return volume_kubus
    """Fungsi untuk menghitung volume kubus.

    Contoh:
        >>> hitung_volume_kubus(5)
        125
        >>> hitung_volume_kubus(6)
        216

    Args:
        panjang_rusuk (int): panjang rusuk kubus
    Returns:
        int: volume kubus
    """
    # TODO: implementasikan fungsi ini


def hitung_rerata(*list_angka):
    list_angka = list_angka[0]
    n = len(list_angka)
    s = sorted(list_angka)
    return float((s[n//2-1]/2.0 + s[n//2]/2.0, s[n//2])[n%2]if n else None)

    """Fungsi untuk menghitung rerata dari list angka.

    Contoh:
        >>> hitung_rerata([1, 2, 3, 4, 5])
        3.0
        >>> hitung_rerata([1, 2, 3, 4, 5, 6])
        3.5

    Args:
        list_angka (list): list angka
    Returns:
        float: rerata dari list angka
    """
    # TODO: implementasikan fungsi ini


def hitung_huruf_vokal(*kalimat):
    kalimat = kalimat[0]
    kalimat = str(kalimat)
    huruf_vokal = "aiueoAIUEO"
    hitung = 0
    for i in kalimat : 
        if i in huruf_vokal :
            hitung += 1
    return hitung 
    """
    Fungsi untuk menghitung jumlah huruf vokal dalam sebuah kalimat.
    Huruf vokal yang dimaksud bisa huruf kecil maupun huruf besar.

    Contoh:
        >>> hitung_huruf_vokal("Assalamu'alaikum")
        8
        >>> hitung_huruf_vokal("Halo")
        2

    Args:
        kalimat (str): kalimat
    Returns:
        int: jumlah huruf vokal dalam kalimat
    """
    # TODO: implementasikan fungsi ini


def cari_angka_terbesar(list_angka):
    angka = list_angka[0]
    if len(list_angka) > 1 :
        next_angka = cari_angka_terbesar(list_angka[1:])
        if next_angka > angka : 
            angka = next_angka
    return angka 
    """Fungsi untuk mencari angka terbesar dari list angka.

    Contoh:
        >>> cari_angka_terbesar([1, 2, 3, 4, 5])
        5
        >>> cari_angka_terbesar([1, 2, 3, 4, 5, 6])
        6

    Args:
        list_angka (list): list angka integer
    Returns:
        int: angka terbesar dari list angka
    """
    # TODO: implementasikan fungsi ini


def cari_angka_duplikat(*list_angka):
    list_angka = list_angka[0]
    angka = set()
    tambah = angka.add
    angka_double = set(x for x in list_angka if x in angka or tambah(x))
    return list(angka_double)

    """Fungsi untuk mencari angka yang duplikat dalam list angka.

    Contoh:
        >>> cari_angka_duplikat([1, 2, 3, 4, 5])
        []
        >>> cari_angka_duplikat([1, 2, 3, 4, 5, 6, 1, 2, 3])
        [1, 2, 3]
        >>> cari_angka_duplikat([1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 5])
        [1, 4, 5]

    Args:
        list_angka (list): list angka
    Returns:
        list: list angka yang duplikat
    """
    # TODO: implementasikan fungsi ini


def hitung_faktorial(*angka):
    angka = angka [0]
    angka = int(angka)
    if angka > 2 :
        return angka * hitung_faktorial(angka - 1)
    return angka


    """Fungsi untuk menghitung faktorial dari sebuah angka.

    Contoh:
        >>> hitung_faktorial(5)
        120
        >>> hitung_faktorial(6)
        720

    Args:
        angka (int): angka
    Returns:
        int: faktorial dari angka
    """
    # TODO: implementasikan fungsi ini


def hitung_jumlah_setiap_karakter(*kata):
    kata = kata[0]
    freq = {}
    for c in set(kata) :
        freq[c] = kata.count(c)
    return {c: kata.count(c) for c in set(kata)}

    """Fungsi untuk menghitung jumlah setiap karakter dalam sebuah kata.

    Contoh:
        >>> hitung_jumlah_setiap_karakter("Assalamu'alaikum")
        {'a': 4, 's': 2, 'l': 2, 'm': 3, 'u': 2, "'": 1, 'i': 1, 'k': 1}
        >>> hitung_jumlah_setiap_karakter("Haloo")
        {'h': 1, 'a': 1, 'l': 1, 'o': 2}

    Args:
        kata (str): kata
    Returns:
        dict: dictionary dengan key adalah karakter dan value adalah jumlah karakter
    """
    # TODO: implementasikan fungsi ini
