# 🎓 Student Attendance Management System (Django)

A simple **Student Attendance Management System** built using the **Django framework**.
This project helps manage students and allows marking & viewing attendance in an easy and structured way.

---

## 🚀 Features

* 🔐 User Authentication (Login & Signup)
* ➕ Add Students
* 📝 Mark Student Attendance
* 👀 View Attendance Records
* 🏠 Home Dashboard
* 🗂️ Organized Django app & template structure

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite3
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
attendance/
│
├── attendance/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── studapp/             # Attendance application
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   └── studapp/
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── signup.html
│       ├── add_student.html
│       ├── mark_attendance.html
│       └── view_attendance.html
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/student-attendance-django.git
```

2. **Go to project directory**

```bash
cd student-attendance-django
```

3. **Create virtual environment**

```bash
python -m venv venv
```

4. **Activate virtual environment**

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

5. **Install Django**

```bash
pip install django
```

6. **Apply migrations**

```bash
python manage.py migrate
```

7. **Run the server**

```bash
python manage.py runserver
```

8. **Open browser**

```
http://127.0.0.1:8000/
```

---

## 🔑 Application Flow

* App opens with **Login Page**
* New users can **Sign Up**
* After login:

  * Add students
  * Mark attendance
  * View attendance records

---

## 📌 Future Enhancements

* 📊 Attendance reports & analytics
* 📅 Date-wise filtering
* 👨‍🏫 Role-based access
* 🎨 Better UI/UX

---

## 👩‍💻 Author

**Shivani Barot**
🎯 Django & Web Development Learner

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
