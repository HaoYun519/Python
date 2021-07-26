# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="new0519102@gmail.com" #@gmail.com
msg["To"]="new0519102@gmail.com"
msg["Subject"]="你好, 練習用程式碼發送信件!"
# 寄送純文字的內容
# msg.set_content("測試看看")
# 寄送比較多樣式的內容 (html)
msg.add_alternative("<h3>優惠券</h3>滿五百送一百哦", subtype="html")
# 連線到 SMTP Server, 驗證寄件人身份並發送郵件
import smtplib
# 到網路上搜尋 gmail smtp server or yahoo smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("帳號", "密碼")
server.send_message(msg)
server.close()