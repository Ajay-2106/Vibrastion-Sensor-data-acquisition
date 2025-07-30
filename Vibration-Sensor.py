import serial
import time
import csv
import pandas as pd

# === Configuration ===
PORT = 'COM3'         # change the port number
BAUD_RATE = 9600
CSV_FILE = 'B:/Sensor_Data/Vib_sen_data.csv' # Chage the path to save the data===
RECORD_DURATION = 10  # seconds to collect data

# === Initialize Serial Connection ===
try:
    sensor = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(5)  # Wait for the connection to establish
except Exception as e:
    print(f"Error: Could not connect to {PORT}. {e}")
    exit()

# === Prepare Data Storage ===
timestamps = []
values = []

# === Setup CSV File ===
with open(CSV_FILE, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Time (s)", "Voltage (V)"])

# === Data Collection ===
print("Collecting data...")
start_time = time.time()

while (time.time() - start_time) < RECORD_DURATION:
    try:
        raw = sensor.readline().decode('utf-8').strip()
        if raw:
            value = float(raw)
            current_time = round(time.time() - start_time, 3)

            timestamps.append(current_time)
            values.append(value)

            # Write to CSV
            with open(CSV_FILE, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([current_time, value])
    except Exception as e:
        print(f"Data read error: {e}")

# === Cleanup ===
sensor.close()
print("Data collection complete.")