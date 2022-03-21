# Bab 8 Errors & Exceptions
Pada Python terdapat 2 jenis pesan kesalahan yaitu `Error` dan `Exception`.

## 8.1 Syntax Error

Syntax `Error` atau yang bisa disebut dengan `parsing` adalah suatu keadaan saat kode python mengalami kesalahan penulisan. Python interpreter dapat mendeteksi kesalahan ini saat kode dieksekusi.

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

`Parser` mengulangi baris penyinggung dan menampilkan 'tanda panah' kecil yang menunjuk pada titik paling awal saat kesalahan terdeteksi. Pada contoh diatas, kesalahan terdeteksi pada fungsi `print()`, karena titik dua `:`. Nama file dan nomor baris dicetak sehingga kita tahu letak pasti kesalahannya.

## 8.2 Exceptions

`Exception` adalah kesalahan yang terdeteksi saat eksekusi berlangsung. Kesalahan yang di maksud seperti kesalahan nama function, library, dan lainnya. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilka pesan kesalahan seperti contoh berikut :

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Pada baris akhir program tersebut terdapat pesan kesalahan yang menunjukkan kesalaham apa yang terjadi. Tersapat berbagai jenis pengecualian, dan tipe yang dicetak sebagai bagian dari pesan. Contohnya dalam program yakni `ZeroDivisionError`, `NameError` dan `TypeError`. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Hal ini berlaku untuk semua jenis pengecualian bawaan, tetapi tidak harus sama untuk pengecualian yang dibuat pengguna. Nama pengecualian standar adalah pengindentifikasi bawaan bukan `reserved keyword`.

Penjelasan tentang `Exception` pada program di atas:
  * ZeroDivisonError adalah exception yang terjadi saat eksekusi program menghasilkan perhitungan matematika pembagian dengan angka nol.
  * NameError adalah exception yang terjadi saat kode mengeksekusi terhadap local name atau global name yang tidak terdefinisi. Misalnya saat menjumlahkan variabel yang tidak didefinisikan, memanggil function yang tidak ada, dan lain-lain.
  * TypeError adalah exception yang terjadi saat dilakukan eksekusi terhadap suatu operasi atau fungsi dengan tipe objek yang tidak sesuai.

Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana pengecualian terjadi, dalam bentuk `traceback stack`.

## 8.3. Handling Exceptions

`Handling Exceptions` merupakan mekanisme penanganan untuk menulis program pengecualian yang dipilih. Pada contoh berikut memungkinkan pengguna untuk menghentikan program (menggunakan Control-C tergantung sistem operasinya). Kesalahan masukan yang dibuat pengguna ditandai dengan munculnya pengecualian `KeyboardInterrupt`.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pernyataan `try` berfungsi sebagai berikut:
  * Pertama, `try clause` (pernyataan-pernyataan) di antara kata kunci `try` dan `except` dieksekusi.
  * Jika tidak ada pengecualian yang terjadi, `except clause` dilewati dan mengeksekusi pernyatan keyword `try` kemudian selesai.
  * Jika pengecualian terjadi selama eksekusi `try clause`, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci `except`, klausa `except` dijalankan, dan kemudian eksekusi dilanjutkan setelah blok `continues` atau `except`.
  * Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam `except clause`, hal itu akan diteruskan ke pernyataan percobaan luar; jika tidak ada penanganan yang ditemukan, hal tersebut adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan `try` mungkin memiliki lebih dari satu `except clause`, untuk menentukan penanganan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Handler hanya menangani pengecualian yang terjadi di klausa `try` yang sesuai, bukan di handler lain dari pernyataan `try` yang sama. Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tuple dalam kurung, misalnya:

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

Kelas dalam `except clause` kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar (tetapi tidak sebaliknya, `except clause` yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan tersebut :

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Jika `except clause` dibalik (dengan kecuali B terlebih dahulu), akan mencetak B, B, B.

Semua pengecualian mewarisi dari `BaseException`, sehingga dapat digunakan sebagai `wildcard`. 

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Sebagai alternatif, klausa pengecualian dapat menghilangkan nama pengecualian, namun nilai pengecualian harus diambil dari `sys.exc_info()[1]`.

Pernyataan `try ... except` memiliki klausa `else` opsional, yang jika muncul harus mengikuti semua `except clause`. Berguna untuk kode yang harus dijalankan jika klausa `try` tidak memunculkan eksepsi. Sebagai contoh :

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan klausa `else` lebih baik daripada menambahkan kode tambahan ke klausa `try` karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan `try ... :keyword: !except`.

Klausa `except` dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke instance pengecualian dengan argumen yang disimpan di `instance.args.` Untuk kenyamanan, instance pengecualian mendefinisikan `__str__()` sehingga argumen dapat dicetak secara langsung tanpa harus merujuk ke `.args.`. Juga dapat membuat instance pengecualian terlebih dahulu sebelum menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika pengecualian memiliki argumen, mereka dicetak sebagai bagian terakhir dari pesan untuk pengecualian yang tidak ditangani. Pengendali pengecualian tidak hanya menangani pengecualian jika terjadi di klausa `try`, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam klausa `try`. Sebagai contoh:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4 Raising Exceptions

Pernyataan `raise` memungkinkan untuk memaksa pengecualian untuk muncul. Sebagai contoh :

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Jika kelas pengecualian diteruskan, maka kelas tersebut akan secara implisit diinstansiasi dengan memanggil `constructor` tanpa argumen :

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Jika kita ingin menentukan apakah pengecualian harus dimunculkan tetapi kita juga tidak ingin menanganinya, maka kita bisa menggunakan bentuk sederhana dari statement `raise` untuk memunculkan ulang sebuah pengecualian :

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5 Exception Chaining

Pernyataan `raise` memperbolehkan opsional yang memungkinkan pengecualian berantai. Sebagai contoh :

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

Hal tersebut bisa berguna ketika kita men-transformasi pengecualian. Sebagai contoh :

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dimunculkan di dalam sebuah `except` atau `finally` bagian. Hal ini dapat dinonaktifkan dengan menggunakan `from None idiom` :

```python
>>> try:
...    open('database.sqlite')
... except OSError:
...    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

## 8.6 User-defined Exceptions

Program dapat memberi nama `Exception` mereka sendiri dengan membuat kelas `Exception` baru. `Exception` biasanya berasal dari kelas `Exception`, baik secara langsung atau tidak langsung.

`Exception classes` bisa didefinisikan dan bisa melakukan apapun yang kelas lain bisa lakukan, tetapi biasanya lebih sederhana. Biasanya `exception classes` hanya menyediakan kumpulan atribut yang memungkinkan informasi `error` diekstrak oleh handler untuk `exception`.

Banyak modul standar bisa mendefinisikan `exception` untuk melaporkan error yang muncul di dalam fungsi yang telah didefinisikan.

## 8.7 Defining Clean-up Actions

Statement `try` memiliki klausa opsional lain yang digunakan untuk mendefinisikan tindakan pembersihan yang harus dieksekusi di segala kondisi. Sebagai contoh :

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Klausa `finally` akan dieksekusi sebagai perintah terakhir sebelum statemen `try` selesai dieksekusi. Klausa `finally` berjalan saat statement `try` memproduksi ataupun juga saat tidak memproduksi sebuah pengecualian. Berikut beberapa poin tentang apa saja yang terjadi saat pengecualian muncul :
  * Jika `Exception` terjadi selama eksekusi klausa untuk `:keyword: !try`, maka pengecualian tersebut dapat ditangani oleh klausa `except`. Jika pengecualian tidak ditangani oleh klausa `:keyword: !except`, maka pengecualian dimunculkan kembali setelah klausa `finally` dieksekusi.* Pengecualian dapat terjadi selama pelaksanaan klausa `except` atau `else`. Sekali lagi, pengecualian akan muncul kembali setelah klausa `finally` telah dieksekusi.
  * Jika klausa last mengeksekusi pernyataan `break`, `continue`, atau `return`, `exception` tidak dimunculkan kembali.
  * Jika pernyataan klausa untuk `try` mencapai klausa `break`, `continue` atau `:keyword: return` maka, pernyataan untuk klausa `finally` akan dieksekusi sebelum `break`, `continue` atau `return` dieksekusi.
  * Jika klausa untuk `:keyword:!finally` telah menyertakan pernyataan `return`, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk `finally` dan dari klausa `return`, bukan nilai dari `try` pernayataan untuk `return`.

Sebagai Contoh:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

Berikut Contoh yang lebih kompleks:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang kita lihat, klausa `finally` dieksekusi dalam peristiwa apa pun. `TypeError` muncul karena ada operasi pembagian dua string yang tidak ditangani oleh klausa `except` sehingga `TypeError` dimunculkan ulang setelah klausa `finally` selesai dieksekusi.

## 8.8 Predefined Clean-up Actions

Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Sebagai contoh program, yang mencoba membuka file dan mencetak ke layar :

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Pada program diatas terdapat masalah karena membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode tersebut selesai dieksekusi. Hal tersebut bukan merupakan masalah dalam script sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih kompleks. Pernyataan `with` memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar. Seperti pada contoh berikut :

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dieksekusi, file `f` selalu ditutup, bahkan ketika masalah ditemukan ketika proses menjalankan kode.