# 📋 API To-Do List

API To-Do List adalah aplikasi berbasis Flask yang menyediakan fitur untuk membuat, mengelola, dan menghapus checklist dengan sistem autentikasi menggunakan JWT.

## 🚀 Fitur
- **Autentikasi**: Register & Login dengan JWT
- **Checklist**: CRUD (Create, Read, Update, Delete)
- **Checklist Items**: CRUD dalam sebuah checklist
- **Ubah Status**: Tandai item sebagai selesai atau belum selesai

---

## 📌 Instalasi & Konfigurasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/repo-name.git
cd api-to-do-list
```

### 2️⃣ Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Instal Dependensi
```bash
pip install -r requirements.txt
```

### 4️⃣ Konfigurasi Database
Migrasi database dengan perintah berikut:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5️⃣ Jalankan Server
```bash
flask run
```
Server akan berjalan di `http://127.0.0.1:5000`

---

## 🔐 Autentikasi

### Register User
**Endpoint:** `POST /auth/register`
```json
{
  "username": "user123",
  "password": "password123"
}
```
**Response:**
```json
{
  "message": "User registered successfully"
}
```

### Login User
**Endpoint:** `POST /auth/login`
```json
{
  "username": "user123",
  "password": "password123"
}
```
**Response:**
```json
{
  "access_token": "your-jwt-token"
}
```
Gunakan `access_token` ini sebagai Bearer Token di header permintaan berikutnya.

---

## 📋 Checklist API
Semua endpoint checklist diawali dengan `/api/...`

### Buat Checklist
**Endpoint:** `POST /api/checklist`
```json
{
  "title": "Belajar Flask"
}
```
**Response:**
```json
{
  "id": 1,
  "title": "Belajar Flask"
}
```

### Lihat Semua Checklist
**Endpoint:** `GET /api/checklist`
**Response:**
```json
[
  { "id": 1, "title": "Belajar Flask" }
]
```

### Hapus Checklist
**Endpoint:** `DELETE /api/checklist/{id}`
**Response:**
```json
{
  "message": "Checklist deleted"
}
```

---

## 📌 Checklist Items API

### Tambah Item ke Checklist
**Endpoint:** `POST /api/checklist/{checklist_id}/items`
```json
{
  "name": "Install Flask"
}
```
**Response:**
```json
{
  "id": 1,
  "name": "Install Flask",
  "is_done": false
}
```

### Ubah Status Item (Selesai/Belum Selesai)
**Endpoint:** `PATCH /api/items/{item_id}/status`
**Response:**
```json
{
  "message": "Item status updated"
}
```

### Hapus Item dari Checklist
**Endpoint:** `DELETE /api/items/{item_id}`
**Response:**
```json
{
  "message": "Item deleted"
}
```

---

## 🛠 Teknologi yang Digunakan
- Python & Flask
- Flask-JWT-Extended (Autentikasi JWT)
- Flask-SQLAlchemy (ORM untuk Database)
- SQLite (Database Default, bisa diganti ke PostgreSQL/MySQL)

---

## 📌 Lisensi
Proyek ini menggunakan lisensi MIT. Bebas digunakan dan dikembangkan lebih lanjut. 😊
