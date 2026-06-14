# 🚗 IoT Vehicle Tracking & Theft Prevention System

## 📌 Overview

The IoT Vehicle Tracking & Theft Prevention System is an IoT-based security solution that tracks vehicle location in real time and detects unauthorized movement using geofencing. The system simulates GPS coordinates, generates theft alerts, stores location history, and displays live tracking on a dashboard.

This project is implemented using Python simulation and Streamlit without requiring actual hardware or datasets.

---

## 🎯 Problem Statement

Vehicle theft and lack of real-time monitoring are major concerns for vehicle owners and fleet operators. Traditional tracking systems are expensive and require specialized hardware.

This project provides:

* Real-time vehicle tracking
* Theft detection using geofencing
* Live dashboard visualization
* Automatic location logging

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* Folium
* Streamlit-Folium
* NumPy
* Git & GitHub

---

## 📡 IoT Concepts Used

* GPS Tracking
* Geofencing
* Real-Time Monitoring
* Cloud Dashboard
* Alert Generation
* Data Logging
* Vehicle Security

---

## 📂 Project Structure

```text
Vehicle_Tracking_Theft_Prevention_System
│
├── code
│      vehicle_tracking.py
│
├── data
│      location_history.csv
│
├── ui
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ✨ Features

✅ GPS Coordinate Simulation

✅ Real-Time Tracking

✅ Google Maps Link Generation

✅ Geofence Detection

✅ Theft Alert Generation

✅ CSV Logging

✅ Interactive Map Dashboard

---

## 🔄 Workflow

```text
GPS Simulation
      ↓
Location Tracking
      ↓
Geofence Detection
      ↓
Theft Alert Generation
      ↓
CSV Logging
      ↓
Dashboard Visualization
```

---

## 🏗 Architecture

```text
GPS Coordinates
       ↓
Python Simulation
       ↓
Geofence Engine
       ↓
Alert System
       ↓
CSV Logging
       ↓
Streamlit Dashboard
```

---

## 🚨 Theft Detection Logic

The system defines a safe zone using base coordinates.

If the vehicle moves outside the safe zone:

* Status = THEFT ALERT 🚨
* Alert is displayed on dashboard
* Location is logged

---

## 📍 Google Maps Integration

The project automatically generates map links:

```text
https://www.google.com/maps?q=latitude,longitude
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/IoT-Vehicle-Tracking-Theft-Prevention-System.git
cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

### Run GPS Simulation

```bash
cd code
python vehicle_tracking.py
```

### Run Dashboard

Open another terminal:

```bash
streamlit run main.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## 📊 Sample Output

```text
Latitude  : 17.386250
Longitude : 78.488120
Status    : SAFE ✅

Map Link:
https://www.google.com/maps?q=17.386250,78.488120
```

---

## 📁 Data Logging

Vehicle location history is automatically stored in:

```text
data/location_history.csv
```

No external dataset is required.

---

## 📷 Screenshots to Add

Place screenshots inside the `ui/` folder:

* Dashboard Screenshot
* Live Map Screenshot
* Theft Alert Screenshot
* CSV File Screenshot
* GitHub Repository Screenshot

---

## 🌍 Real-World Applications

* Fleet Management
* Vehicle Theft Prevention
* School Bus Monitoring
* Delivery Vehicle Tracking
* Logistics Monitoring

---

## 🔮 Future Improvements

* ESP32 Integration
* GPS Hardware Support
* MQTT Communication
* SMS Alerts
* Engine Lock/Unlock
* Mobile App Integration

---

## 📚 Learning Outcomes

Through this project, I learned:

* IoT Concepts
* GPS Tracking
* Geofencing
* Dashboard Development
* Data Logging
* Git & GitHub

---

## 👨‍💻 Author

**Neethu**

IoT | Python | Vehicle Security | Automation

---

⭐ If you like this project, give it a star!
