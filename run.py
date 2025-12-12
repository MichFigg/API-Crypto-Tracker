import os
from dotenv import load_dotenv
load_dotenv()

print("API Crypto Tracker + Airflow uruchomiony!")
print("Airflow UI → http://localhost:8080 (admin/admin)")
print(f"API_KEY załadowany: {'Tak' if os.getenv('API_KEY') else 'Nie'}")

import time
while True:
    time.sleep(60)