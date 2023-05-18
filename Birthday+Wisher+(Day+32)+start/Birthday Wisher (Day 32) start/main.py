import smtplib
my_email = "sben834520@gmail.com"
password = "Berriane_47"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="benabdallah.slimane@gmail.com",
                        msg="Subject:Hello from app\n\nThis is the body of my email.")
