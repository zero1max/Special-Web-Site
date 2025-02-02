# Special-Web-Site

Bu veb-sayt **Cambridge o'quv markazi**da ishlovchi o'qituvchi uchun yaratilgan. Veb-sayt **Django** frameworkida qurilgan va **SQLite3** ma'lumotlar bazasidan foydalanadi. Veb-saytning asosiy maqsadi - yangi o'quvchilar va veb-sayt egasi tanigan insonlar uchun o'qituvchi haqida to'liq ma'lumot olish imkoniyatini yaratish.

## Veb-saytning imkoniyatlari

- **O'qituvchi haqida to'liq ma'lumot**:
  - O'qituvchining tajribasi, malakasi, o'quv markazidagi faoliyati va boshqa muhim ma'lumotlar.
- **Yangi o'quvchilar uchun ma'lumot**:
  - O'quv markazi haqida umumiy ma'lumot, kurslar va o'qituvchilar haqida ma'lumot.
- **Foydalanuvchilar uchun qulaylik**:
  - Veb-sayt egasi tanigan insonlar o'qituvchi haqida to'liq ma'lumot olishlari mumkin.

## Texnologiyalar

- **Django** - Python dasturlash tili uchun kuchli veb-framework.
- **SQLite3** - Yengil va samarali ma'lumotlar bazasi.
- **HTML/CSS/JavaScript** - Veb-saytning frontend qismi.

## O'rnatish

Loyihani mahalliy muhitda ishga tushirish uchun quyidagi qadamlarni bajaring:

1. Repozitoriyani klonlang:
   ```bash
   git clone https://github.com/foydalanuvchi/Special-Web-Site.git
   cd Special-Web-Site

2. Virtual muhit yarating va faollashtiring:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows uchun venv\Scripts\activate

3. Zarur paketlarni o'rnating:
    ```bash
    pip install -r requirements.txt

4. Ma'lumotlar bazasini migratsiya qiling:
    ```bash
    python manage.py migrate

5. Superuser yarating (admin paneliga kirish uchun):
    ```bash
    python manage.py createsuperuser

6. Loyihani ishga tushiring:
    ```bash
    python manage.py runserver

7. Veb-saytni brauzerda oching:
    ```bash
    http://127.0.0.1:8000/

8. Admin panel ga kirish:
    ```bash
    http://127.0.0.1:8000/admin/