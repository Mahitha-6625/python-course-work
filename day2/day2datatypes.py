Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#integer
product_quantity = 3
order_id = 10987432
type(product_quantity)
<class 'int'>
type(order_id)
<class 'int'>
product_price = 749.99
discount_percentage = 15.5
average_rating = 4.3
type(product_price)
<class 'float'>
type(average_rating)
<class 'float'>
#complex
z = 5 + 2j
type(z)
<class 'complex'>
# sequence type
#str
customer_name = "Rohit Sharma"
delivery_address = "Bangalore, Karnataka"
product_category = "Electronics"
type(customer_name)
<class 'str'>
type(delivery_address)
<class 'str'>
type(product_category)
<class 'str'>
#list
cart_items = ["Shoes", "T-shirt", "Headphones"]
top_categories = ["Mobiles", "Fashion", "Home", "Beauty"]
#tuple
type(cart_items)
<class 'list'>
type(top_categories)
<class 'list'>
#tuple
product_dimensions = (12.5, 9.8, 2.2)
popular_brands = {"Nike", "Adidas", "Puma", "Nike"}
tpe(product_dimensions)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tpe(product_dimensions)
NameError: name 'tpe' is not defined. Did you mean: 'type'?
type(product_dimensions)
<class 'tuple'>
>>> type(popular_brands)
<class 'set'>
>>> frozen_tags = frozenset(["Sale", "Limited Edition",
... "Trending"])
>>> type(frozen_tags)
<class 'frozenset'>
>>> #mapping
>>> product_details = {
... "name": "Wireless Mouse",
... "brand": "Logitech",
... "price": 899.99,
... "rating": 4.5
... }
>>> type(product_details)
<class 'dict'>
>>> customer_profile = {
... "name": "Anjali Verma",
... "email": "anjali@example.com",
... "prime_member": True
... }
>>> type(customer_profile)
<class 'dict'>
>>> # boolean
>>> is_logged_in = True
>>> is_payment_successful = False
>>> is_in_stock = True
>>> type(is_logged_in)
<class 'bool'>
>>> type(is_payment_successful)
<class 'bool'>
>>> type(is_in_stock)
<class 'bool'>
>>> #none
>>> tracking_number = None
>>> delivery_partner = None
>>> type(tracking_number)
<class 'NoneType'>
>>> type(delivery_partner)
<class 'NoneType'>
