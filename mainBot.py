from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time



driver  = webdriver.Remote("http://127.0.0.1:9515",webdriver.DesiredCapabilities.CHROME)
urlStart = "http://www.supremenewyork.com/shop/all/accessories"
driver.get(urlStart)

regex = re.compile('Supreme.*Hanes.*Tees.*\nWhite')

info = {'name': 'First Last', 'email':'mail@email.com', 'tel':'(520)-520-520', 'address':'1234 Test Ave',
        'zip': '12345', 'city':'Ciudad', 'credit':'4567897612340697', 'cvv':'222'}

foundProduct = False
while foundProduct != True:

    allLinks = driver.find_elements_by_class_name('inner-article')
    for links in allLinks:

        match =regex.match(links.text)
        if match:
            foundProduct = True
            links.click()


time.sleep(.25)
# Found our product so go to the products purchase page
wrap = driver.find_element_by_id('wrap')
cart_addf = wrap.find_element_by_id('cart-addf')
size = cart_addf.find_element_by_id('s')

sizeOptions = size.find_elements_by_tag_name('option')


for options in sizeOptions:
    if options.text == 'Large':
        options.click()

add_cart = cart_addf.find_element_by_name('commit')
add_cart.click()

time.sleep(.2)
driver.get("https://www.supremenewyork.com/checkout")

check_out_form = driver.find_element_by_id('checkout_form')


nameField = check_out_form.find_element_by_class_name('order_billing_name')
nameField.click()
nameField.send_keys("Test")



#print(inputFields)




