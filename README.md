# Mendapatkan tubes assessment dari csv penilaian siswa

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
berbeda, misal tabel email ga dipake atau indexnya beda, di tabel constant ganti
indeksnya ke indeks yg sesuai, misal tabel yg gapenting (kyk email sm timestamp)
ga kepake, kasih indeks asal aja (gabakal ngaruh sama hasil akhir)

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
