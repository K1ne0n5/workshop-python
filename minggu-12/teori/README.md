# Jupyter Documentation

Perangkat lunak gratis, standar terbuka, dan layanan web untuk komputasi interaktif di semua bahasa pemrograman

`JupyterLab` adalah lingkungan pengembangan interaktif berbasis web terbaru untuk buku catatan, kode, dan data. Antarmukanya yang fleksibel memungkinkan pengguna untuk mengonfigurasi dan mengatur alur kerja dalam ilmu data, komputasi ilmiah, jurnalisme komputasi, dan pembelajaran mesin. Desain modular mengundang ekstensi untuk memperluas dan memperkaya fungsionalitas.

`Notebook Jupyter` adalah aplikasi web asli untuk membuat dan berbagi dokumen komputasi. Ini menawarkan pengalaman yang sederhana, efisien, dan berpusat pada dokumen.

**Language of choice**

Jupyter mendukung lebih dari 40 bahasa pemrograman, termasuk Python, R, Julia, dan Scala.

**Share notebooks**

Buku catatan dapat dibagikan dengan orang lain menggunakan email, Dropbox, GitHub, dan Jupyter Notebook Viewer .

**Interactive output**

Kode Kita dapat menghasilkan keluaran yang kaya dan interaktif: HTML, gambar, video, LaTeX, dan jenis MIME khusus.

**Big data integration**

Manfaatkan alat data besar, seperti Apache Spark, dari Python, R, dan Scala. Jelajahi data yang sama dengan pandas, scikit-learn, ggplot2, dan TensorFlow.

## Installing Jupyter

Alat Project Jupyter tersedia untuk instalasi melalui Python Package Index , repositori perangkat lunak terkemuka yang dibuat untuk bahasa pemrograman Python.

Halaman ini menggunakan instruksi dengan `pip`, alat instalasi yang direkomendasikan untuk Python.

### JupyterLab

Instal JupyterLab dengan pip :

```python
pip install jupyterlab
```

Setelah terinstal, luncurkan JupyterLab dengan :

```python
jupyter-lab
```

**Jupyter Notebook**

Instal Notebook Jupyter klasik dengan :

```python
pip install notebook
```

Untuk menjalankan notebook :

```python
jupyter notebook
```

### JupyterHub

`JupyterHub` menghadirkan kekuatan notebook ke grup pengguna. Ini memberi pengguna akses ke lingkungan dan sumber daya komputasi tanpa membebani pengguna dengan tugas instalasi dan pemeliharaan. 

`JupyterHub` berjalan di cloud atau di perangkat keras Anda sendiri, dan memungkinkan untuk menyajikan lingkungan ilmu data yang telah dikonfigurasi sebelumnya kepada pengguna mana pun di dunia. Ini dapat disesuaikan dan terukur, dan cocok untuk tim kecil dan besar, kursus akademik, dan infrastruktur skala besar.

### Fitur utama JupyterHub

`Dapat disesuaikan` - JupyterHub dapat digunakan untuk melayani berbagai lingkungan. Ini mendukung lusinan kernel dengan server Jupyter, dan dapat digunakan untuk melayani berbagai antarmuka pengguna termasuk Notebook Jupyter, Jupyter Lab, RStudio, nteract, dan banyak lagi.

`Fleksibel` - JupyterHub dapat dikonfigurasi dengan otentikasi untuk memberikan akses ke sebagian pengguna. Otentikasi dapat dipasang, mendukung sejumlah protokol otentikasi (seperti OAuth dan GitHub).

`Scalable` - JupyterHub ramah terhadap container, dan dapat digunakan dengan teknologi container modern. Itu juga berjalan di Kubernetes, dan dapat berjalan dengan hingga puluhan ribu pengguna.

`Portable` - JupyterHub sepenuhnya open-source dan dirancang untuk dijalankan di berbagai infrastruktur. Ini termasuk penyedia cloud komersial, mesin virtual, atau bahkan perangkat keras laptop Anda sendiri.

Kode dan teknologi dasar JupyterHub dapat ditemukan di repositori JupyterHub . Repositori ini dan dokumentasi JupyterHub berisi lebih banyak informasi tentang internal JupyterHub, penyesuaiannya, dan konfigurasinya.

# Struktur Data (Bab 3)

Struktur data adalah cara menyimpan dan mengatur data secara terstruktur pada sistem komputer atau database sehingga lebih mudah diakses.

Struktur ini memudahkan pengguna mengakses data yang dibutuhkan secara cepat dan tepat karena struktur data memiliki format khusus yang berfungsi untuk mengatur, memproses, mengambil, dan menyimpan data.

### 5.1 List / Daftar

Beberapa metode yang digunakan untuk list / daftar pada python : 

```python
list.append(x)
    # Item ini ditambahkan pada akhir sebuah daftar.
``` 

```python
list.extend(iterable)
    # Extend pada daftar dapat ditambahkan ke semua item yang berada di iterable.
```
        
```python
list.insert(i, x)
    # Insert dapat digunakan untuk memberikan posisi pada sebuah item. Argumen pertama merupakan indeks dari elemen sebelum dimasukkan.
```

```python
list.remove(x)
    # Remove dapat digunakan untuk menghilangkan item pertama disebuah daftar yang nilainya sama dengan x dan akan menghasilkan ValueError jika tidak ditemukan item yang serupa. 
```
        
```python
list.pop([i])
    # Perintah ini dapat menghapus item yang berada pada posisi tertentu didalam daftar dan dapat juga dikembalikan lagi. Jika tidak ditemukan indeks yang ditentukan akan dihapus dan dikembalikan sehingga menjadi item terakhir didalam daftar.
```
       
```python
list.clear()
    # Memindahkan semua item dari daftar.
``` 
        
```python
list.index(x[, start[, end]])
    # Mengulang data dari indeks *zero-base* pada daftar menjadi item pertama dengan *value* berupa x atau yang setara dan akan menghasilkan ValueError jika tidak ditemukan perintah serupa didalamnya.
```

```python
list.count(x)
    # Menghitung kembali nomor dari variabel *x* yang berada didalam daftar.
```
        
```python
list.sort(, key=None, Reverse=False)
    # Sort berfungsi untuk menyortir item didalam daftar.
```

```python
list.reverse()
    # Reverse berfungsi untuk membalikkan elemen didaftar pada tempat sebenarnya.
```

```python
list.copy()
    # Perintah ini berfungsi untuk mengembalikan salinan daftar yang dangkal.
```

Contoh penggunaan metode pada list python : 

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)   # Mencari banana setelah memulai pencarian dari posisi 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()
```

#### 5.1.1 Menggunakan List Sebagai Tumpukan

Metode daftar jika dibuat sebagai sebuah tumpukan, dimana elemen terakhir yang ditambahkan adalah elemen pertama yang dapat diambil.

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack
```

#### 5.1.2 Menggunakan Daftar Sebagai Antrian

Metode daftar sebagai antrian yaitu elemen pertama yang ditambahkan merupakan elemen pertama yang dapat diambil. Walaupun begitu penggunaan daftar ini tidaklah efesien karena pengambilan data menjadi lambat.

```python
from collections import deque
queue = deque(["David Kim", "Mama Takata", "Travis Watanabe"])

queue.append("Daniel Choi")     # Memasukkan Daniel kedalam antrian

queue.append("Kyle Bang")       # Memasukkan Kyle kedalam antrian

queue.popleft()                 # Memindahkan data pertama

queue.popleft()                 # Memindahkan data kedua

queue                           # Menyusun kembali antrian berdasarkan data yang dimasukkan 
```

#### 5.1.3 List Comprehensions

Metode ini biasanya digunakan untuk membuat sebuah daftar baru dimana setiap elemen merupakan hasil dari beberapa operasi yang diterapkan ke setiap item dari urutan lain atau *iterable*, atau untuk membuat sub urutan dari elemen yang memenuhi kondisi tersebut.

Contoh penerapan membuat sebuah list berbentuk kotak :

```python
squares = []
for x in range(4):
    squares.append(x**2)

squares
```

Untuk menghilangkan variabel yang menumpuk pada source code diatas dapat dilakukang dengan perintah berikut ataupun ekuivalen berikut :

```python
squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]
```

Contoh penggunaan listcomp yang menggabungkan elemen dari dua list jika tidak sama :

```python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

atau

```python
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs
```
Jika ekspresi adalah tuple maka harus di kurung (x, y)

```python
vec = [-4, -2, 0, 2, 4]

# Membuat list baru dengan value berlipat
[x*2 for x in vec]

# Mem-filter daftar tidak termasuk bilangan negatif
[x for x in vec if x >= 0]

# Mengaplikasikan sebuah fungsi untuk semua elemen yang ada
[abs(x) for x in vec]

# Memanggil method dari elemen lain
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# Membuat sebuah list dari 2 tuple seperti nomer atau kotak
[(x, x**2) for x in range(6)]

# Sebuah tuple haruslah memiliki parenthesized atau tidak akan mengalami error
[x, x**2 for x in range(6)]

# Meratakan daftar menggunakan listcomp dengan dua seleksi for
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
```

Dapat juga berisi ekspresi kompleks dan fungsi bersarang :

```python
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```

#### 5.1.4 Nested List Comprehensions

Ekspresi awal yang digunakan dalam pemahaman daftar dapat berupa ekspresi arbitrer. Berikut contoh dari matriks 3 list 4 length : 

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```

Berikut akan mengubah baris dan kolom :

```python
[[row[i] for row in matrix] for i in range(4)]
```

atau menggunakan listcomp

```python
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
```

atau dapat menggunakan

```python
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
```

Menggunakan built-in function _zip()_ :

```python
list(zip(*matrix))
```

### 5.2 Del Statement

Untuk menghapus sebuah item dari daftar terdapat beberapa cara yang dapat dilakukan salah satunya adalah pernyataan del. _Del_ Juga dapat digunakan untuk menghapus sebuah irisan dari daftar atau menghapus semua isi daftar.

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a

del a[2:4]
a

del a[:]
a
```

_Del_ juga dapat digunakan untuk menghapus seluruh variabel :

```python
del a
```

### 5.3 Tuples dan Sequence

Pada python tipe data berurutan dapat ditambahkan dan juga dapat dimasukan pada tipe data urutan standar lainnya yakni tuple. Tuple sendiri terdiri atas sejumlah nilai yang dipisahkan oleh koma :

```python
t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
```

Seperti yang terlihat pada program diatas, tuple keluaran selalu diapit tanda kurung, sehingga tuple bersarang dapat diterjemahkan dengan benar.

```python
empty = ()
singleton = 'Annyeonghaseo',    # <-- note trailing comma
len(empty)

len(singleton)

singleton

x, y, z = t
```

### 5.4 Sets

Python juga menyertakan tipe data untuk set . Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Set() fungsi dapat digunakan untuk membuat himpunan. Untuk membuat set kosong harus menggunakan set(), bukan { }.

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)          # Menampilkan duplikat setelah dipindahkan

'orange' in basket     # Menguji kecepatan membership

'crabgrass' in basket

# Mendemonstrasikan operasi set dengan unique letter dari dua kata

a = set('abracadabra')
b = set('alacazam')
a          # unique letters in a

a - b      # letters in a but not in b

a | b      # letters in a or b or both

a & b      # letters in both a and b

a ^ b      # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a
```

### 5.5 Dictionaries

Operasi utama pada _dictionary_ adalah menyimpan sebuah nilai dengan beberapa kunci dan dapat mengekstrak nilai yang diberikan kunci tersebut. Untuk membuat daftar pada _dictionary_ dapat dilakukan dengan perintah list().

Contoh penggunaan _dictionary_ :

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}

dict(sape=4139, guido=4127, jack=4098)
```

### 5.6 Teknik Looping

Pengulangan pada _dictionary_ key dan value dapat dilakukan dengan metode items() ini, enumerate(), zip(), reversed(), sorted().

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['Kevin Steward', 'patronous', 'black']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
```

Membuat daftar baru dengan teknik *looping* :
```python
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
```

### 5.7 Beberapa Dalam Kondisi

Kondisi yang digunakan dalam whiledan ifpernyataan dapat berisi operator apa pun, bukan hanya perbandingan. 

Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik.

Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not.

Contoh penggunaannya :

```python
string1, string2, string3 = '', 'Trondheim', 'Chicken noddle soup dance'
non_null = string1 or string2 or string3
non_null
```

Dalam python, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus :=

### 5.8 Membandingkan Sequences dan Tipe lainnya 

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. 

Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan *leksikografis* dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama.

