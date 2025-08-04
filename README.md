# CareConnect - A Django-Based Healthcare Communication Portal 🏥💬

CareConnect is a web-based healthcare communication platform designed for Patients and Doctors to interact effectively. The system supports user authentication, appointment management, secure chat, medical document uploads, and role-based dashboards.

---

## 🌟 Key Features

### 👥 User Management
- **Two User Roles**: 
  - 🧑‍⚕️ Doctor
  - 🧑‍💼 Patient
- **Signup Form** with validations:
  - First Name & Last Name
  - Username & Email
  - Profile Picture Upload
  - Password and Confirm Password (match validation)
  - Full Address (Line1, City, State, Pincode)

### 🔐 Authentication
- Secure login/logout with Django’s authentication system.
- Redirect users to their respective dashboards after login based on role.

### 📋 Dashboards
- **Patient Dashboard**:
  - Displays user profile and booked consultations.
  - Option to book new consultations.
- **Doctor Dashboard**:
  - Displays user profile.
  - View and accept consultation requests.
  - View upcoming and past appointments.

### 📅 Appointments
- Patients can book appointments with available doctors.
- Doctors can **accept** or **reject** appointments.
- Appointments are displayed with timestamps in both dashboards.

### 💬 Chat Functionality
- Real-time messaging (on refresh) between Doctor and Patient.
- Separate conversation view for each user pair.
- Displays message content, sender, and timestamp.

### 📁 Medical Document Upload
- Patients can upload medical reports/documents.
- Doctors can view documents uploaded by patients.

### 📸 Media Uploads
- Profile Pictures and Documents are stored in `media/` using Django’s `MEDIA_ROOT`.

---

## 💻 Technologies Used

| Technology      | Purpose                         |
|------------------|----------------------------------|
| Python 3.x       | Backend Language                |
| Django 5.x       | Main Web Framework              |
| SQLite3          | Database (Default Django DB)    |
| HTML5, CSS3      | Frontend Markup and Styling     |
| Bootstrap        | UI Enhancements (optional)      |
| JavaScript       | DOM Manipulation (for chat scroll) |
| Pillow           | Image Upload Handling           |
| Git & GitHub     | Version Control and Hosting     |

---

### 📦 Prerequisites

- Python 3.x
- Pip
- Git
- Virtualenv (recommended)

### 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/ChanduMucharla/CareConnect-BlastUIC.git
cd CareConnect-BlastUIC

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional for admin access)
python manage.py createsuperuser

# Start development server
python manage.py runserver

## 🗂️ Project Structure
## 👨‍💻 Developer Info

**Developed by**:  
**Chandu Naga Sai Jyothi Mucharla**  
📧 Email: [chandumucharla09@gmail.com](mailto:chandumucharla09@gmail.com)  
🎓 Final Year BTech, Computer Science  
🚀 Passionate about Full Stack Web Development, Android, and Data Science

---

## ©️ Copyright

© 2025 Chandu Naga Sai Jyothi Mucharla. All Rights Reserved.  
