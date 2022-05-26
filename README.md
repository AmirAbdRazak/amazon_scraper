# amazon_scraper
Scrapes a product on Amazon and notifies the user through email if the product falls below a set target price.

Video of it working: https://youtu.be/sEiNE_Udt8w 

Project workflow:

1) Scrape the product price and product name through Beautiful Soup 4 on Amazon.
2) Compare it against the target price you set, you can check it on https://www.camelcamelcamel.com to set the target price.
3) Email the user if the price is below the target price, SMTP will manage sending the email. 
