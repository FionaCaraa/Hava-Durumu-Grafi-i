import requests
import matplotlib.pyplot as plt
import datetime

# OpenWeatherMap API bilgilerimiz
API_KEY = "b75ce903ab24462cefc267be687ceaa5"
CITY = "Istanbul"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# API isteğimiz
response = requests.get(URL)
data = response.json()

# Sıcaklık ve zaman bilgilerini işliyoruz
temperatures = []
timestamps = []

for item in data['list']:
    temperatures.append(item['main']['temp'])  # Sıcaklık
    timestamps.append(datetime.datetime.fromtimestamp(item['dt']).strftime('%d-%m %H:%M'))  # Zaman

# Grafik oluşturuyoruz
plt.figure(figsize=(12, 6))
plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='b')

# Grafik başlıkları ve etiketleri ekliyoruz
plt.title(f"{CITY} 3 Saatlik Aralıklarla Hava Durumu Tahmini", fontsize=16)
plt.xlabel("Zaman", fontsize=12)
plt.ylabel("Sıcaklık (°C)", fontsize=12)
plt.xticks(rotation=45)  # X eksenini eğik göster
plt.grid(True)
plt.tight_layout()

# Grafiğin ekran görüntüsü isteniyor
plt.show()
