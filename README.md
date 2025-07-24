# 🌡️ IoT Monitoring Suhu & Kelembapan Virtual (ESP32 + DHT22 + Wokwi + Adafruit IO)

Proyek ini adalah simulasi sistem monitoring suhu dan kelembapan menggunakan **sensor DHT22** yang terhubung ke **ESP32**, dengan data yang dikirim ke **Adafruit IO** menggunakan protokol MQTT. Semua pengujian dilakukan secara virtual menggunakan **Wokwi Simulator**.

---

## 🧰 Peralatan dan Teknologi

- 🧠 **Mikrokontroler:** ESP32 DevKit v4
- 🌡️ **Sensor:** DHT22
- 🖥️ **Simulasi:** [Wokwi](https://wokwi.com)
- 📡 **Protokol:** MQTT (via `umqtt.simple`)
- ☁️ **Platform IoT:** [Adafruit IO](https://io.adafruit.com)
- 🐍 **Bahasa:** MicroPython

---

## 🗂️ Struktur File

| File | Deskripsi |
|------|-----------|
| `main.py` | Script utama MicroPython yang membaca sensor dan mengirim data ke Adafruit IO |
| `diagram.json` | Diagram simulasi Wokwi (ESP32 + DHT22) |
| `wokwi-project.txt` | Link langsung ke proyek simulasi di Wokwi |

---

## 🔌 Wiring & Skematik

Berikut adalah koneksi antar komponen di dalam file `diagram.json`:

- DHT22 `VCC` → ESP32 `3V3`
- DHT22 `GND` → ESP32 `GND`
- DHT22 `SDA` → ESP32 `GPIO15`

Simulasi dapat diakses di:  
🔗 [https://wokwi.com/projects/437256411960400897](https://wokwi.com/projects/437256411960400897)

---

## 🚀 Langkah-Langkah Implementasi

### 1. Simulasi di Wokwi
1. Buka [Wokwi](https://wokwi.com)
2. Unggah file `diagram.json` dan `main.py`
3. Simulasikan proyek (klik ▶️)
4. Monitor serial akan menampilkan data suhu & kelembapan virtual

### 2. Buat Akun Adafruit IO
1. Kunjungi [io.adafruit.com](https://io.adafruit.com)
2. Buat akun (gratis)
3. Dapatkan:
   - **Username**
   - **AIO Key** (di `My Key`)

### 3. Buat Feed di Adafruit IO
Buat dua feed:
- `suhu`
- `kelembapan`

> Format topik MQTT:  
> `username/feeds/suhu`  
> `username/feeds/kelembapan`

### 4. Ubah Konfigurasi di `main.py`
Ganti baris berikut dengan milik Anda:
```python
ADAFRUIT_IO_USERNAME = "username_anda"
ADAFRUIT_IO_KEY = "aio_your_key"
