## Bab.6 Module

Python memiliki cara untuk meletakkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter. File seperti itu disebut module; definisi dari modul dapat imported ke modul lain atau ke modul main

Modul adalah file yang berisi definisi dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran .py diakhirnya. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global.

Sebagai Contohnya dengan membuat file fibo.py di direktori saat ini dengan source code berikut : 

```python
# Fibonacci numbers module

def fib(n):     # write Fibonacci series up to n
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # return Fibbonaci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Lalu masukkan interpreter Python dan impor modul ini dengan perintah berikut :

```python
import fibo
```

Ini tidak memasukkan nama fungsi yang didefinisikan dalam fibo secara langsung tetapi hanya memasukkan nama modul fibo saja.

Menggunakan nama modul Anda dapat mengakses fungsi :

```python
fibo.fib(1000)

fibo.fib2(100)

fibo.__name__
```

atau

```python
fib = fibo.fib

fib(500)
```

### 6.1 lebih lanjut tentang Modul

Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya first kali nama modul ditemui dalam pernyataan impor.

Setiap modul memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul.

Modul dapat mengimpor modul lain. Biasanya, tidak diperlukan untuk menempatkan semua pernyataan import di awal modul. Ada varian dari pernyataan import yang mengimpor nama dari modul langsung ke tabel simbol modul impor. Sebagai contoh :

```python
from fibo import fib, fib2

fib(500)
```

atau varian untuk mengimpor semua nama yang didefinisikan oleh modul :

```python
from fibo import *

fib(500)
```

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (_). Secara umum mengimpor * dari modul atau paket tidak disukai, karena sering menyebabkan kode yang kurang dapat dibaca.

Jika nama modul diikuti oleh as, maka nama setelah as terikat langsung ke modul yang diimpor.

```python
import fibo as fib

fib.fib(500)
```

Secara efektif mengimpor modul dengan cara yang sama dengan import fibo akan dilakukan, dengan satu-satunya perbedaan adalah sebagai fib.

Dapat juga digunakan ketika menggunakan from dengan efek yang sama.

```python
from fibo import fib as fibonacci

fibonacci(500)
```

#### 6.1.1 Mengoperasikan Modul Sebagai Skrip

Ketika program :
```
python fibo.py <arguments>
```

Maka kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__ diatur ke "__main__". Itu berarti bahwa dengan menambahkan kode ini di akhir program modul :

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Anda dapat membuat berkas dapat digunakan sebagai skrip dan juga modul yang dapat diimpor, karena kode yang mengurai parsing baris perintah hanya beroperasi jika modul dieksekusi sebagai berkas "main":

```
$ python fibo.py 50
```

Jika modul diimpor, maka program diatas tidak dioperasikan.

#### 6.1.2 Jalur Pencarian Modul

Ketika sebuah modul bernama spam diimpor, interpreter pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, ia kemudian mencari berkas bernama spam.py dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini :

* Direktori yang berisi skrip masukan.

* PYTHONPATH.

* Default instalasi dependent.

#### 6.1.3 Berkas Python "Compiled"

Untuk mempercepat memuat modul, Python menyimpan cache versi terkompilasi dari setiap modul di direktori __pycache__ dengan nama module. version.pyc, di mana versi menyandikan format berkas terkompilasi; umumnya berisi nomor versi Python.

Python tidak akan memeriksa *cache* dalam dua keadaan. 

  - Selama mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah.
  
  - Tidak memeriksa *cache* jika tidak ada modul sumber untuk mendukung distribusi non-sumber (hanya dikompilasi), modul yang dikompilasi harus berada di direktori sumber dan tidak boleh ada sumber modul. 

### 6.2 Modul Standar

Python dilengkapi dengan pustaka modul standar. Beberapa modul dibangun ke dalam interpreter yang menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti pemanggilan sistem. Himpunan modul tersebut adalah opsi konfigurasi yang juga tergantung pada platform yang mendasarinya.

```python
import sys

sys.ps1

sys.ps2

sys.ps1 = 'C> '
```

Variabel sys.path adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan PYTHONPATH, atau dari bawaan bawaan jika PYTHONPATH tidak disetel. Dapat di modifikasi menggunakan operasi standar untuk list :

```python
import sys

sys.path.append('/ufs/guido/lib/python')
```

### 6.3 Fungsi dir()

Fungsi bawaan dir() digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul. Ia mengembalikan list string yang diurutkan. Sebagai contohnya : 

```python
import fibo, sys

dir(fibo)

dir(sys) 
```

Tanpa argumen, dir( ) mencantumkan nama yang telah ditentukan saat ini :

```python
a = [1, 2, 3, 4, 5]

import fibo

fib = fibo.fib
dir()
```

Jika ingin daftar nama fungsi dan variabel bawaan didefinisikan dalam modul standar __builtins__:

```python
import builtins

dir(builtins)  
```

### 6.4 Packages

Packages atau paket adalah cara penataan namespace modul Python dengan menggunakan "dotted module names". Sebagai contoh, nama modul A.B menetapkan submodule bernama B dalam sebuah paket bernama A.

Sebagai contoh jika ingin merancang koleksi modul ("paket") untuk penanganan berkas suara dan data suara yang seragam. Didalam paket tersebut terdapat begitu banyak format file untuk ragam suara yang berbeda, terdapat berbagai operasi berbeda yang mungkin ingin Anda lakukan pada data suara seperti mencampur, menambahkan gema,dll. Untuk mengatasinya adalah dengan membuat koleksi modul yang terus bertambah untuk konversi antara berbagai format file yang ada.

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat mengimpor paket, Python mencari melalui direktori pada sys.path mencari subdirektori paket. Berkas `__init__.py` diperlukan untuk membuat Python memerlakukan direktori yang berisi file sebagai paket.

Contoh mengimport modul individual dari paket :

```python
import sound.effects.echo
```

Perintah tersebut akan memuat submodule sound.effects.echo. Itu harus dirujuk dengan nama lengkapnya.

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

atau

```python
from sound.effects import echo
```

Perintah tersebut akan memuat submodul :mod: echo, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut :

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

atau mengimpor fungsi atau variabel yang diinginkan secara langsung :

```python
from sound.effects.echo import echofilter
```

Perintah tersebut memuat submodul echo, tetapi ini membuat fungsinya echofilter() langsung tersedia :

```python
echofilter(input, output, delay=0.7, atten=4)
```

Ketika menggunakan from package import item, item tersebut dapat berupa submodul (atau subpaket) dari paket, atau beberapa nama lain yang ditentukan dalam paket, seperti fungsi, kelas atau variabel.

Ketika menggunakan sintaksis seperti import item.subitem.subsubitem, setiap item kecuali yang terakhir harus berupa paket; item terakhir dapat berupa modul atau paket tetapi tidak bisa berupa kelas atau fungsi atau variabel yang didefinisikan dalam item sebelumnya.

#### 6.4.1 Mengimpor * Dari Paket

Mengimpor submodul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika submodul diimpor secara eksplisit. Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks paket secara eksplisit. Pernyataan import menggunakan konvensi berikut : jika suatu paket punya kode `__init __.py` yang mendefinisikan daftar bernama `__all__`, itu diambil sebagai daftar nama modul yang harus diimpor ketika from package import * ditemukan.

Sebagai contoh berkas sound/effects/`__init__.py` dapat berisi kode berikut :

```python
__all__ = ["echo", "surround", "reverse"]
```

Maka from sound.effects import * akan mengimpor tiga submodul bernama dari paket sound.

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

Modul echo dan surround diimpor dalam namespace saat ini karena mereka didefinisikan dalam paket sound.effects ketika paket from...import Pernyataan dieksekusi.

Meskipun modul-modul tertentu dirancang hanya untuk mengekspor nama-nama yang mengikuti pola tertentu ketika menggunakan import *, masih dianggap hal yang buruk dalam lingkungan kode produksi production.

Tidak ada yang salah dengan menggunakan from package import specific_submodule! Sebenarnya, ini adalah notasi yang disarankan kecuali modul impor perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.

#### 6.4.2 Referensi Intra-paket

Ketika paket disusun menjadi subpaket, kita dapat menggunakan impor absolut untuk merujuk pada submodul paket saudara kandung.

Kita juga dapat menulis impor relatif, dengan bentuk from module import name pada pernyataan impor. Impor ini menggunakan titik-titik di awalan untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif.

Sebagai contoh pada modul surround : 

```python
from . import echo
from .. import formats
from .. filters import equalizer
```

#### 6.4.3 Paket di Beberapa Direktori

Paket mendukung satu atribut khusus, `__path__`. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan file paket: `__init__.py` sebelum kode dalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi yang hasilnya dapat memengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket.