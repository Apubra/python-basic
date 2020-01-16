from datetime import datetime
import pytz
tz_Dhaka = pytz.timezone('Asia/Dhaka')
datetime_Dhaka = datetime.now(tz_Dhaka)
print("Dhaka time:", datetime_Dhaka.strftime("%I:%M:%S %p"))
print(datetime_Dhaka.date())