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
11. Jalankan Locust.io
12. Buka Locust.io di alamat http://localhost:8089
13. Klik Start
14. Atur parameter
15. Klik Start
16. Jika selesai maka klik Download
17. Klik Download Report
18. Klik tulisan Download Report di kanan atas
19. Evaluasi hasil tes
