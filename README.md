
📝 Curie Blogs
A clean, professional Django-based blogging platform where authors can publish stories, mystery articles, time-travel tales, historical fiction, and more.
________________________________________
🚀 Project Overview
Curie Blogs is a fully functional Django blog application that allows multiple authors to write, publish, and manage posts. The homepage displays the latest posts with author details, thumbnails, timestamps, and a sidebar featuring categories like Latest Posts, Author’s Corner, and About.
________________________________________
✨ Features
•	✍️ Multi-author blogging system
•	📰 Beautiful homepage layout with latest stories
•	🔍 Post detail page with full content
•	👤 Author profiles with post counts
•	📅 Automatic timestamps
•	🧭 Sidebar widgets
o	About section
o	Latest posts
o	Author’s corner
•	🌐 Responsive Bootstrap-based UI
•	🔐 User authentication (login, logout, register)
________________________________________
🏗️ Tech Stack
•	Backend: Django (Python)
•	Frontend: HTML, CSS, Bootstrap 5
•	Database: SQLite (default), expandable to PostgreSQL/MySQL
•	Template Engine: Django Templates
________________________________________
📁 Project Structure
curie_blogs/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   ├── blog/
│   │   │   ├── home.html
│   │   │   ├── post_detail.html
│   │   │   ├── author_posts.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── curie_blogs/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/ (for user-uploaded images)
├── db.sqlite3
├── manage.py
└── README.md
________________________________________
1. Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the blog.
________________________________________
🖼️ Screenshots
Home Page
<img width="666" height="479" alt="image" src="https://github.com/user-attachments/assets/57481636-8e89-4127-b1b0-d8c230a5a4c8" /> 
 ________________________________________
🧩 Key Django Models
🔹 Post Model
•	Title
•	Slug
•	Author (ForeignKey → User)
•	Thumbnail image
•	Body
•	Created date
•	Updated date
🔹 Author Model
Extended using Django User model.
________________________________________
📦 Deployment
This project can be deployed on:
•	Render
•	Railway
•	PythonAnywhere
•	Heroku (needs adjustments)
•	AWS EC2
________________________________________
🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to modify.
________________________________________
👩‍💻 Author
Developed by Likhitha D S
Feel free to ⭐ the repo if you like this project!
________________________________________

