from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import time

name = "Dandy Arya Akbar"
nim = "1313623028"
phone = "085776698343"

matkuldb = {
    'KALINT': {
        'fullname': 'Kalkulus Integral',
        'sectionnumber': '1313600002',
        'matkulcode': '31451063',
        'sks': '3',
        'lecturers': {
            'first': ("Dr. Ellis Salsabila, M.Si.", "E"),
            'second': ("Dr.  Flavia Aurelia Hidajat, S.Pd., M.Pd.", "F"),
        }
    },
    'ALIN': {
        'fullname': 'Aljabar Linier',
        'sectionnumber': '1313600023',
        'matkulcode': '31451043',
        'sks': '3',
        'lecturers': {
            'first': ("Ratna Widyati, S.Si. M.Kom.", "R")
        }
    },
    'DSA': {
        'fullname': 'Struktur Data dan Algoritma',
        'sectionnumber': '1313600025',
        'matkulcode': '31452033',
        'sks': '3',
        'lecturers': {
            'first': ("Med Irzal, S.Kom., M.Kom", "M"),
            'second': ("Muhammad Eka Suryana, S.Kom. M.Kom.", "M")
        }
    },
    'PSD': {
        'fullname': 'Pengantar Sistem Digital',
        'sectionnumber': '1313600007',
        'matkulcode': '31451103',
        'sks': '3',
        'lecturers': {
            'first': ("Ir. Fariani Hermin Indiyah, M.T.", "F")
        }
    },
    'PTG': {
        'fullname': 'Pengantar Teori Graph',
        'sectionnumber': '1313600024',
        'matkulcode': '31454113',
        'sks': '3',
        'lecturers': {
            'first': ("Drs. Mulyono, M.Kom.", "M")
        }
    },
    'FILSAFAT': {
        'fullname': 'Filsafat MIPA',
        'sectionnumber': '1313600003',
        'matkulcode': '31454132',
        'sks': '2',
        'lecturers': {
            'first': ("Dr.  Lukman El Hakim, M.Pd.", "L")
        }
    },
    'AGAMA': {
        'fullname': 'Pendidikan Agama Islam',
        'sectionnumber': '1000000057',
        'matkulcode': '00052242',
        'sks': '2',
        'lecturers': {
            'first': ("Khairil Ikhsan Siregar, M.A.", "K")
        }
    },
    'PKN': {
        'fullname': 'Pendidikan Kewarganegaraan',
        'sectionnumber': '1000000133',
        'matkulcode': '00051112',
        'sks': '2',
        'lecturers': {
            'first': ("Dr. Djunaidi, M.Hum.", "D")
        }
    },
    'WASPEND': {
        'fullname': 'Wawasan Pendidikan',
        'sectionnumber': '1000000391',
        'matkulcode': '00053182',
        'sks': '2',
        'lecturers': {
            'first': ("Dr.  Hanum Isfaeni, M.Si.", "H")
        }
    }
}

def clicknext():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Berikutnya']"))).click()

##matkul = "DSA"        DECOMMENT THESE LINES FOR TESTING
##nsession = "2"        DECOMMENT THESE LINES FOR TESTING
##nweek = "3"           DECOMMENT THESE LINES FOR TESTING

inputstrings = str(input("Enter input data here: ")).split()
matkul = inputstrings[0]
nsession = inputstrings[1]
nweek = inputstrings[2]

lecturers = matkuldb[matkul]['lecturers']
if len(lecturers) > 1:
    isMultiple = True
    i = 1
    print()
    print("Which lecturer taught you today?")
    for key, (fullname, initial) in lecturers.items():
        print(f"{i}: {fullname} ({initial})")
        i = i + 1
    while True:
        try:
            lecturerindex = int(input("Please enter a corresponding number: "))
            selectedlecturer = list(lecturers.keys())[lecturerindex - 1]
            lecturerfullname, lecturerinitial = lecturers[selectedlecturer]
            ##print()
            ##print(f"selectedfullname: {lecturerfullname}")
            ##print(f"selectedinitial: {lecturerinitial}")
            break
        except (ValueError, IndexError):
            print()
            print("Invalid selection.")
        finally:
            firstlecturer = lecturers['first'][0]
            secondlecturer = lecturers['second'][0]
            matkulcode = matkuldb[matkul]['matkulcode']
            matkulfullname = matkuldb[matkul]['fullname']
            sks = matkuldb[matkul]['sks']
            ##print()
            ##print(firstlecturer)
            ##print(secondlecturer)
            ##print(matkulcode)
            ##print(matkulfullname)
            ##print(sks)
            
else:
    isMultiple = False
    lecturerfullname, lecturerinitial = list(matkuldb[matkul]['lecturers'].values())[0]
    firstlecturer = lecturers['first'][0]
    matkulcode = matkuldb[matkul]['matkulcode']
    matkulfullname = matkuldb[matkul]['fullname']
    sks = matkuldb[matkul]['sks']

print()
print("Automating Attendance Process...")
print("Please Wait...")
service = Service(executable_path='E:\Personal Projects\Python\Autofilling Google Form Responses\chromedriver-win64\chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--disable-extensions')
##options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--disable-infobars')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://bit.ly/3SNZze0")

studentname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nama Mahasiswa']//following::input[1]")))
studentid = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='NIM']//following::input[1]")))
phonenumber = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='No. Handphone']//following::input[1]")))
studentname.send_keys(name)
studentid.send_keys(nim)
phonenumber.send_keys(phone)
clicknext()

facultybtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Fakultas Matematika dan Ilmu Pengetahuan Alam']//preceding::div[2]")))
dropitdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Pilih']")))
time.sleep(0.6)
dropitdown.click()
time.sleep(0.3)
bachelorbtn = driver.find_elements(By.XPATH, "//span[text()='S1']")
for i in bachelorbtn:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)
facultybtn.click()
clicknext()

dropitdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Pilih']")))
time.sleep(0.6)
dropitdown.click()
time.sleep(0.3)
majorbtn = driver.find_elements(By.XPATH, "//span[text()='(S1) Sistem Komputer']")
for i in majorbtn:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)
clicknext()

dropitdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Pilih']")))
time.sleep(0.6)
dropitdown.click()
time.sleep(0.3)
initialbtn = driver.find_elements(By.XPATH, f"//span[text()='{lecturerinitial}']")
for i in initialbtn:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)
clicknext()

dropitdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Pilih']")))
time.sleep(0.6)
dropitdown.click()
time.sleep(0.3)
fullnamebtn = driver.find_elements(By.XPATH, f"//span[text()='{lecturerfullname}']")
for i in fullnamebtn:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)
clicknext()

firstlecturerform = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nama Dosen 1']//following::input[1]")))
secondlecturerform = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nama Dosen 2']//following::input[1]")))
thirdlecturerform = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nama Dosen 3']//following::input[1]")))
firstlecturerform.send_keys(firstlecturer)
secondlecturerform.send_keys(secondlecturer) if isMultiple else None
clicknext()

finalforms = driver.find_elements(By.XPATH, "//div[text()='Jawaban Anda']//preceding::input[1]")
dropitdowns = driver.find_elements(By.XPATH, "//span[text()='Pilih']")
time.sleep(0.6)
finalforms[0].send_keys(matkulcode)
finalforms[1].send_keys(matkulfullname)
dropitdowns[0].click()
time.sleep(0.3)
sksbtns = driver.find_elements(By.XPATH, f"//span[text()='{sks}']")
for i in sksbtns:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)
dropitdowns[1].click()
time.sleep(0.3)
weekbtns = driver.find_elements(By.XPATH, f"//span[contains(text(), 'Minggu Ke') and contains(text(), '{nweek}') and contains(text(), '-')]")
for i in weekbtns:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)
dropitdowns[2].click()
time.sleep(0.3)
sessionbtns = driver.find_elements(By.XPATH, f"//span[contains(text(), 'Pertemuan Ke') and contains(text(), '{nsession}')]") if int(nsession) <= 10 else driver.find_elements(By.XPATH, f"//span[contains(text(), 'Pertemuan ke') and contains(text(), '{nsession}')]")
for i in sessionbtns:
    try:
        i.click()
    except Exception as e:
        ##print(e)
        None
time.sleep(0.1)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Kirim']"))).click()
time.sleep(0.5)
driver.quit()