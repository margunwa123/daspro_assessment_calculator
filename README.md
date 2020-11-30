# Mendapatkan self dan peer assessment dari csv penilaian siswa

| timestamp  | Email            | NIM(sendiri) | self_assessment | NIM(teman1) | assessment1 | NIM(teman2) | assessment2 | ... |
| ---------- | ---------------- | ------------ | --------------- | ----------- | ----------- | ----------- | ----------- | --- |
| 23-05-2019 | abc.gmail.com    | 13519111     | 90              | 13519223    | 25          | ...         | ...         | ... |
| 23-07-2019 | cda.gmail.com    | 13519113     | 40              | 13519221    | 55          | ...         | ...         | ... |
| 23-12-2019 | dsadsa.gmail.com | 13519112     | 20              | 13519222    | 35          | ...         | ...         | ... |

Gunanya buat apa? Bayangin misal ada data di excel kyk tabel di atas, maka kita
bisa secara manual ngitung rata" peer dari masing masing siswa, tapi ribet
banget atau bikin rumus di google sheet, (harusnya sih gitu, tapi urang gabisa).
Maka program ini akan nerima input file csv (donlot dr google sheet, bentuknya
csv), lalu bakal ngerata ratain nilai peer assessment dari suatu orang berdasar
assessment teman temannya

## Yg perlu diinstal:

- python 3
- modul: csv, re, dataclassess (kyknya mah udh disediain sm pythonnya)

## Asumsi

| timestamp  | Email            | NIM(sendiri) | self_assessment | NIM(teman1) | assessment1 | ... |
| ---------- | ---------------- | ------------ | --------------- | ----------- | ----------- | --- |
| 23-05-2019 | abc.gmail.com    | 13519111     | 90              | 13519223    | 25          | ... |
| 23-07-2019 | cda.gmail.com    | 13519113     | 40              | 13519221    | 55          | ... |
| 23-12-2019 | dsadsa.gmail.com | 13519112     | 20              | 13519222    | 35          | ... |

**tabel penilaian seperti diatas ini:** (diambil dari gsheet)<br/> bila ada yang
berbeda, misal tabel email ga dipake atau indexnya beda, di constant.py ganti
nilai variabel ke indeks yg sesuai, misal tabel yg gapenting (kyk email sm
timestamp) ga kepake, kasih indeks asal aja (gabakal ngaruh sama hasil akhir)

### intinya, misal indeks beda, ganti di constant.py tapi jangan hapus variabelnya

### Di contoh diatas indeks MULAI_NIM_TEMEN adalah ke 4 (mulai dari 0 indeksnya)

## Cara menggunakan

## 1. Self Assessment

py self_assessment.py {namafile.csv} {list of nim}<br/> contoh: py
self_assessment.py penilaian.csv 13518114,1232233,1522222<br/> py
self_assessment.py penilaian.csv 13517121<br/>

## 2. Peer assessment

py peer_assessment.py {namafile.csv} {list of nim}<br/> contoh sama kyk self
assessment

## Output

Contoh output berupa teks, misalnya:<br/> Peer assessment: <br>

```
Rata rata nilai dari peer NIM 18219019 adalah 15.0
```

Self assessment: <br>

```
Self assessment nim 18219019 adalah 19
```

## Kontribusi

Kontribusi anda untuk meningkatkan performa dan kode dari program ini akan
sangat diapresiasi, silahkan melakukan pull request dan bisa contact id line
mariogunawan1 atau instagram @mariogunawan1
