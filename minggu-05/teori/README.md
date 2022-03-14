# Bab.7 Input dan Output (I/O)

Python menyediakan banyak fungsi built-in yang bisa kita pergunakan. Salah satunya adalah yang berkenaan dengan fungsi i/o atau input output. Data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa yang akan datang.

## 7.1. Fancier Output Formatting

Pada python terdapat beberapa cara untuk penulisan nilai yaitu `expression statements` dan fungsi `print()`. Kemudian bisa menggunakan `write()` metode objek file yang merupakan standar keluaran dapat dirujuk sebagai `sys.stdout`.

Ada beberapa cara untuk memformat output seperti:

- Untuk menggunakan `formatted string literals`, mulailah string dengan `f` atau `F` sebelum tanda kutip pembuka atau tanda kutip tiga dan dalam string menulis ekspresi Python antara karakter `{` dan `}` yang dapat merujuk ke variabel atau nilai literal.

    ```python
    >>> year = 2016
    >>> event = 'Referendum'
    >>> f'Results of the {year} {event}'
    'Results of the 2016 Referendum'
    ```

- Metode `str.format()` dari string membutuhkan lebih banyak upaya manual. Metode ini masih  menggunakan `{` dan `}` untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci.

    ```python
    >>> yes_votes = 42_572_654
    >>> no_votes = 43_132_495
    >>> percentage = yes_votes / (yes_votes + no_votes)
    >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
    ' 42572654 YES votes  49.67%'
    ```

- String dengan menggunakan operasi `slicing string` dan `concatenation` untuk membuat tata letak apapun yang dibuat. Tipe string ini memiliki beberapa metode yang melakukan operasi untuk mengisi string ke lebar kolom tertentu.

Untuk keperluan `debugging`, dapat mengonversi nilai apapun menjadi string dengan fungsi `repr()` atau `str()`.

Fungsi `str()` untuk mengembalikan representasi nilai-nilai yang dapat dibaca oleh manusia, dan fungsi  `repr()` untuk menghasilkan representasi yang dapat dibaca oleh penerjemah atau akan memaksa `SyntaxError` jika tidak ada sintaks yang setara. 

Contoh :

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```


### 7.1.1 Formatted String Literals

Pada `Formatted string literals` atau disebut juga f-string, memungkinkan untuk menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan `f` atau `F` dan menulis ekspresi sebagai `{expression}`.

Contoh berikut ini pembulatan pi ke tiga tempat setelah desimal :

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

Melewatkan bilangan bulat setelah `:` akan menyebabkan field itu menjadi jumlah karakter minimum, yang berguna untuk membuat kolom berbaris.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

Pengubah lain yang dapat digunakan untuk mengonversi nilai sebelum diformat. `!a` berlaku untuk `ascii()`, `!s` berlaku untuk `str()`, dan `!r` berlaku untuk `repr()`, seperti contoh berikut :

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

### 7.1.2 The String format() Method

Pada penggunaan metode `str.format()` akan seperti ini:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dan karakter yang terdapat di dalamnya disebut fields format, diganti dengan objek yang diteruskan ke metode `str.format()`. Angka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam metode `str.format()`.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

Jika `keyword argument` digunakan dalam metode `str.format()`, nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
Posisi argument dan kata kunci dapat dikombinasikan :

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

Jika memiliki string format yang sangat panjang dan tidak ingin dipisahkan, untuk mereferensikan variabel yang akan diformat berdasarkan nama bukan berdasarkan posisi, dapat dilakukan dengan melewatkan dict dan menggunakan tanda kurung siku `[]` untuk mengakses kuncinya.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Juga bisa dilakukan dengan meneruskan tabel sebagai argumen kata kunci `keyword argument` dengan notasi `**`.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Juga sangat berguna dalam kombinasi dengan fungsi bawaan `vars()`, yang mengembalikan dictionary yang berisi semua variabel lokal.

Sebagai contoh :

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

### 7.1.3 Manual String Formatting

Berikut ini tabel kotak dan kubus yang sama, dan di format secara manual :

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Metode `str.rjust()` dari objek string membuat rata kanan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri. Ada metode serupa `str.ljust()` dan `str.center()`. Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah.

Ada metode lain, `str.zfill()`, yang melapisi string numerik di sebelah kiri dengan nol. Pada metode ini bisa menggunakan tanda plus dan minus :

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4 Old string formatting

Operator `%` (modulo) dapat digunakan untuk pemformatan string. Operasi ini juga dikenal sebagai interpolasi string. 

Sebagai Contoh :

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

## 7.2 Reading and Writing Files

Fungsi metode `open()` mengembalikan sebuah `file object`, dan  sering digunakan dengan dua argumen, antara lain : `open(filename, mode)`.

```python
>>> f = open('workfile', 'w')
```

Dalam kode di atas di Argumen `pertama` adalah string yang berisi nama file. Kemudian Argumen `kedua` adalah string lain yang berisi beberapa karakter yang menggambarkan cara berkas akan digunakan. Setiap data yang ditulis secara otomatis ditambahkan ke bagian akhir.

Menggunakan `with` jauh lebih pendek daripada penulisan yang setara `try-blok finally` :

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

Jika kita tidak menggunakan kata kunci `with`, maka kita harus memanggil `f.close()` untuk menutup file secara langsung.

Setelah objek file ditutup, baik dengan pernyataan `with` atau dengan memanggil `f.close()`, upaya untuk menggunakan objek file akan secara otomatis gagal.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 7.2.1 Methods of File Objects 

Untuk membaca konten file bisa dengan memanggil `f.read(size)`, yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). Ketika size/ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan, Jika akhir file telah tercapai, `f.read()` akan mengembalikan string kosong `('')`.

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

`f.readline()` akan membaca satu baris dari file, karakter baris baru `(\n)` dibiarkan di akhir string, dan hanya dihapus pada baris terakhir file jika file tidak berakhir pada baris baru.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, dapat menggunakan perulangan sehingga menghemat memori, cepat, dan mengarah ke kode sederhana, contoh :

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

Jika ingin membaca semua baris file dalam daftar, dapat menggunakan `list(f)` atau `f.readlines()`. Kemudian `f.write(string)` menulis konten string ke file,dan mengembalikan jumlah karakter yang ditulis.

```python
>>> f.write('This is a test\n')
15
```

Jenis objek lain perlu dikonversi baik menjadi string dalam mode teks atau objek byte dalam mode biner, contoh :

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

`f.tell()` mengembalikan integer yang memberikan posisi objek file ketika dalam mode biner dan angka buram `opaque` ketika dalam mode teks.

Untuk mengubah posisi objek file, gunakan `f.seek(offset, whence)`. 
Posisi dihitung dari menambahkan offset ke titik referensi. Titik referensi dipilih oleh argumen `whence`.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```
Dalam file teks, hanya mencari relatif dari awal file yang diizinkan. Nilai offset lainnya menghasilkan nilai yang tidak terdefinisi.

### 7.2.2 Saving structured data with json


String dapat dengan mudah ditulis dan dibaca, sedangkan angka membutuhkan lebih banyak usaha, karena read metode ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int, yang mengambil string '123' dan mengembalikan nilai numeriknya 123.

Dari pada terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke berkas, Python memungkinkan kita untuk menggunakan format pertukaran data populer yang disebut dengan `JSON` . Modul standar bernama `json` dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string. Proses ini disebut serializing. Kemudian Merekonstruksi data dari representasi string disebut deserializing. 

Jika kita memiliki objek `x`, kita dapat melihat representasi string `JSON` dengan baris kode sederhana, contoh :

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Fungsi `dump()` akan membuat serial objek menjadi `:term:` text file. Jadi jika `f` adalah objek text file untuk menulis, maka dapat menggunakan code berikut ini :

```python
json.dump(x, f)
```

Untuk memecahkan kode objek, jika `f` adalah objek text file yang telah dibuka untuk membaca :

```python
x = json.load(f)
```

Teknik serialisasi sederhana ini dapat menangani daftar list dan dictionary, tetapi membuat serialisasi yang berubah-ubah pada `JSON` akan memakan tenaga dan waktu extra.