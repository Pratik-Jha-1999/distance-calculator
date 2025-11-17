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

## ⚙️ Backend Setup

1. Create virtual environment  
2. Install dependencies  
3. Setup PostgreSQL  
4. Update DB credentials  
5. Run backend:

```
uvicorn main:app --reload
```

## 🎨 Frontend Setup

```
cd frontend
npm install
npm start
```

## 🔌 API Endpoints

### GET /distance
Calculates and stores distance.

### GET /history
Returns all stored queries.

## 📝 Logging
Logs all events to `app.log`.

## 📄 License
MIT License.
