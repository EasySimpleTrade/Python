'''
VALLAKKOTTAI MURUGAN THUNAI
Easy Simple Trading Solutions
Telegram @easysimpletrade
Website https://easysimpletrade.blogspot.com
Youtube https://www.youtube.com/@easysimpletrade
GitHub https://github.com/EasySimpleTrade
'''

from pyotp import TOTP

totpkey = 'MVQXG6LTNFWXA3DFORZGCZDF'
otp = TOTP(totpkey).now().zfill(6)
print(otp)

# Keep the command prompt open after printing the OTP
input("Press Enter to exit...")
