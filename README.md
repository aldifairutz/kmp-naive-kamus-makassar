Aplikasi Kamus Bahasa Makassar Berbasis String Matching
Proyek ini dikembangkan untuk memenuhi tugas akhir semester mata kuliah Analisis Desain Algoritma. Fokus utama aplikasi ini adalah digitalisasi bahasa Makassar guna melestarikan identitas budaya daerah melalui fitur pencarian kosa kata yang efisien secara luring (offline).
Tim Pengembang
Aldi (105841110023) – Universitas Muhammadiyah Makassar.
Rafli Naufal (105841109823) – Universitas Muhammadiyah Makassar.
Fitur Utama

Pencarian Dua Arah: Mencari kosa kata dari bahasa Makassar ke Indonesia maupun sebaliknya.
Akses Offline: Sistem tidak memerlukan koneksi internet karena menggunakan basis data lokal dalam format CSV.
Perbandingan Algoritma: Implementasi dan komparasi performa antara algoritma Naive dan Knuth-Morris-Pratt (KMP).
Algoritma yang Digunakan1. Naive String MatchingAlgoritma dasar yang memeriksa kecocokan pola dengan menggeser tepat satu karakter ke arah kanan setelah setiap percobaan ketidakcocokan . Memiliki kompleksitas waktu terburuk $O(n \times m)$.2. Knuth-Morris-Pratt (KMP)Algoritma yang lebih cerdas dengan memanfaatkan tabel Longest Prefix Suffix (LPS) untuk menghindari perbandingan karakter yang berulang . Memiliki kompleksitas waktu linear $O(n + m)$
Teknologi yang Digunakan

Bahasa Pemrograman: Python 3.13.
Library: Pandas (Manajemen Data CSV).
Framework: Streamlit (Antarmuka Web).
Instalasi dan Cara Menjalankan
Pastikan Anda telah menginstal Python 3.13.

Instal pustaka yang diperlukan:
pip install pandas streamlit
Jalankan aplikasi melalui terminal:
streamlit run main.py
Hasil PengujianBerdasarkan pengujian pada dataset kamus_makassar.csv, berikut adalah perbandingan kecepatan eksekusi:Kata KunciWaktu Eksekusi (KMP)Waktu Eksekusi (Naive)aba0.000125 Detik0.000382 Detikammenteng0.000140 Detik0.000415 Detik
Kesimpulannya, algoritma KMP terbukti lebih efisien untuk pencarian kosa kata pada dataset teks berukuran besar.
