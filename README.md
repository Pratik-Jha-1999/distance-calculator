# 📍 Distance Calculator — FastAPI + React + PostgreSQL

A full-stack web application that calculates the distance between two addresses using the OpenStreetMap Nominatim API, stores each query in a PostgreSQL database, and displays historical results in a React UI.

## 🚀 Features

### Backend (FastAPI)
- Geocoding using Nominatim API  
- Distance calculation using Haversine formula  
- PostgreSQL storage using SQLAlchemy  
- History endpoint  
- Error handling (invalid address, API timeout, DB failure)  
- Logging using RotatingFileHandler  

### Frontend (React)
- Distance calculator UI  
- Historical queries table  
- Toast error notifications  
- Pure CSS styling (no external UI libs)

## 🏗️ Tech Stack
- **Frontend:** React, JavaScript, CSS  
- **Backend:** FastAPI, Python, SQLAlchemy, PostgreSQL  
- **Geocoding:** OpenStreetMap Nominatim API  

## 📂 Project Structure

```
backend/
│── main.py
│── database.py
│── table_model.py
│── repository.py
│── calculations.py
│── app.log
│── requirements.txt
│
frontend/
│── src/
│   ├── App.js
│   ├── components/
│   │   ├── Header.js
│   │   ├── Calculator.js
│   │   ├── HistoryTable.js
│   │   └── ErrorToast.js
│   ├── App.css
│   └── index.js
│── package.json
│
README.md
```
---

# ⚙️ 1. Backend Setup (FastAPI + PostgreSQL)

### Step 1 — Navigate to backend folder
cd backend

### Step 2 — Create a virtual environment
python3 -m venv myenv
source myenv/bin/activate     # macOS/Linux
myenv\Scripts\activate      # Windows

### Step 3 — Install dependencies
pip install -r requirements.txt

### Step 4 — Configure PostgreSQL database

Create a database:
CREATE DATABASE distances;

Add credentials in `.env`:
API_PASSWORD=your_api_password
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=distances

### Step 5 — Start backend
uvicorn main:app --reload

Backend available at:
http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/docs

---

# 🎨 2. Frontend Setup (React)

### Step 1 — Navigate to frontend folder
cd frontend

### Step 2 — Install dependencies
npm install

### Step 3 — Start frontend
npm start

Frontend available at:
http://localhost:3000

---

# 🔐 3. API Authentication

Both `/distance` and `/history` require an API key.

Send it via header:
X-API-Key: your_api_password

In React:
headers: { "X-API-Key": process.env.REACT_APP_API_KEY }

---

# 📦 4. Frontend Environment Variables

Create `frontend/.env`:
REACT_APP_API_KEY=your_api_password
REACT_APP_BACKEND_URL=http://127.0.0.1:8000

Restart frontend after creating `.env`.

---

# 🧪 5. Test API Manually
curl -H "X-API-Key: your_api_password" http://127.0.0.1:8000/history

---

## 🔌 API Endpoints

### GET /distance
Calculates and stores distance.

### GET /history
Returns all stored queries.

## 📝 Logging
Logs all events to `app.log`.

## 📄 License
MIT License.
