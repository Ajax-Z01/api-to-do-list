# 📌 Dokumentasi API To-Do List

Dokumentasi ini menjelaskan endpoint yang tersedia dalam API To-Do List.

## 🔑 Autentikasi

### 1️⃣ Register User
- **Endpoint:** `POST /auth/register`
- **Deskripsi:** Mendaftarkan pengguna baru.
- **Body JSON:**
  ```json
  {
    "username": "user123",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully"
  }
  ```

### 2️⃣ Login User
- **Endpoint:** `POST /auth/login`
- **Deskripsi:** Login untuk mendapatkan token akses.
- **Body JSON:**
  ```json
  {
    "username": "user123",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "<JWT_TOKEN>"
  }
  ```

## 📝 Checklist API
Semua endpoint checklist diawali dengan `/api/...`

### 3️⃣ Buat Checklist
- **Endpoint:** `POST /api/checklist`
- **Deskripsi:** Membuat checklist baru.
- **Headers:**
  ```json
  {
    "Authorization": "Bearer <JWT_TOKEN>"
  }
  ```
- **Body JSON:**
  ```json
  {
    "title": "Checklist Baru"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Checklist Baru",
  }
  ```

### 4️⃣ Hapus Checklist
- **Endpoint:** `DELETE /api/checklist/<id>`
- **Deskripsi:** Menghapus checklist berdasarkan ID.

### 5️⃣ Tampilkan Semua Checklist
- **Endpoint:** `GET /api/checklist`
- **Deskripsi:** Menampilkan semua checklist milik pengguna yang login.

### 6️⃣ Detail Checklist
- **Endpoint:** `GET /api/checklist/<id>`
- **Deskripsi:** Menampilkan detail checklist beserta item di dalamnya.

## ✅ Checklist Item API

### 7️⃣ Buat Item dalam Checklist
- **Endpoint:** `POST /api/checklist/<checklist_id>/items`
- **Deskripsi:** Menambahkan item ke dalam checklist tertentu.

### 8️⃣ Detail Item dalam Checklist
- **Endpoint:** `GET /api/items/<item_id>`
- **Deskripsi:** Menampilkan detail item berdasarkan ID.

### 9️⃣ Update Item dalam Checklist
- **Endpoint:** `PUT /api/items/<item_id>`
- **Deskripsi:** Mengubah nama item dalam checklist.

### 🔟 Ubah Status Item (Done/Undone)
- **Endpoint:** `PATCH /api/items/<item_id>/status`
- **Deskripsi:** Mengubah status item menjadi selesai atau belum selesai.

### 1️⃣1️⃣ Hapus Item dari Checklist
- **Endpoint:** `DELETE /api/items/<item_id>`
- **Deskripsi:** Menghapus item dari checklist.

---

Dokumentasi ini dapat diperbarui sesuai dengan perkembangan API.

