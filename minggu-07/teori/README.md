# Bab 9 Classes
Classes menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat sebuah class baru menghasilkan objek dengan type baru, memungkinkan dibuat instance baru dari tipe itu. Setiap instance dari class dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya. Instance dari sebuah class juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi kondisinya.

Mekanisme kelas Python menambah kelas dengan minimum sintaksis dan semantik baru. Mekanisme ini adalah campuran dari mekanisme kelas yang ditemukan dalam C++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek seperti pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat menimpa metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang berubah-ubah. 

## 9.1 Tentang Nama dan Objek

Objek memiliki individualitas, dan banyak nama (dalam berbagai lingkup) dapat terikat ke objek yang sama. Biasanya dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tuple). 

## 9.2 Lingkup Python dan Namespaces

`Namespace` adalah pemetaan dari nama ke objek. Sebagian besar `Namespace` saat ini diimplementasikan sebagai kamus dictionary Python, tetapi biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan. Contoh `Namespace` adalah: himpunan nama bawaan berisi fungsi seperti abs(), dan nama pengecualian bawaan, nama-nama global dalam sebuah modul, dan nama-nama lokal dalam pemanggilan fungsi.

`Namespace` yang berisi nama-nama bawaan dibuat ketika interpreter Python dimulai, dan tidak pernah dihapus. `Namespace` global untuk modul dibuat ketika definisi modul dibaca, biasanya `Namespace` modul juga bertahan hingga interpreter berhenti. Pernyataan yang dieksekusi oleh pemanggilan interpreter, baik membaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut `__main__`, sehingga mereka memiliki `Namespace` global sendiri.

### 9.2.1 Contoh Lingkup dan Namespaces

Contoh yang menunjukkan cara mereferensikan lingkup scopes dan `namespaces` yang berbeda, dan bagaimana global dan nonlocal memengaruhi pengikatan variabel : 

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Output dari kode diatas : 

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## 9.3 Tentang Class

Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

### 9.3.1 Sintaks Definisi Class

Bentuk definisi kelas paling sederhana :

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-2>
```

Definisi kelas, seperti definisi fungsi pernyataan `def` harus dieksekusi sebelum mereka memiliki efek. Kita dapat menempatkan definisi kelas di cabang dari pernyataan `if`, atau di dalam suatu fungsi.

Ketika definisi kelas dimasukkan, namespace baru dibuat, dan digunakan sebagai lingkup scope lokal, semua tugas untuk variabel lokal masuk ke namespace baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.

Ketika definisi kelas dibiarkan normal (melalui akhir), class object dibuat. Ini pada dasarnya adalah pembungkus di sekitar isi namespace yang dibuat oleh definisi kelas; kita akan belajar lebih banyak tentang objek kelas di bagian selanjutnya. Lingkup scope lokal asli yang berlaku tepat sebelum definisi kelas dimasukkan diaktifkan kembali, dan objek kelas terikat di sini dengan nama kelas yang diberikan dalam header definisi kelas

### 9.3.2 Class Objek

Objek kelas mendukung dua jenis operasi yaitu referensi atribut dan instansiasi.

Attribute references menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: `obj.name`. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat.

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

Kelas "MyClass.i" dan "MyClass.f" pada potongan kode diatas adalah referensi atribut yang valid, masing-masing dapat mengembalikan nilai berupa bilangan bulat dan objek fungsi. Atribut kelas juga dapat ditetapkan sehingga dapat diubah nilainya berdasarkan tugas. 

Instansiasi kelas menggunakan notasi fungsi. Saat ini objek kelas didefenisikan sebagai fungsi tanpa parameter yang dapat mengembalikan `instance` baru dari kelas. 

```
x = MyClass()
```

Operasi instansiasi akan memanggil objek kelas sehingga membuat objek kosong. Seringkali terdapat kelas yang suka membuat objek dengan `instance` yang disesuaikan dengan keadaan tertentu. Oleh karena itu, sebuah kelas dapat mendefenisikan metode khusus bernama `__init__()`, berikut contohnya :

```python
>>> class Complex:                          
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
... 
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3 Instance Objek 

Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid yaitu atribut data, dan metode. Jika x adalah turunan dari MyClass yang dibuat di atas, bagian kode berikut akan mencetak nilai 16, contoh penggunaannya adalah :

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

Nama metode yang valid dari objek instance bergantung pada kelasnya. Menurut definisi, semua atribut dari kelas yang merupakan objek fungsi menentukan metode yang sesuai dari instance-nya. Jadi dalam contoh kita, `x.f` adalah referensi metode yang valid, karena `MyClass.f` adalah fungsi, tetapi `x.i` tidak, karena `MyClass.i` tidak. Tetapi `x.f` bukan hal yang sama dengan `MyClass.f`

### 9.3.4 Metode Objek

Dalam contoh MyClass, ini akan mengembalikan string `'hello world'`. Namun, tidak perlu memanggil metode segera. `x.f` adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh :

```python
xf = x.f
while True:
    print(xf())
```

Hal khusus tentang metode adalah objek instance dilewatkan sebagai argumen pertama dari fungsi. Dalam contoh, panggilan `x.f()` persis sama dengan `MyClass.f(x)`. Secara umum, memanggil metode dengan daftar argumen `n` setara dengan memanggil fungsi yang sesuai dengan daftar argumen yang dibuat dengan menyisipkan objek contoh metode sebelum argumen pertama.

### 9.3.5 Variabel Kelas dan Instance

Variabel instance untuk data unik untuk setiap instance dan variabel kelas adalah atribut dan metode yang dibagikan oleh semua instance kelas.

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

Data sharing dapat memiliki efek yang mengejutkan dengan melibatkan objek `mutable` seperti daftar lists dan kamus dictionaries.

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Sebagai contoh, daftar tricks dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua Dog instance :

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Desain kelas yang benar harus menggunakan variabel instance sebagai gantinya :

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 9.4 Keterangann Acak

Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance, sebagai contoh :

```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

Atribut data dapat dirujuk oleh metode dan juga oleh pengguna biasa ("clients") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni.

Objek fungsi apa pun yang merupakan atribut kelas menentukan metode untuk instance dari kelas itu. Tidak perlu bahwa definisi fungsi tertutup secara teks dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga ok. Sebagai contoh :

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Sekarang `f`, `g` dan `h` adalah semua atribut class C yang merujuk ke objek-objek fungsi, dan akibatnya semuanya adalah metode instance dari C.

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen `self` :

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Setiap nilai adalah objek, dan karenanya memiliki kelas juga disebut sebagai type. Ini disimpan sebagai object.`__class__`.

## 9.5 Pewarisan

Sintaks untuk definisi kelas turunan seperti contoh berikut :

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Nama BaseClassName harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi berubah-ubah arbitrary lainnya juga diperbolehkan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan dalam modul lain :

```python
class DerivedClassName(modname.BaseClassName):
```

Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri berasal dari beberapa kelas lain.

`DerivedClassName()` membuat instance baru dari kelas. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, turun rantai kelas dasar jika perlu, dan referensi metode ini valid jika  menghasilkan objek fungsi.

Ada cara sederhana untuk memanggil metode kelas dasar secara langsung yaitu cukup panggil `BaseClassName.methodname(self, arguments)`.

Python memiliki dua fungsi bawaan yang bekerja dengan warisan :

- Gunakan `isinstance()` untuk memeriksa jenis instance : `isinstance(obj, int)` akan menjadi True hanya jika `obj.__class__` adalah int atau beberapa kelas yang diturunkan dari int.
- Gunakan `issubclass()` untuk memeriksa warisan kelas: `issubclass(bool, int)``adalah ``True` karena `bool` adalah subkelas dari `int`. Namun, `issubclass(float, int)` adalah False karena `float` bukan subkelas dari `int`.

### 9.5.1 Pewarisan Berganda

Python mendukung bentuk pewarisan berganda juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini :

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Urutan resolusi metode berubah secara dinamis untuk mendukung pemanggilan kooperatif ke `super()`. Pendekatan ini dikenal dalam beberapa bahasa warisan ganda sebagai metode panggilan-berikutnya call-next-method dan lebih daripada panggilan super yang ditemukan dalam bahasa warisan tunggal.

Sebagai contoh, semua kelas mewarisi dari `object`, jadi segala kasus pewarisan berganda menyediakan lebih dari satu jalur untuk mencapai class `object`. Untuk menjaga agar kelas dasar tidak diakses lebih dari sekali, algoritma dinamis linier mengurutkan urutan pencarian dengan cara yang mempertahankan urutan kiri-ke-kanan yang ditentukan dalam setiap kelas, yang memanggil setiap induk hanya sekali, dan itu monoton artinya suatu kelas dapat di-subklas-kan tanpa memengaruhi urutan prioritas orang tuanya.

## 9.6 Variabel Privat

Variabel instance `Private` yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (mis. _spam) harus diperlakukan sebagai bagian non-publik dari API .

Setiap pengidentifikasi dari bentuk `__spam` setidaknya dua garis bawah utama, paling banyak satu garis bawah garis bawah secara teks diganti dengan `_classname__spam`, di mana `classname` adalah nama kelas saat ini. `Mangling` dilakukan tanpa memperhatikan posisi sintaksis pengidentifikasi, asalkan terjadi dalam definisi kelas.

Nama `Mangling` sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh :

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

Contoh di atas akan berfungsi bahkan jika `MappingSubclass` akan memperkenalkan sebuah pengidentifikasi `__update` karena diganti dengan `_Mapping__update` di kelas `Mapping` dan `_MappingSubclass__update` di kelas `MappingSubclass` masing-masing.

Bahwa aturan `mangling` sebagian besar dirancang untuk menghindari kesalahan masih dimungkinkan untuk mengakses atau memodifikasi variabel yang dianggap pribadi. Bahkan dapat berguna dalam keadaan khusus, seperti di debugger.

Bahwa kode yang dilewatkan ke `exec()` atau `eval()` tidak menganggap nama kelas `classname` dari kelas yang dipanggil sebagai kelas mirip dengan efek pernyataan global, yang efeknya juga terbatas pada kode yang dikompilasi-byte byte-compiled bersama. Pembatasan yang sama berlaku untuk `getattr()`, `setattr()` dan `delattr()`, serta saat mereferensikan `__dict__` secara langsung.

## 9.7 Odds dan Ends

Definisi kelas kosong akan menghasilkan hal tersebut dengan baik :

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

Jika memiliki fungsi yang memformat beberapa data dari objek file, kita dapat mendefinisikan kelas dengan metode `read()` dan `readline()` yang mendapatkan data dari buffer string sebagai gantinya, dan meneruskan itu sebagai argumen.

Objek metode instance memiliki atribut, juga: `m.__self__` adalah objek instan dengan metode `m()`, dan `m.__func__` adalah objek fungsi yang sesuai dengan metode tersebut.

## 9.8 Iterator

Sebagian besar objek penampung container dapat dibuat perulangan menggunakan pernyataan `for` :

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

Penggunaan iterator meliputi pervades dan menyatukan Python. Pernyataan `for` memanggil `iter()` pada objek penampung container. Fungsi mengembalikan objek iterator yang mendefinisikan metode `__next__()` yang mengakses elemen dalam penampung container satu per satu. Ketika tidak ada lagi elemen, `__next__()` memunculkan pengecualian `StopIteration` yang memberi tahu perulangan `for` untuk mengakhiri. Kita dapat memanggil metode `__next__()` menggunakan `next()` fungsi bawaan, sebagai contoh :

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

ika kelas mendefinisikan `__next__()`, maka `__iter__()` bisa langsung mengembalikan self, sebagai contoh :

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```


## 9.9 Generator

Generator adalah sebuah tool yang sederhana dan simpel untuk membuat sebuah iterasi. Ditulis seperti fungsi biasa tapi menggunakan pernyataan `yield` setiap kali ingin mengembalikan sebuah data. Tiap kali `next()` itu dipanggil, generator tersebut akan melanjutkan di mana hal itu berhenti. Itu akan mengingat semua nilai dan pernyataan mana yang terakhir dieksekusi.

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

Apa pun yang dapat dilakukan dengan generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan pada bagian sebelumnya. Apa yang membuat  generator sangat kompak adalah metode `__iter__()` dan `__next__()` dibuat secara otomatis. Selain pembuatan metode otomatis dan menyimpan status program, ketika  generator berhenti, mereka secara otomatis menimbulkan `StopIteration`.

## 9.10 Ekspresi Generator

Beberapa generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman `list` tetapi dengan tanda kurung `()` bukan dengan tanda kurung siku `[]`.

Sebagai Contoh : 

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```
