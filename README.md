# odoo_load_test
Tes Beban Absensi Kehadiran Odoo Menggunakan Locust.io

1. Aktifkan Odoo
2. Buat database baru di Odoo
3. Masuk ke database baru tersebut
4. Install modul Employee
5. Impor res.users.csv ke data Users
6. Impor hr.employee.csv ke data Employee
7. Buat python virtual environment untuk meng-install Locust.io

       python3 -m venv locust

8. Aktifkan python virtual environment tersebut

       source locust/bin/activate
   
10. Install Locust.io, OdooLocust, dan Odoo Client Library

        pip3 install locust OdooLocust odoo-client-lib
    
12. Sesuaikan port, database, login, dan password di file attend.py dengan pengguna administrator Odoo yang digunakan
13. Ubah dbname di file odoo_stat.sh dengan nama database baru dari nomor 2.
14. Buat jadwal eksekusi per menit untuk odoo_stat.sh menggunakan Linux cron

        (crontab -l; echo '* * * * *  bash odoo_stat.sh') | crontab
    
16. Jalankan Locust.io

        locust -u 20 -r 2 -t 300 -f attend.py
    
17. Buka Locust.io di alamat http://localhost:8089
18. Klik Start
19. Atur parameter
20. Klik Start
21. Jika selesai maka klik Download
22. Klik Download Report
24. Klik tulisan Download Report di kanan atas
25. Evaluasi hasil tes

File attend_seprate_login.py berisi skenario tes bahwa setiap user selalu login menggunakan akunnya sendiri.

