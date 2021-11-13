from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
for i in range(1, 14):
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{i}-noiembrie-ora-13-00/")

    table = browser.find_elements(By.TAG_NAME, 'tbody')[0]
    rows = table.find_elements(By.TAG_NAME, 'tr')

    result = []
    for item in rows:
        result.append(list(map(lambda x: x.text, item.find_elements(By.TAG_NAME, 'td'))))

    df = pd.DataFrame(result[1:], columns=result[0])
    df.to_csv(f'date_covid_{i}_noiembrie.csv', index=False)
