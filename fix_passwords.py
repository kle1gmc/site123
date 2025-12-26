import hashlib
import json
import os
from datetime import datetime


def fix_passwords():
    """Исправить пароли в базе"""

    # Новые правильные хэши SHA256
    admin_hash = hashlib.sha256("admin123".encode()).hexdigest()
    student_hash = hashlib.sha256("student123".encode()).hexdigest()

    users_data = [
        {
            "id": 1,
            "username": "admin",
            "password": admin_hash,  # SHA256 вместо scrypt
            "role": "admin",
            "email": "admin@college.ru",
            "createdAt": datetime.now().isoformat()
        },
        {
            "id": 2,
            "username": "student1",
            "password": student_hash,  # SHA256 вместо scrypt
            "role": "student",
            "email": "student1@college.ru",
            "createdAt": datetime.now().isoformat()
        }
    ]

    # Также создадим студентов
    students_data = [
        {
            "id": 1,
            "name": "Иван Иванов",
            "course": 1,
            "status": "studying",
            "description": "Backend-разработчик, увлекается Python и SQL",
            "fullInfo": "Студент 1 курса, изучает Python и базы данных.",
            "skills": ["Python", "SQL", "PostgreSQL"],
            "links": {
                "github": "https://github.com/ivanov",
                "portfolio": "https://ivanov-portfolio.ru"
            },
            "photo": "/images/student1.jpg",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
            "userId": 1
        },
        {
            "id": 2,
            "name": "Мария Петрова",
            "course": 3,
            "status": "studying",
            "description": "Frontend-разработчик, специалист по React",
            "fullInfo": "Студентка 3 курса, создала несколько проектов на React.",
            "skills": ["JavaScript", "React", "HTML", "CSS"],
            "links": {
                "github": "https://github.com/maria",
                "portfolio": "https://maria-dev.ru"
            },
            "photo": "/images/student2.jpg",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
            "userId": 2
        }
    ]

    # Сохраняем
    with open('data/users.json', 'w', encoding='utf-8') as f:
        json.dump(users_data, f, ensure_ascii=False, indent=2)

    with open('data/students.json', 'w', encoding='utf-8') as f:
        json.dump(students_data, f, ensure_ascii=False, indent=2)

    print("✅ База данных пересоздана!")
    print(f"\n👤 Админ: admin / admin123")
    print(f"👨‍🎓 Студент: student1 / student123")
    print(f"🔑 Хэши: SHA256")


if __name__ == '__main__':
    fix_passwords()