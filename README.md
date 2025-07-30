# 📈 Serial Sensor Data Logger – Python

This project logs real-time analog voltage data from a serial device (e.g., Arduino with a sensor) and stores it in a CSV file for analysis. The script is lightweight, easy to configure, and ideal for basic data acquisition tasks such as vibration sensing or sensor calibration.

---

## 🚀 Features
- Reads live sensor data via serial (e.g., COM3 at 9600 baud)
- Records voltage values with precise timestamps
- Stores the output in CSV format for further processing
- Automatically handles serial initialization and file setup
- Uses native Python libraries for maximum portability

---

## 🛠 Requirements
- Python 3.x
- Libraries: **pandas**, **pyserial**
