# Scikit-learn

Scikit-learn atau sklearn merupakan sebuah module dari bahasa pemrograman Python yang dibangun berdasarkan NumPy, SciPy, dan Matplotlib. Fungsi dari module ini adalah untuk membantu melakukan processing data ataupun melakukan training data untuk kebutuhan machine learnng atau data science. Banyak sekali fitur yang ada pada module ini seperti model-model klasifikasi, clustering, regresi berbasis model machine learning, dan proses-proses yang dapat dimanfaatkan pada tahap Feature Engineering seperti reduksi dimensi menggunakan PCA.

## An introduction to machine learning with scikit-learn

Secara umum, learning problem mempertimbangkan satu set n sampel data dan kemudian mencoba memprediksi sifat data yang tidak diketahui. Jika setiap sampel lebih dari satu angka dan, misalnya, entri multidimensi (alias data multivariat ), dikatakan memiliki beberapa atribut atau fitur.

Masalah belajar terbagi dalam beberapa kategori:

1. Supervised learning , di mana data dilengkapi dengan atribut tambahan yang ingin prediksi. Masalah ini dapat berupa:
   * klasifikasi : sampel milik dua atau lebih kelas dan ingin belajar dari data yang sudah berlabel bagaimana memprediksi kelas data yang tidak berlabel. Contoh masalah klasifikasi adalah pengenalan digit tulisan tangan, di mana tujuannya adalah untuk menetapkan setiap vektor input ke salah satu dari sejumlah kategori diskrit yang terbatas. Cara lain untuk memikirkan klasifikasi adalah sebagai bentuk Supervised learning diskrit (berlawanan dengan kontinu) di mana seseorang memiliki sejumlah kategori terbatas dan untuk masing-masing dari n sampel yang disediakan, salah satunya adalah mencoba memberi label dengan kategori atau kelas yang benar.
   * regresi : jika keluaran yang diinginkan terdiri dari satu atau lebih variabel kontinu, maka tugas tersebut disebut regresi . Contoh masalah regresi adalah prediksi panjang ikan salmon sebagai fungsi dari umur dan beratnya.

2. Unsupervised learning , di mana data pelatihan terdiri dari satu set vektor input x tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut mungkin untuk menemukan kelompok contoh serupa dalam data, yang disebut pengelompokan , atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai estimasi kepadatan , atau untuk memproyeksikan data dari dimensi tinggi. ruang ke dua atau tiga dimensi untuk tujuan visualisasi.

## Loading an example dataset

`scikit-learn` dilengkapi dengan beberapa kumpulan data sr, misalnya kumpulan data `iris` dan `angka` untuk klasifikasi dan `kumpulan data diabetes` untuk regresi.

Berikut ini, memulai interpreter Python dari shell dan kemudian memuat irisdan digitsset data. Konvensi notasi adalah yang $menunjukkan prompt shell sementara `>>>` menunjukkan prompt Python:

```python
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```

Dataset adalah objek seperti kamus yang menyimpan semua data dan beberapa metadata tentang data tersebut. Data ini disimpan dalam `.data` anggota, yang merupakan array. Dalam kasus masalah yang diawasi, satu atau lebih variabel respons disimpan di anggota. Rincian lebih lanjut tentang kumpulan data yang berbeda dapat ditemukan di bagian khusus `.n_samples`, `n_features.target`

Misalnya, dalam kasus kumpulan data digit, `digits.data` memberikan akses ke fitur yang dapat digunakan untuk mengklasifikasikan sampel digit:

```python
>>> print(digits.data)
[[ 0.   0.   5. ...   0.   0.   0.]
 [ 0.   0.   0. ...  10.   0.   0.]
 [ 0.   0.   0. ...  16.   9.   0.]
 ...
 [ 0.   0.   1. ...   6.   0.   0.]
 [ 0.   0.   2. ...  12.   0.   0.]
 [ 0.   0.  10. ...  12.   1.   0.]]
```

`digits.target` memberikan kebenaran dasar untuk kumpulan data digit, yaitu angka yang sesuai dengan setiap gambar digit yang coba pelajari:

```python
>>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
```

**Bentuk array data**

Data selalu berupa larik 2D, bentuk , meskipun data asli mungkin memiliki bentuk yang berbeda. Dalam hal digit, setiap sampel asli adalah gambar bentuk dan dapat diakses menggunakan: `(n_samples, n_features)(8, 8)`

```python
>>> digits.images[0]
array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
       [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
       [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
       [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
       [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
       [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
       [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
       [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])
```

## Learning and predicting

Dalam kasus kumpulan data digit, tugasnya adalah memprediksi, dengan diberikan gambar, digit mana yang diwakilinya. diberikan sampel dari masing-masing 10 kelas yang mungkin (angka nol sampai sembilan) yang sesuaikan dengan estimator untuk dapat memprediksi kelas yang termasuk dalam sampel tak terlihat.

Dalam scikit-learn, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode dan `.fit(X, y)predict(T)`

Contoh estimator adalah kelas `sklearn.svm.SVC`, yang mengimplementasikan klasifikasi vektor pendukung . Konstruktor estimator mengambil parameter model sebagai argumen.

Untuk saat ini, akan mempertimbangkan estimator sebagai kotak hitam:

```python
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
```

**Memilih parameter model**

Dalam contoh ini, menetapkan nilai gamma secara manual. Untuk menemukan nilai yang baik untuk parameter ini, kita dapat menggunakan alat seperti pencarian kisi dan validasi silang.

Instance estimator ( `clf` untuk pengklasifikasi ) pertama-tama dipasang ke model. Dilakukan dengan meneruskan set pelatihan ke `fit` metode. Untuk set pelatihan, akan menggunakan semua gambar dari dataset, kecuali untuk gambar terakhir, yang akan simpan untuk prediksi. memilih set pelatihan dengan [:-1] sintaks Python, yang menghasilkan array baru yang berisi semua kecuali item terakhir dari `digits.data`:

```python
>>> clf.fit(digits.data[:-1], digits.target[:-1])
SVC(C=100.0, gamma=0.001)
```

sekarang dapat memprediksi nilai baru. Dalam hal ini, akan memprediksi menggunakan gambar terakhir dari `digits.data.` Dengan memprediksi, akan menentukan gambar dari set pelatihan yang paling cocok dengan gambar terakhir.

```python
>>> clf.predict(digits.data[-1:])
array([8])
```

## Conventions

scikit-learn estimator mengikuti aturan tertentu untuk membuat perilaku mereka lebih prediktif.

**Type casting**

Kecuali ditentukan lain, masukan akan diberikan ke float64:

```python
>>> import numpy as np
>>> from sklearn import kernel_approximation

>>> rng = np.random.RandomState(0)
>>> X = rng.rand(10, 2000)
>>> X = np.array(X, dtype='float32')
>>> X.dtype
dtype('float32')

>>> transformer = kernel_approximation.RBFSampler()
>>> X_new = transformer.fit_transform(X)
>>> X_new.dtype
dtype('float64')
```

Dalam contoh ini, X adalah float32, yang dilemparkan float64 oleh fit_transform(X).

Target regresi diberikan float64 dan target klasifikasi dipertahankan:

```python
>>> from sklearn import datasets
>>> from sklearn.svm import SVC
>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
SVC()

>>> list(clf.predict(iris.data[:3]))
[0, 0, 0]

>>> clf.fit(iris.data, iris.target_names[iris.target])
SVC()

>>> list(clf.predict(iris.data[:3]))
['setosa', 'setosa', 'setosa']
```

Di sini, yang pertama predict() mengembalikan array integer, karena `iris.target` (array integer) digunakan dalam fit. Yang kedua predict() mengembalikan array string, karena `iris.target_names` untuk pemasangan.

**Refitting and updating parameters**

Hyper-parameter estimator dapat diperbarui setelah dibangun melalui metode set_params() . Memanggil fit()lebih dari sekali akan menimpa apa yang dipelajari oleh sebelumnya fit():

```python
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC
>>> X, y = load_iris(return_X_y=True)

>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X, y)
SVC(kernel='linear')
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])

>>> clf.set_params(kernel='rbf').fit(X, y)
SVC()
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
```

Di sini, kernel default rbfpertama kali diubah menjadi linearvia SVC.set_params()setelah estimator dibuat, dan diubah kembali ke rbfuntuk menyesuaikan estimator dan membuat prediksi kedua.

**Multiclass vs. multilabel fitting**

Saat menggunakan, tugas pembelajaran dan prediksi yang dilakukan bergantung pada format data target yang sesuai dengan:`multiclass classifiers`

```python
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```

Dalam kasus di atas, pengklasifikasi cocok pada larik 1d dari label multikelas dan oleh predict() karena itu metode ini menyediakan prediksi multikelas yang sesuai. Dimungkinkan juga untuk menyesuaikan pada array 2d indikator label biner:

```python
>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```

Di sini, pengklasifikasi berada fit() pada representasi label biner 2d dari y, menggunakan LabelBinarizer. Dalam hal ini predict() mengembalikan array 2d yang mewakili prediksi multilabel yang sesuai.

Perhatikan bahwa contoh keempat dan kelima mengembalikan semua nol, menunjukkan bahwa mereka tidak cocok dengan tiga label fit. Dengan keluaran multilabel, sebuah instance juga dapat diberi beberapa label:

```python
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```

Dalam hal ini, pengklasifikasi cocok pada instance yang masing-masing diberi beberapa label. Digunakan untuk binerisasi `MultiLabelBinarizer` array 2d dari multilabel ke fitatas. Akibatnya, predict() kembalikan larik 2d dengan beberapa label yang diprediksi untuk setiap instance.

