# 🎓 Student Management System (Django CRUD - FBV)

A Student Management Web Application built using Django Function-Based Views with CRUD Operations, Search, Pagination, Bootstrap UI & SweetAlert Confirmations.

---

## ✅ Features
| Feature         | Description                                  |
|-----------------|----------------------------------------------|
| Add Student     | Create new student records using forms       |
| Edit Student    | Update / modify existing student details     |
| Delete Student  | SweetAlert confirmation before deleting data |
| List Students   | Display students in a clean table structure  |
| Search          | Filter by Name or Roll Number                |
| Pagination      | Manage long lists effectively                |
| Bootstrap UI    | Clean, responsive & user friendly interface  |
| Messages System | Shows success notifications                  |

---

## 🏛️ Tech Stack
| Component | Technology          |
|----------|---------------------|
| Backend  | Django              |
| Frontend | HTML, CSS, Bootstrap|
| Database | SQLite              |
| Alerts   | SweetAlert2         |
| ORM      | Django ORM          |

---

## 🛠️ Installation
```bash
# 1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/student_management_system.git
cd student_management_system

# 2️⃣ Create Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

# (Linux/Mac)
# python3 -m venv venv
# source venv/bin/activate

# 3️⃣ Install Requirements
pip install -r requirements.txt

# 4️⃣ Apply Migrations
python manage.py migrate

# 5️⃣ Run Server
python manage.py runserver
Open in browser: http://127.0.0.1:8000/

