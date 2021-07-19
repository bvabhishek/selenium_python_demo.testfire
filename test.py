from selenium import webdriver
from selenium.webdriver.support.select import Select 
import time

class Test():
    def new(self):
            
        driver=webdriver.Firefox()
        driver.get("http://demo.testfire.net/")
        time.sleep(2)
        driver.maximize_window()
        # click button id="LoginLink"

        login = driver.find_element_by_id("LoginLink")
        login.click()

        # username and password
        uid = driver.find_element_by_id("uid")
        uid.send_keys('jsmith')
        time.sleep(2)
        passwd = driver.find_element_by_id("passw")
        passwd.send_keys('demo1234')
        time.sleep(2)
        login_btn = driver.find_element_by_name("btnSubmit")
        login_btn.click()
        print("Login Successfull")
        time.sleep(2)

        #account related
        print("Getting account details.....")
        #recent trans
        r_tras=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/ul/li[2]/a").click()
        time.sleep(2)
        after_date=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/table[1]/tbody/tr/td[2]/input")
        after_date.send_keys("2020-11-24")
        time.sleep(2)
        trans_submit=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/table[1]/tbody/tr/td[5]/input").click()
        print("getting account details after 2020-11-24")
        driver.back()

        trans_funds = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/ul/li[3]/a").click()
        time.sleep(2)
        print("Time for Transactions")
        elem_to = driver.find_element_by_id("toAccount")
        to_acc = Select(elem_to)
        to_acc.select_by_index(1)
        amt = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/table/tbody/tr[3]/td[2]/input")
        amt.send_keys("1000")
        time.sleep(2)
        sendamnt = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/table/tbody/tr[4]/td/input").click()
        print("Amount sent ..")
        time.sleep(2)

        #search news articles 
        news_articles = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/ul/li[4]/a").click()
        time.sleep(2)
        print("Search for news articles")
        search_art = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/input[2]").clear()
        time.sleep(3)

        search_art = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/input[2]")
        search_art.send_keys('Unix')

        query_article = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/input[3]").click()
        time.sleep(2)
        print("Searching for news article completed")

        #language
        site_lang = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/ul/li[5]/a").click()
        print("Select site language")
        time.sleep(2)
        intl_lang = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/p[3]/a[1]").click()
        print("selecting international language")
        time.sleep(2)
        english_lang = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/p[3]/a[2]").click()
        print("selecting english as language")
        time.sleep(2)
        print("Back to home page")

        homepage = driver.find_element_by_id("AccountLink")
        homepage.click()


        #dropdownlist

        #selecting ddl
        element_drp=driver.find_element_by_id("listAccounts")
        drp=Select(element_drp)
        #select by index
        drp.select_by_index(0)
        go_btn = driver.find_element_by_id("btnGetAccount")
        go_btn.click()
        time.sleep(5)
        #inside
        element_drp=driver.find_element_by_id("listAccounts")
        drp=Select(element_drp)
        drp.select_by_index(1)
        btnGetAccount = driver.find_element_by_id("btnGetAccount")
        #btnGetAccount.click()
        print("checking bank statment")
        time.sleep(2)
        #inside
        drp.select_by_index(2)
        btnGetAccount = driver.find_element_by_id("btnGetAccount")
        btnGetAccount.click()


        #myaccount/homepage
        my_account = driver.find_element_by_id("AccountLink")
        my_account.click()

        #click here to apply with xpath
        apply = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/form/table/tbody/tr[2]/td/span/table/tbody/tr[3]/td/a") 
        apply.click()
        time.sleep(2)
        #password
        enterpass = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/span/form/table/tbody/tr[1]/td[2]/input")
        enterpass.send_keys("demo1234")
        time.sleep(2)
        submitt = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/span/form/table/tbody/tr[2]/td[2]/input")
        submitt.click()
        print("Apply for Gold Visa Application ")
        time.sleep(2)

        #home
        home = driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[1]/td[1]/a/img")
        home.click()
        ############################Small business#####################

        small_buis = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/a[2]").click()
        print("Entering small buisiness")
        time.sleep(2)

        #deposite

        small_buis = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/h2[1]/a").click()
        print("Deposite page")
        time.sleep(2)

        #highyeild

        highyeild = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/ul/li[4]/a").click()
        print("High yeild investment")
        time.sleep(2)

        highyeild_email = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[2]/span/div/p[3]/input[1]").send_keys("john@gmail.com")
        time.sleep(2)
        highyeild_submit = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[2]/span/div/p[3]/input[2]").click()
        print("Email for high yield submitted")
        time.sleep(2)
        driver.back()
        driver.back()
        #lending services
        lending = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[2]/li[2]/a").click()
        time.sleep(3)
        print("Lending services....")

        #cards
        cards = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[2]/li[3]/a").click()
        time.sleep(2)
        print("Card options")

        #insurance
        insurance = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[2]/li[4]/a").click()
        time.sleep(3)
        print("About insurance...")

        #retirement
        retire = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[2]/li[5]/a").click()
        time.sleep(3)
        print("Plan your retirement")

        #other services
        other_ser = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[2]/li[6]/a").click()
        time.sleep(3)
        print("Other services")







        #INSIDE ALTRO MUTUALform

        print("About us")
        time.sleep(2)

        #aboutus
        about_us=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[3]/li[1]/a").click()
        time.sleep(2)
        team = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/ul/li[1]/a").click()
        time.sleep(2)
        print("About the team")
        driver.back()


        #contact us
        contact=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[3]/li[2]/a")
        contact.click()
        onlineform=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/p[2]/a")
        onlineform.click()
        time.sleep(2)
        yoemail = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[3]/td[2]/input")
        yoemail.send_keys("john@gmail.com")
        time.sleep(1)
        subje = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[4]/td[2]/input")
        subje.send_keys("call back")
        time.sleep(1)
        comment=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[5]/td[2]/textarea")
        comment.send_keys("requesting you for a quick call back...!!!")
        time.sleep(1)
        submi=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[6]/td[2]/input[1]")
        submi.click()
        time.sleep(2)
        print("Form filled successfully")
        home = driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[1]/td[1]/a/img")
        home.click()
        print("back to home page")

        #location
        location = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[3]/li[3]/a").click()
        print("Location we are at")
        time.sleep(2)
        driver.back()

        #investor
        ir = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/ul[3]/li[4]/a").click()
        time.sleep(2)
        print("Investor relation..")
        #press release
        pr = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/p[3]/a").click()
        time.sleep(2)
        print("press release")
        driver.back()
        driver.back()






        #inside altro for view pdf
        insidealtoro = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/a[3]")
        insidealtoro.click()
        print("inside altoro for podf")
        pdf=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/p[3]/a[2]")
        pdf.click()
        time.sleep(2)
        driver.back()
        #communityprogram
        communityprog = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/p[3]/a[1]")
        communityprog.click()
        print("Entering community program")
        time.sleep(1)
        #downlaod_adobe
        adobe_down=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/p[4]/a")
        adobe_down.click()
        print("Downloading free adobe....")
        time.sleep(3)


        #in adobe page

        element_os = driver.find_element_by_id("select_os")
        os = Select(element_os)
        os.select_by_index(4)
        print("Os selected")
        time.sleep(2)
        language = driver.find_element_by_id("select_language")
        lang = Select(language)
        lang.select_by_visible_text("English (UK)")
        print("Language selected")
        time.sleep(2)
        version = driver.find_element_by_id("select_version")
        ver = Select(version)
        ver.select_by_index(1)
        time.sleep(2)
        print("Version selected")

        #chkbox
        uncheck = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[4]/div[1]/div[1]/div[3]/input").click()
        time.sleep(2)
        #download adobe
        dload = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[4]/div[1]/div[2]/div[2]/p[1]/a").click()
        print("Adobe downloading....")
        #time.sleep(10)
        driver.back()
        driver.back()

        #privacypolicy
        pp = driver.find_element_by_xpath("/html/body/div[3]/a[1]").click()
        print("Reading privacy policy")
        time.sleep(2)
        driver.back()
        #security statment
        ss = driver.find_element_by_xpath("/html/body/div[3]/a[2]").click()
        print("Reading security statment")
        time.sleep(2)
        driver.back()
        #serverstatuscheck
        serverstatus = driver.find_element_by_xpath("/html/body/div[3]/a[3]").click()
        print("server status checking")
        time.sleep(2)
        check_status = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td/form/input").click()
        print("checking status")
        time.sleep(2)
        driver.back()
        driver.back()


        #logout
        logout_btn = driver.find_element_by_link_text('Sign Off')
        logout_btn.click()

test_object = Test()
test_object.new()
