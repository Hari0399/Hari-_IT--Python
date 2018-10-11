import smtplib
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login("harishay01@gmail.com", "Thiruhari@1")


msg = "hi"

server.sendmail("harishay01@gmail.com", "ikhlaasrasib@gmail.com", msg)
server.quit()
