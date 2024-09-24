import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdressParser:
    def __init__(self, output_file):
        self.output_file = output_file
        self.driver = webdriver.Firefox()

    def close(self):
        self.driver.quit()

    def parse(self):
        self.driver.get('https://www.onlyoffice.com')

        about_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='navitem_about']"))
        )
        ActionChains(self.driver).move_to_element(about_link).perform()

        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='navitem_about_contacts']"))
        )
        contacts_link.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@itemtype='https://schema.org/PostalAddress']"))
        )

        data = []
        offices = self.driver.find_elements(By.XPATH, "//div[@itemtype='https://schema.org/PostalAddress']")

        for office in offices:
            country = office.find_element(By.XPATH, ".//span[@itemprop='addressLocality']").text.strip()
            company_name = office.find_element(By.XPATH, ".//span[b]").text.strip()
            full_address = office.find_element(By.XPATH, ".//span[@itemprop='addressCountry']").text.strip()
            data.append([country, company_name, full_address])

        self.save_to_csv(data)

    def save_to_csv(self, data):
        with open(self.output_file, 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Country', 'CompanyName', 'FullAddress'])
            writer.writerows(data)



if __name__ == "__main__":
    parser = AdressParser('addresses.csv')
    try:
        parser.parse()
    finally:
        parser.close()