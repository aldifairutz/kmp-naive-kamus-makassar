import pandas as pd

# ==========================================================
# 1. ALGORITMA NAIVE STRING MATCHING
# ==========================================================
def naive_search(text, pattern):
    """
    Implementasi Naive String Matching sesuai pseudocode:
    Geser pattern dari kiri ke kanan (i = 0..n-m)
    Cocokkan karakter dari kiri ke kanan (j = 0..m-1)
    """
    n = len(text)
    m = len(pattern)
    
    # Loop untuk menggeser pattern (i)
    for i in range(n - m + 1):
        j = 0
        # Loop untuk mencocokkan karakter (j)
        while j < m and text[i + j].lower() == pattern[j].lower():
            j += 1
        
        # Jika j == m, berarti seluruh karakter pola cocok
        if j == m:
            return True
    return False

# ==========================================================
# 2. ALGORITMA KNUTH-MORRIS-PRATT (KMP)
# ==========================================================
def compute_lps(pattern):
    """
    Membangun tabel LPS (Longest Prefix Suffix) sebelum pencarian.
    Menentukan panjang prefix terpanjang yang juga merupakan suffix.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0 
    i = 1
    
    while i < m:
        if pattern[i].lower() == pattern[length].lower():
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Implementasi KMP Search dengan kompleksitas O(n + m).
    Memanfaatkan tabel LPS untuk menghindari perbandingan ulang karakter.
    """
    n = len(text)
    m = len(pattern)
    if m == 0: return False
    
    lps = compute_lps(pattern)
    i = 0  # Indeks untuk Teks (n)
    j = 0  # Indeks untuk Pattern (m)
    
    while i < n:
        if pattern[j].lower() == text[i].lower():
            i += 1
            j += 1
        
        if j == m:
            return True # Pola ditemukan
            j = lps[j - 1] # Persiapan mencari kecocokan berikutnya
        elif i < n and pattern[j].lower() != text[i].lower():
            if j != 0:
                j = lps[j - 1] # Lompat cerdas berdasarkan tabel LPS
            else:
                i += 1
    return False

# ==========================================================
# 3. FUNGSI UTAMA APLIKASI
# ==========================================================
def main():
    try:
        # Load dataset CSV
        file_name = 'kamus_makassar (2).csv'
        df = pd.read_csv(file_name)
        
        print("=== APLIKASI KAMUS BAHASA MAKASSAR ===")
        keyword = input("Masukkan kata yang ingin dicari: ").strip()
        
        print("\nMemilih Metode:")
        print("1. Naive String Matching")
        print("2. KMP (Knuth-Morris-Pratt)")
        pilihan = input("Pilih (1/2): ")
        
        print(f"\n--- Hasil Pencarian untuk '{keyword}' ---")
        found_any = False
        
        for index, row in df.iterrows():
            # Teks (T) adalah data di kolom kamus
            target_mks = str(row['Kata_Makassar'])
            target_ind = str(row['Kata_Indonesia'])
            
            # Melakukan pencarian menggunakan metode terpilih
            is_match = False
            if pilihan == '1':
                is_match = naive_search(target_mks, keyword) or naive_search(target_ind, keyword)
            else:
                is_match = kmp_search(target_mks, keyword) or kmp_search(target_ind, keyword)
            
            if is_match:
                print(f"[{row['Jenis_Kata']}] {row['Kata_Makassar']} = {row['Kata_Indonesia']}")
                print(f"Contoh: {row['Contoh_Kalimat']}\n")
                found_any = True
        
        if not found_any:
            print("Kata tidak ditemukan dalam kamus.")
            
    except FileNotFoundError:
        print("Error: File 'kamus_makassar (2).csv' tidak ditemukan.")

if __name__ == "__main__":
    main()