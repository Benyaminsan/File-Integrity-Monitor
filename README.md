# Tugas Kelompok dibawa pulang
 
Kamu diminta membangun sistem deteksi integritas file dan aktivitas mencurigakan sederhana menggunakan bahasa Python / Node.js (boleh bahasa lain dengan izin dosen).

Sistem ini akan:

1. Memantau folder (misal ./secure_files/) untuk mendeteksi jika ada file yang:
- Diubah
- Dihapus
- Ditambahkan
  
2. Memverifikasi integritas file
- Simpan baseline hash setiap file (misal di hash_db.json).
- Setiap kali dijalankan, sistem membandingkan hash saat ini dengan baseline.
- Jika berbeda → catat peringatan di log dan kirim alert (simulasi, misal print ke konsol atau kirim email dummy).
  
3. Melakukan logging yang komprehensif
- Setiap aktivitas (normal maupun mencurigakan) dicatat ke file security.log dalam format:
```
[2025-10-30 13:25:11] INFO: File "config.json" verified OK.
[2025-10-30 13:26:02] WARNING: File "data.txt" integrity failed!
[2025-10-30 13:27:15] ALERT: Unknown file "hacked.js" detected.
```
- Log minimal mengandung: timestamp, level, pesan, nama file.
- Gunakan level logging: INFO, WARNING, ALERT.

3. Simulasi Monitoring
- Tambahkan fitur sederhana untuk membaca security.log dan menampilkan:
  
  -> Jumlah file yang aman

  -> Jumlah file rusak

  -> Waktu terakhir ada anomali

- Bonus (opsional): buat versi web mini (Flask/Express) untuk menampilkan hasil pemantauan.

Hasil Running Program
![WhatsApp Image 2025-11-05 at 9 00 45 PM](https://github.com/user-attachments/assets/5bd2e946-8035-46c0-909d-52c1fd96ed3c)


<img width="1158" height="900" alt="image" src="https://github.com/user-attachments/assets/2eacf053-8cd7-499b-8458-173c314d9915" />


<img width="982" height="731" alt="image" src="https://github.com/user-attachments/assets/0941382a-a7f9-4ae4-bc14-bd1a6da0a26e" />


