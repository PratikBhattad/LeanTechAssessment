class Locators:
    #loginpage
    username_textbox_id = 'user-name'
    password_textbox_id = 'password'
    login_btn_id = 'login-button'

    #homepage
    item_list = 'div.inventory_item'
    #add_to_cart_btn = "//div[@class='pricebar']/descendant::button"
    add_to_cart_btn = "div.pricebar button"
    cart_link_id = "a.shopping_cart_link"
    confirm_checkout_btn = "div.cart_footer > button.checkout_button"
    input_first_name = "input[placeholder='First Name']"
    input_last_name = "input[placeholder='Last Name']"
    input_zip_code = "input[placeholder= 'Zip/Postal Code']"
    submit_customer_info = "input[type='submit']"
    proceed_checkout_overview = "button[id='finish']"
    checkout_header = "span.title"