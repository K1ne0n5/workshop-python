# Flask Tutorial

Flask adalah sebuah web framework yang ditulis dengan bahasa Python dan tergolong sebagai jenis microframework. Flask berfungsi sebagai kerangka kerja aplikasi dan tampilan dari suatu web. Dengan menggunakan Flask dan bahasa Python, pengembang dapat membuat sebuah web yang terstruktur dan dapat mengatur behaviour suatu web dengan lebih mudah.

## Create an environment

Gunakan environment virtual untuk mengelola dependensi untuk proyek, baik dalam pengembangan maupun produksi. Environment virtual adalah grup independen dari pustaka Python, satu untuk setiap proyek. Paket yang diinstal untuk satu proyek tidak akan memengaruhi proyek lain atau paket sistem operasi.

Python dibundel dengan venv modul untuk membuat environment virtual.

- macOS/Linux
    ```python
    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv
    ```

- Windows
    ```python
    > mkdir myproject
    > cd myproject
    > py -3 -m venv venv
    ```

## Mengaktifkan env

Sebelum mengerjakan proyek, aktifkan environment yang sesuai:

- macOS/Linux
    ```python
    $ . venv/bin/activate
    ```

- Windows
    ```python
    > venv\Scripts\activate
    ```

## Install Flask

Dalam environment yang diaktifkan, gunakan perintah berikut untuk menginstal Flask:

```python
$ pip install Flask
```

## Project Layout

Membuat direktori proyek :

```python
$ mkdir flask-tutorial
$ cd flask-tutorial
```

Kemudian ikuti petunjuk instalasi untuk menyiapkan environment virtual Python dan menginstal Flask untuk proyek.

Direktori proyek akan berisi:
  * `flaskr/`, paket Python yang berisi kode aplikasi dan file.
  * `tests/`, direktori yang berisi modul pengujian.
  * `venv/`, environment virtual Python tempat Flask dan dependensi lainnya diinstal.
  * File instalasi memberi tahu Python cara menginstal proyek.
  * Konfigurasi kontrol versi, seperti `git` . harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek berapa pun ukurannya.

Tata letak Proyek akan terlihat seperti di bawah ini:

```python
/home/user/Projects/flask-tutorial
????????? flaskr/
???   ????????? __init__.py
???   ????????? db.py
???   ????????? schema.sql
???   ????????? auth.py
???   ????????? blog.py
???   ????????? templates/
???   ???   ????????? base.html
???   ???   ????????? auth/
???   ???   ???   ????????? login.html
???   ???   ???   ????????? register.html
???   ???   ????????? blog/
???   ???       ????????? create.html
???   ???       ????????? index.html
???   ???       ????????? update.html
???   ????????? static/
???       ????????? style.css
????????? tests/
???   ????????? conftest.py
???   ????????? data.sql
???   ????????? test_factory.py
???   ????????? test_db.py
???   ????????? test_auth.py
???   ????????? test_blog.py
????????? venv/
????????? setup.py
????????? MANIFEST.in
```

## Application Setup

Aplikasi Flask adalah turunan dari Flaskkelas. Segala sesuatu tentang aplikasi, seperti konfigurasi dan URL, akan didaftarkan dengan kelas ini.

Cara paling mudah untuk membuat aplikasi Flask adalah dengan membuat Flaskinstance global langsung di bagian atas kode.

Dari pada membuat Flaskinstance secara global, akan membuatnya di dalam suatu fungsi. Fungsi ini dikenal sebagai factory aplikasi.

### The Application Factory

Saatnya untuk memulai pengkodean! Buat flaskrdirektori dan tambahkan `__init__.py` file.

```python
$ mkdir flaskr
```

flaskr/__init__.py
```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

### Define and Access the Database

Aplikasi akan menggunakan database SQLite untuk menyimpan pengguna dan posting. Python hadir dengan dukungan bawaan untuk SQLite dalam sqlite3 modul. SQLite nyaman digunakan karena idak memerlukan pengaturan server database terpisah dan sudah terintegrasi dengan Python. 

### Connect to the Database

Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite adalah membuat koneksi ke database tersebut. Setiap kueri dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai. Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan.

flaskr/db.py

```python
    import sqlite3

    import click
    from flask import current_app, g
    from flask.cli import with_appcontext

    def get_db():
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

        return g.db

    def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()
```

### Create the Tables

Dalam SQLite, data disimpan dalam tabel dan kolom . Ini perlu dibuat sebelum dapat menyimpan dan mengambil data. Flaskr akan menyimpan pengguna di usertabel, dan posting di posttabel. Buat file dengan perintah SQL yang diperlukan untuk membuat tabel kosong:

flaskr/schema.sql

```python
    DROP TABLE IF EXISTS user;
    DROP TABLE IF EXISTS post;

    CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    );

    CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
    );
```

Tambahkan fungsi Python yang akan menjalankan perintah SQL ini ke `db.py`file :

flaskr/db.py

```python
    def init_db():
        db = get_db()

        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))


    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')
```

### Register with the Application

Fungsi `close_dband` `init_db_command` harus didaftarkan pada instance aplikasi, jika tidak mereka tidak akan digunakan oleh aplikasi. Namun, karena menggunakan fungsi factory, instans tersebut tidak tersedia saat menulis fungsi. Sebagai gantinya, tulis fungsi yang mengambil aplikasi dan melakukan pendaftaran.

flaskr/db.py
```python
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Impor dan panggil fungsi ini dari factory. Tempatkan kode baru di akhir fungsi factory sebelum mengembalikan aplikasi.

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

### Initialize the Database File

Sekarang setelah `init-db` terdaftar dengan aplikasi, itu dapat dipanggil menggunakan flaskperintah, mirip dengan run perintah dari halaman sebelumnya.

Jalankan `init-db` perintah:

```python
$ flask init-db
Initialized the database.
```

## Blueprints and Views

Fungsi tampilan adalah kode yang ditulis untuk menanggapi permintaan ke aplikasi. Flask menggunakan pola untuk mencocokkan URL permintaan yang masuk dengan tampilan yang seharusnya menanganinya. Tampilan mengembalikan data yang diubah Flask menjadi respons keluar.

### Create a Blueprint

Blueprint adalah cara untuk mengatur sekelompok tampilan terkait dan kode lainnya. Daripada mendaftarkan tampilan dan kode lain secara langsung dengan aplikasi, mereka terdaftar dengan blueprint. Kemudian blueprint didaftarkan dengan aplikasi ketika tersedia di fungsi factory.

Flaskr akan memiliki dua blueprint, satu untuk fungsi otentikasi dan satu lagi untuk fungsi posting blog. Kode untuk setiap blueprint akan dimasukkan ke dalam modul terpisah. Karena blog perlu mengetahui tentang autentikasi, akan menulis autentikasi terlebih dahulu.

flaskr/auth.py
```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```

### The First View : Register

Saat pengguna mengunjungi /auth/registerURL, registertampilan akan mengembalikan HTML dengan formulir untuk mereka isi. Ketika mereka mengirimkan formulir, akan memvalidasi input mereka dan menampilkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login.

Untuk saat ini hanya akan menulis kode tampilan. Pada halaman berikutnya, akan menulis template untuk menghasilkan formulir HTML.

flaskr/auth.py
```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```

### Login

Tampilan ini mengikuti pola yang sama seperti registertampilan.

flaskr/auth.py
```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

Sekarang setelah pengguna `id` disimpan di `session`, akan tersedia pada permintaan berikutnya. Di awal setiap permintaan, jika pengguna masuk, informasi mereka harus dimuat dan tersedia untuk tampilan lain.

flaskr/auth.py
```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```

### Logout

Untuk logout, harus mengdelete id pengguna dari file session. Kemudian `load_logged_in_user` tidak akan memuat pengguna pada permintaan berikutnya.

flaskr/auth.py
```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

```python
export DATABASE_URL="{connection-string}"
```

### Require Authentication in Other Views

Membuat, mengedit, dan mengdelete posting blog akan membutuhkan pengguna untuk login. Dekorator dapat digunakan untuk memeriksa ini untuk setiap tampilan yang diterapkan.

flaskr/auth.py
```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```

### Endpoints and URL

Fungsi `url_for()` menghasilkan URL ke tampilan berdasarkan nama dan argumen. Nama yang terkait dengan tampilan juga disebut titik akhir , dan secara default sama dengan nama fungsi tampilan.

## Templates

Template adalah file yang berisi data statis serta placeholder untuk data dinamis. Sebuah template diberikan dengan data tertentu untuk menghasilkan dokumen akhir. Flask menggunakan perpustakaan template Jinja untuk merender template.

### The Base Layout

Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di s badan yang berbeda.

flaskr/templates/base.html

```python
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

### Register

flaskr/templates/auth/register.html

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

### Log In

Identik dengan template daftar kecuali untuk judul dan tombol kirim.

flaskr/templates/auth/login.html

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

### Register A User

Isi username dan password dan akan diarahkan ke halaman login. Coba masukkan nama pengguna yang salah, atau nama pengguna yang benar dan kata sandi yang salah. Jika masuk, akan mendapatkan kesalahan karena belum ada index tampilan untuk dialihkan.

## Static Files

Flask secara otomatis menambahkan `static` tampilan yang mengambil jalur relatif ke `flaskr/static` direktori dan menyajikannya. Template `base.html` sudah memiliki tautan ke `style.css` file:

```python
{{ url_for('static', filename='style.css') }}
```

Selain CSS, jenis file statis lainnya mungkin file dengan fungsi JavaScript, atau gambar logo. Mereka semua ditempatkan di bawah `flaskr/static` direktori dan direferensikan dengan `.url_for('static', filename='...')`

flaskr/static/style.css

```python
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }
```

## Blog Blueprint

Blog harus mencantumkan semua posting, mengizinkan pengguna yang masuk untuk membuat posting, dan mengizinkan penulis posting untuk mengedit atau mengdeletenya. Saat menerapkan setiap tampilan, jaga agar server pengembangan tetap berjalan.

### The Blueprint

Tentukan blueprint dan daftarkan di factory aplikasi.

flaskr/blog.py

```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```

Impor dan daftarkan blueprint dari factory menggunakan `app.register_blueprint()`.

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

### Index

Indeks akan menampilkan semua posting, yang terbaru terlebih dahulu. `A JOIN` digunakan agar informasi penulis dari `user` tabel tersedia di hasil.

flaskr/blog.py
```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

flaskr/templates/blog/index.html

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```

### Create

Tampilan `create` berfungsi sama dengan registertampilan auth. Baik formulir ditampilkan, atau data yang diposting divalidasi dan postingan ditambahkan ke database atau kesalahan ditampilkan.

flaskr/blog.py

```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

flaskr/templates/blog/create.html

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```

### Update

Baik tampilan `update` maupun `delete` tampilan perlu diambil post oleh id dan memeriksa apakah pembuatnya cocok dengan pengguna yang masuk. Untuk menghindari duplikasi kode, dapat menulis fungsi untuk mendapatkan post dan memanggilnya dari setiap tampilan.

flaskr/blog.py

```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```

flaskr/blog.py

```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```

flaskr/templates/blog/update.html

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```

### Delete

Tampilan delete tidak memiliki template sendiri, tombol delete adalah bagian dari `update.html` dan memposting ke /<id>/deleteURL. Karena tidak ada template, itu hanya akan menangani `POST` metode dan kemudian mengarahkan ulang ke `index` tampilan.

flaskr/blog.py
```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

## Make the Project Installable

Membuat proyek dapat diinstal berarti dapat membuat file distribusi dan menginstalnya di environment lain, sama seperti  menginstal Flask di environment proyek. Ini membuat penerapan proyek sama dengan menginstal pustaka lain, jadi menggunakan semua alat Python standar untuk mengelola semuanya.

Menginstal juga dilengkapi dengan manfaat lain yang mungkin tidak terlihat dari tutorial atau sebagai pengguna Python baru, termasuk:
   * Saat ini, Python dan Flask memahami cara menggunakan flaskr paket hanya karena menjalankan dari direktori proyek. Menginstal berarti dapat mengimpornya dari mana pun menjalankannya.
   * Dapat mengelola dependensi proyek seperti halnya paket lain, jadi instal.pip install yourproject.whl
   * Alat pengujian dapat mengisolasi environment pengujian dari environment pengembangan.

### Describe the Project

setup.py

```python
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```

## Test Coverage

Menulis pengujian unit untuk aplikasi, memungkinkan untuk memeriksa apakah kode yang ditulis berjalan sesuai dengan yang diharapkan Flask menyediakan klien uji yang mensimulasikan permintaan ke aplikasi dan mengembalikan data respons. Kode dalam fungsi hanya berjalan ketika fungsi dipanggil, dan kode di cabang, seperti if blok, hanya berjalan ketika kondisi terpenuhi.

Menggunakan pytest dan coverage untuk menguji dan mengukur kode. Instal keduanya:

```python
$ pip install pytest coverage
```

### Setup and Fixtures

Kode tes terletak di testsdirektori. Direktori ini berada di sebelah paket flaskr, bukan di dalamnya. File tests/conftest.pyberisi fungsi pengaturan yang disebut perlengkapan yang akan digunakan setiap pengujian. Pengujian dalam modul Python yang dimulai dengan test_, dan setiap fungsi pengujian dalam modul tersebut juga dimulai dengan test_. Setiap pengujian akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam pengujian. Tulis file SQL untuk memasukkan data itu.

tests/data.sql

```python
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```

tests/conftest.py

```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```

### Factory

Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan memperhatikan. Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi pengujian. Jika konfigurasi tidak diteruskan, harus ada beberapa konfigurasi default, jika tidak, konfigurasi harus diganti.

tests/test_factory.py

```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

### Database

Dalam konteks aplikasi, `get_db` harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.

tests/test_db.py

```python
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```

tests/test_db.py

```python
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called"
```

### Authentication

Untuk sebagian besar tampilan, pengguna harus masuk. Cara termudah untuk melakukan ini dalam pengujian adalah membuat POST permintaan ke login tampilan dengan klien. Daripada menuliskannya setiap saat, dapat menulis kelas dengan metode untuk melakukan itu, dan menggunakan perlengkapan untuk memberikannya kepada klien untuk setiap pengujian.

tests/conftest.py

```python
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
```

tests/test_auth.py

```python
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```

### Blog

Semua tampilan blog menggunakan `auth` perlengkapan yang tulis sebelumnya. Panggilan `auth.login()` dan permintaan berikutnya dari klien akan masuk sebagai `test` pengguna.

Tampilan `index` harus menampilkan informasi tentang postingan yang ditambahkan dengan data pengujian. Saat masuk sebagai penulis, harus ada tautan untuk mengedit posting.

tests/test_blog.py

```python
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```

Pengguna harus masuk untuk mengakses `create`, `update`, dan `delete` tampilan. Pengguna yang masuk harus menjadi penulis kiriman untuk mengakses `update` dan `delete`, jika tidak, status akan dikembalikan. Jika tidak ada, dan harus kembali .`403 Forbidden post id update delete 404 Not Found`

tests/test_blog.py
```python
@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```

## Deploy to Production

Memberikan gambaran umum tentang cara membuat file distribusi dan menginstalnya, tetapi tidak akan membahas secara spesifik tentang server atau perangkat lunak apa yang digunakan. 

### Build and Install

Saat ingin menyebarkan aplikasi di tempat lain, harus membangun file distribusi. Standar saat ini untuk distribusi Python adalah format roda , dengan `.whl` ekstensi. Pastikan perpustakaan roda diinstal terlebih dahulu:

```python
$ pip install wheel
```

Menjalankan `setup.py` dengan Python memberi baris perintah untuk mengeluarkan perintah terkait `build`. Perintah `bdist_wheel` akan membangun file distribusi roda.

```python
$ python setup.py bdist_wheel
```

### Running with Server

Saat menjalankan secara publik dalam pengembangan, tidak boleh menggunakan server pengembangan bawaan. Server pengembangan disediakan oleh Werkzeug untuk kenyamanan, tetapi tidak dirancang untuk menjadi sangat efisien, stabil, atau aman.

flask run

```python
$ pip install waitress
```

```python
$ waitress-serve --call 'flaskr:create_app'

Serving on http://0.0.0.0:8080
```