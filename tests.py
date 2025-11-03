from ContactPages import ContactPage

def test_form():
    form_page = ContactPage()
    form_page.go_to_site()
    form_page.enter_name("Maxim")
    form_page.enter_age(21)
    form_page.enter_email("max@mail.ru")
    form_page.enter_number(12345)
    form_page.click_on_submit_button()
    result = form_page.check_validation()
    
    print(result)

def test_negative_form():
    form_page = ContactPage()
    form_page.go_to_site()
    form_page.enter_age(21)
    form_page.enter_email("max@mail.ru")
    form_page.enter_number(12345)
    form_page.click_on_submit_button()
    result = form_page.check_validation()

    print(result)