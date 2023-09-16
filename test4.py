from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard
import pyautogui


# Replace the chrome driver path with your own
browser = webdriver.Chrome()
browser.get('https://profitcentr.com/login')
browser.maximize_window()

time.sleep(1)

change_language = browser.find_element(By.XPATH, '//*[@id="top-menu"]/img').click()

time.sleep(1)

change_language2 = browser.find_element(By.XPATH, '//*[@id="top-menu"]/div/span[2]').click()

time.sleep(2)

browser.find_element(By.NAME, 'username').send_keys('baoanle10@gmail.com')

browser.find_element(By.NAME, 'password').send_keys('s3krkald')

# Wait for the user to log in and for the web page to change to https://profitcentr.com/members
WebDriverWait(browser, 100).until(EC.url_to_be('https://profitcentr.com/members'))

# Wait for 1 second
time.sleep(1)

# Click on the "Earn" element
earn_element = browser.find_element(By.ID, 'mnu_title1')
earn_element.click()

time.sleep(1)

# Click on the "YouTube" element within the "Earn" element using the find_element method with By.LINK_TEXT
youtube_element = browser.find_element(By.XPATH, "//*[@id='mnu_tblock1']/a[6]")
youtube_element.click()

# Continue with other actions after clicking on the "YouTube" element

time.sleep(10)

while True:
    try:
        try:
            watch_video_link1 = browser.find_element(By.XPATH, "//*[starts-with(@id, 'start-ads-')]/font/span[2]")
            watch_video_link1.click()
        except Exception:
            watch_video_link2 = browser.find_element(By.XPATH, "//*[starts-with(@id, 'start-ads-')]/span[1]/font/font")
            watch_video_link2.click()
        except Exception:
            watch_video_link3 = browser.find_element(By.XPATH, "//*[starts-with(@id, 'start-ads-')]/span[1]").click()
        

        # Wait for 1 second
        time.sleep(2)

        # Find the "Приступить к просмотру" button
        start_watching_button = browser.find_element(By.XPATH, "//*[starts-with(@id, 'check-task-')]")

        # Click on the "Приступить к просмотру" button
        start_watching_button.click()

        # Wait for the new page to open
        WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new window
        browser.switch_to.window(browser.window_handles[1])

        # Lấy ra tất cả các cửa sổ trình duyệt đang mở
        #windows = browser.window_handles

        # Chuyển đến cửa sổ tiếp theo
        #for i in range(len(windows)):
        #    browser.switch_to.window(windows[i])  # Chuyển đến cửa sổ thứ i

        # Đợi 1 giây
        time.sleep(5)

        # Create an ActionChains object
        #actions = ActionChains(browser)

        # Move the mouse cursor to the center of the screen and perform a click
        #actions.move_by_offset(browser.execute_script('return [window.innerWidth, window.innerHeight];')[0]/2, browser.execute_script('return [window.innerWidth, window.innerHeight];')[1]/2).click().perform()

        #screen_width, screen_height = pyautogui.size()

        # Tính toán vị trí cần click
        #x = int(screen_width / 2)  # Vị trí theo trục x, ở đây là giữa màn hình
        #y = int(screen_height / 2)  # Vị trí theo trục y, ở đây là giữa màn hình

        # Click vào vị trí đã tính toán
        #pyautogui.click(x, y)

        browser.switch_to.frame('video-start')
        time.sleep(1)
        browser.find_element(By.XPATH, ('//*[@id="movie_player"]/div[4]/button')).click()
        browser.switch_to.default_content()


        # Đợi cho đến khi con số phía trên bên trái chạy hết
        #WebDriverWait(browser, 37).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='tmr']")))

        #browser.implicitly_wait(20) 
        #browser.switch_to.frame(0) 
        #element = browser.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
        #element.click()

        #browser.execute_script('document.querySelector("div.ytp-cued-thumbnail-overlay-image").click()')

        #time.sleep(25)

        # Tìm dòng chữ "Подтвердить просмотр"
        #confirm_button = browser.find_element(By.XPATH, '//*[@id="succes-error"]/table/tbody/tr/td[2]/button')

        start_time = time.time()

        number_element = browser.find_element(By.XPATH, '//*[@id="tmr"]')

        # Khởi tạo giá trị của con số
        number = number_element.text

        # Lặp kiểm tra giá trị của con số
        while True:
            # Kiểm tra giá trị hiện tại của con số
            current_number = number_element.text
            
            if current_number != number:
                # Nếu giá trị hiện tại khác giá trị trước đó, cập nhật giá trị của con số
                number = current_number
                
                if number == "0":
                    time.sleep(1)
                    # Nếu con số chuyển thành 0, thực hiện hành động click vào nút confirm_button
                    confirm_button = browser.find_element(By.XPATH, '//*[@id="succes-error"]/table/tbody/tr/td[2]/button')
                    confirm_button.click()
                    break
            
            # Kiểm tra thời gian chờ
            elapsed_time = time.time() - start_time
            if elapsed_time > 150:
                # Nếu thời gian chờ vượt quá 100 giây, kết thúc vòng lặp
                break


        #wait = WebDriverWait(browser, 50)
        #button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="succes-error"]/table/tbody/tr/td[2]/button')))

        # Nhấn vào dòng chữ "Подтвердить просмотр"
        #confirm_button.click()

        # Đợi 1 giây
        time.sleep(2)


        # Close the current tab
        browser.close()

        # Switch back to the first tab
        browser.switch_to.window(browser.window_handles[0])

        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
            break

    except Exception as e:
      print(f'An error occurred: {e}')
      browser.switch_to.window(browser.window_handles[0])
      continue
