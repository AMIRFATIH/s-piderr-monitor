import requests
import time
from datetime import datetime

TOKEN = "8380316014:AAE2J4rsAf0CRz0HETXM_Tu5aa5kN9AIZfs"
CHAT_ID = "6831429027"
TARGET = "S_PIDERRBot"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, json=data)
    except:
        pass

print("🤖 شروع ربات...")
send("🚀 ربات شروع شد!\n🎯 @" + TARGET)

count = 0
while True:
    count += 1
    now = datetime.now().strftime("%H:%M:%S")
    
    if count % 6 == 0:
        send(f"⏰ {now}\n✅ مانیتور @{TARGET}")
    
    print(f"چک #{count} - {now}")
    time.sleep(600)
