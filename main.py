from bs4 import BeautifulSoup
import requests
# import pprint
import lxml
import smtplib
import os

TARGET_PRICE = 275.00
PRODUCT_LINK = "https://www.amazon.com/Moondrop-Blessing2-Technology-Monitor-Earphone/dp/B0836C6LQ8"

header = {
    "Accept-Language": os.environ["ACCEPT_LANG"],
    "user-agent": os.environ["USER_AGENT"],
}
response = requests.get(PRODUCT_LINK,
                        headers=header)

soup = BeautifulSoup(response.text, 'lxml')

price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))
product_name = soup.find(name="span", id="productTitle", class_="a-size-large").getText().strip("  ")

if price < TARGET_PRICE:

    msg = f"""Hello Amir, your item {product_name} is available and the price is now below your target price [{TARGET_PRICE}], and is now priced at ${price}.
            Here is the link to your desired product: {PRODUCT_LINK}.  
    """
    try:
        with smtplib.SMTP(os.environ['HOST'], port=587) as conn:
            conn.starttls()
            conn.set_debuglevel(1)
            conn.login(user=os.environ['EMAIL'], password=os.environ['PASSWORD'])
            conn.sendmail(
                from_addr=os.environ['EMAIL'],
                to_addrs="amrrzk02@gmail.com",
                msg=msg
            )

        print("Message sent")
    except smtplib.SMTPException:
        print("Error: unable to send email")