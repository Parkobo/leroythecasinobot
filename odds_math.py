import time
import pickle_handler
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

workshop_items = ["Expanded Helicopter Events", "Susceptible Trait - Airborne Infection", "KaisResourceRecipes", "Skill Recovery Journal",
"Easy Config Chucked","STALKER Armor Pack","Antibodies", "'86 Oshkosh P19A + Military Trailers", "More Description for Traits", 
"Repair Any Clothes", "Better Sorting", "Firearms B41", "buffy's roleplay chat", "Manage Containers", "Moodle Fractions",
"50% Wood Weight", "Gun Suicide", "More Builds", "Fencing Kits!", "Tsar's Common Library", "'92 AM General M998 + M101A3 Cargo trailer",
"No Stunlocks", "Backpack Borders", "Adrenaline - Panic Counters Tiredness", "Fuel Side Indicator", "Has Been Read", "Immersive Solar Arrays",
"Snow is water", "Harry's Tow Truck", "Arsenal(26) GunFighter Mod", "Extra Map Symbols", "Just Throw Them Out The Window", "ExtraSauce Instant Consolidation",
"Spear Traps", "Clothes BOX", "Fixed Craftable Axes", "Military Ponchos", "Containers!", "Autotsar", "True Actions", "Scrap", "The Workshop",
"Irrigation pipes for farming", "Weapon Condition Indicator", "Armored Vests", "Rain Wash", "Repairing Metal Weapons", "Mod Options", 
"Axe's Recrafting", "Faster Hood Opening", "Improved Build Menu", "Crashed Cars Mod", "Reading is not boring", "Vehicle Parts Repair",
"Item Tweaker API", "Immersive Overlays"]

def workshop_scanner():
    print('Scanning workshop for updates')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    subscribed_page = config('steam_workshop', default='')
    driver_path = config('file_path_driver', default='')
    steam_user = config('steam_username', default='')
    steam_passwd = config('steam_password', default='')

    s = Service(driver_path)
    web_form = webdriver.Chrome(service=s, options=chrome_options)
    web_form.get(subscribed_page)
    web_form.maximize_window()

    web_form.find_element(by=By.XPATH, value='/html/body/div[1]/div[7]/div[4]/div[1]/div/div[1]/div/div/div/div/form/div[1]/input').send_keys(steam_user)
    web_form.find_element(by=By.XPATH, value='/html/body/div[1]/div[7]/div[4]/div[1]/div/div[1]/div/div/div/div/form/div[2]/input').send_keys(steam_passwd)
    web_form.find_element(by=By.XPATH, value='/html/body/div[1]/div[7]/div[4]/div[1]/div/div[1]/div/div/div/div/div[3]/div[1]/button').click()
    time.sleep(2)
    new_timestamp = web_form.find_element(by=By.XPATH, value="//*[contains(text(), 'Last Updated ')]").text
    workshop_title = web_form.find_element(by=By.XPATH, value='/html/body/div[1]/div[7]/div[2]/div[1]/div[1]/div[5]/div[2]/div/div[5]/div/div[2]/a/div').text
    prev_timestamp = pickle_handler.load_content()

    if (new_timestamp != prev_timestamp):
        print('Detected the need for update')
        pickle_handler.update_content(new_timestamp)

        for w in workshop_items:
            if (w in workshop_title):
                print (f"The {w} mod needs an update!")
                web_form.quit()
                return True

    else:
        print('Did not locate an update')
        web_form.quit()
        return False