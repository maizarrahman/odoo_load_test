# odoo_load_test
Tes Beban Absensi Kehadiran Odoo Menggunakan Locust.io

1. Aktifkan Odoo
2. Buat database baru di Odoo
3. Masuk ke database baru tersebut
4. Impor res.users.csv
5. Impor hr.employee.csv
6. Buat python virtual environment untuk meng-install Locust.io

       python3 -m venv locust

8. Aktifkan python virtual environment tersebut
9. Install Locust.io, OdooLocust, dan Odoo Client Library
10. Edit file attend.py
11. Edit file odoo_stat.sh
12. Buat cron schedule per menit untuk odoo_stat.sh
13. Jalankan Locust.io
14. Buka Locust.io di alamat http://localhost:8089
15. Klik Start
16. Atur parameter
17. Klik Start
18. Jika selesai maka klik Download
19. Klik Download Report
20. Klik tulisan Download Report di kanan atas
21. Evaluasi hasil tes
