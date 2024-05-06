
# **Vendor Management System with Performance Metrics**

### **Objective**
Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

### **Technologies Used**

 - Argon2 Hasher
 - Django
 - Djanog Jazzmin Dashboard
 - Django Rest Framework
 - Swagger UI Playgroud

### **Setup**

**Step 1:** Download Python 3.12 from the official website `https://www.python.org/`

**Step 2:** Verify successful installation by running the following command:
```cmd
python
```

Example:
```cmd
F:\> python
```

Desired Output:
```cmd
F:\> python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Step 3:** Open the terminal at the desired location and the run the following command to clone the repository:
```cmd
F:\> git clone https://github.com/DataRohit/Vendor-Management-System.git
```

**Step 4:** Navigate to `Vendor-Management-System` and open the terminal at the folder:
```cmd
F:\> cd Vendor-Management-System

F:\Vendor-Management-System>
```

**Step 5:** Create a new virtual environment by running the following command:
```cmd
F:\Vendor-Management-System> python -m venv venv
```

**Step 6:** Activate the virtual enviroment:
```cmd
F:\Vendor-Management-System> venv\Scripts\activate

(venv) F:\Vendor-Management-System>
```

**Step 7:** Now install requirements from the `requirements.txt`:
```cmd
(venv) F:\Vendor-Management-System> pip install -r requirements.txt
```

**Step 8:** Create folder for database:
```cmd
(venv) F:\Vendor-Management-System> mkdir database
```

**Step 9:** Rename the `.env.local` to `.env`
```cmd
(venv) F:\Vendor-Management-System> rename ".env.local" ".env"
```

**Step 10:** Make migrations
```cmd
(venv) F:\Vendor-Management-System> python manage.py makemigrations core performance purchase_orders vendors

(venv) F:\Vendor-Management-System> python manage.py migrate
```

**Step 10:** Create a superuser to access the django admin terminal
```cmd
(venv) F:\Vendor-Management-System> python manage.py createsuperuser
```

**Step 11:** Run the server:
```cmd
(venv) F:\Vendor-Management-System> python manage.py runserver
```

### **Swagger UI Playground**

Swagger UI URL: `http://127.0.0.1:8000/`
Detailed API Docs: `http://127.0.0.1:8000/redoc/`

All the API Endpoints can be viewed and tested from here.