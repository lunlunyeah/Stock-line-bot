import os

print("台股機器人啟動")

token = os.getenv("CHANNEL_ACCESS_TOKEN")

if token:
    print("✅ CHANNEL_ACCESS_TOKEN OK")
else:
    print("❌ CHANNEL_ACCESS_TOKEN Missing")
