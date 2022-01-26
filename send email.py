# 要先去google裡面的安全性  申請一個應用程式密碼
import email.message
from http import server
msg = email.message.EmailMessage()
msg["From"] = "qaz56115624@gmail.com"
msg["To"] = "qaz56115624@gmail.com"
msg["Subject"] = "你好,鳴哨"
# 寄送純文字的內容
msg.set_content("測試看看")
#寄送到比較多樣式的內容
# msg.add_alternative("<h3>優惠卷</h3>滿500送100" ,subtype = "html")
# 連線到 SMTP Server ,驗證寄件人身分並發送郵件
import smtplib
# 到網路上搜索 gmail smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("qaz56115624@gmail.com","密碼")
server.send_message(msg)
server.close()