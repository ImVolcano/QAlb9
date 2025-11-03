from BaseApp import BasePage
from selenium.webdriver.common.by import By

class FormLocators:
    LOCATOR_NAME_FIELD = (By.ID, "name")
    LOCATOR_AGE_FIELD = (By.ID, "age")
    LOCATOR_EMAIL_FIELD = (By.ID, "email")
    LOCATOR_NUMBER_FIELD = (By.ID, "number")
    LOCATOR_SUBMIT_BUTTON = (By.ID, "submitbtn")

class ContactPage(BasePage):

    def enter_name(self, word):
        name_field = self.find_element(FormLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(word)
        return name_field
    
    def enter_age(self, age):
        age_field = self.find_element(FormLocators.LOCATOR_AGE_FIELD)
        age_field.send_keys(age)
        return age_field
    
    def enter_email(self, email):
        email_field = self.find_element(FormLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        return email_field

    def enter_number(self, number):
        number_field = self.find_element(FormLocators.LOCATOR_NUMBER_FIELD)
        number_field.send_keys(number)
        return number_field

    def click_on_submit_button(self):
        return self.find_element(FormLocators.LOCATOR_SUBMIT_BUTTON,time=2).click()

    def check_validation(self):
        name_msg = self.find_element(FormLocators.LOCATOR_NAME_FIELD).get_attribute("validationMessage")
        age_msg = self.find_element(FormLocators.LOCATOR_AGE_FIELD).get_attribute("validationMessage")
        email_msg = self.find_element(FormLocators.LOCATOR_EMAIL_FIELD).get_attribute("validationMessage")
        number_msg = self.find_element(FormLocators.LOCATOR_NUMBER_FIELD).get_attribute("validationMessage")

        if(name_msg != ""): return "Invalid name"
        elif(age_msg != ""): return "Invalid age"
        elif(email_msg != ""): return "Invalid email"
        elif(number_msg != ""): return "Invalid number"

        return "All valid"