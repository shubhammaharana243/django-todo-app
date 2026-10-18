# 📝 Django To-Do App

A responsive To-Do web application built with **Python and Django** to manage daily tasks efficiently.

## ✨ Features

- 🔐 **User Authentication** — User signup, login, and logout
- ➕ **Add Tasks** — Create new tasks easily
- ✏️ **Update Tasks** — Edit existing task details
- 🗑️ **Delete Tasks** — Remove tasks when no longer needed
- 🔍 **Search Tasks** — Find tasks quickly using search
- 🏷️ **Task Filters** — Filter tasks based on their status
- 📱 **Responsive Design** — Works across desktop, tablet, and mobile devices
- 💾 **SQLite Database** — Store task data using Django's SQLite integration

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3
- **Version Control:** Git and GitHub

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shubhammaharana243/django-todo-app.git
cd django-todo-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## 📂 Project Structure

```text
django-todo-app/
├── TODO/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todoApp/
│   ├── migrations/
│   ├── management/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── .gitignore
├── manage.py
└── requirements.txt
```

## 🔒 Security Notes

- Keep secret keys and environment variables out of version control.
- Do not commit your `.env` file or local database.
- Configure production settings before deploying the application.

## 👨‍💻 Author

**Shubham Maharana**

- GitHub: [@shubhammaharana243](https://github.com/shubhammaharana243)

---

⭐ If you find this project useful, consider giving it a star!