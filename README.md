# odoo_load_test
Tes Beban Absensi Kehadiran Odoo Menggunakan Locust.io

1. Aktifkan Odoo
2. Buat database baru di Odoo
3. Masuk ke database baru tersebut
4. Impor res.users.csv
5. Impor hr.employee.csv
6. Buat python virtual environment untuk meng-install Locust.io
   ```python3 -m venv locust```
7. Aktifkan python virtual environment tersebut
8. Install Locust.io, OdooLocust, dan Odoo Client Library
9. Edit file attend.py
10. Jalankan Locust.io
11. Buka Locust.io di alamat http://localhost:8089
12. Klik Start
13. Atur parameter
14. Klik Start
15. Jika selesai maka klik Download
16. Klik Download Report
17. Klik tulisan Download Report di kanan atas
18. Evaluasi hasil tes
