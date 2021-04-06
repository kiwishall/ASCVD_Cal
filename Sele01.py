from urllib.parse import ParseResult
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

# 使用网站1进行计算结果 http://www.cvriskcalculator.com
def cvrisk(age, gender, race, total_chol, hdl, sbp, dbp, Treated_high_blood, Diabetes, Smoker):
    # 设置浏览器选项
    options = Options()
    options.use_chromium = True
    prefs = {
        'profile.default_content_setting_values':
        {
            'notifications':2
        }
    }
    # options.add_experimental_option('prefs', prefs)     #关掉浏览器左上角的通知提示
    # options.add_argument('disable-infobars')            #关闭'chrome正受到自动测试软件的控制'提示
    # 实例化网站并打开
    driver = webdriver.Edge()
    driver.get('http://www.cvriskcalculator.com')


    # 传入年龄
    driver.find_element_by_id('age').send_keys(age)

    # 传入性别
    if gender == 'F':
        driver.find_element_by_id('gender-1').click()
    else:
        driver.find_element_by_id('gender-0').click()

    # 传入国籍
    if race == 'American':
        driver.find_element_by_id('race-0').click()
    else:
        driver.find_element_by_id('race-1').click()

    # 传入总胆固醇
    driver.find_element_by_id('total-chol').send_keys(total_chol )

    # 传入高密度脂蛋白胆固醇
    driver.find_element_by_id('hdl').send_keys(hdl)

    # 传入收缩压
    driver.find_element_by_id('sbp').send_keys(sbp)

    # 传入舒张压
    driver.find_element_by_id('dbp').send_keys(dbp)

    # 传入高血压治疗情况
    if Treated_high_blood:
        driver.find_element_by_id('treated-1').click()
    else:
        driver.find_element_by_id('treated-0').click()

    # 传入糖尿病
    if Diabetes:
        driver.find_element_by_id('diabetes-1').click()
    else:
        driver.find_element_by_id('diabetes-0').click()

    # 传入吸烟情况
    if Smoker:
        driver.find_element_by_id('smoker-1').click()
    else:
        driver.find_element_by_id('smoker-0').click()

    driver.find_element_by_xpath('//*[@id="calc-form"]/fieldset/div[11]/button').click()
    # driver.find_element_by_class_name('btn btn-block btn-lg btn-primar').click()

    result = float(driver.find_element_by_xpath('/html/body/div/div[2]/div/h1').text.split('%')[0])
    driver.close()
    return result

# def cvrisk(age, gender, race, total_chol, hdl, sbp, dbp, Treated_high_blood, Diabetes, Smoker):
#     # 设置浏览器选项
#     options = Options()
#     options.use_chromium = True
#     prefs = {
#         'profile.default_content_setting_values':
#         {
#             'notifications':2
#         }
#     }
#     # options.add_experimental_option('prefs', prefs)     #关掉浏览器左上角的通知提示
#     # options.add_argument('disable-infobars')            #关闭'chrome正受到自动测试软件的控制'提示
#     # 实例化网站并打开
#     driver = webdriver.Edge()
#     driver.get('http://www.cvriskcalculator.com')


#     # 传入年龄
#     driver.find_element_by_id('age').send_keys(age)

#     # 传入性别
#     if gender == 'F':
#         driver.find_element_by_id('gender-1').click()
#     else:
#         driver.find_element_by_id('gender-0').click()

#     # 传入国籍
#     if race == 'American':
#         driver.find_element_by_id('race-0').click()
#     else:
#         driver.find_element_by_id('race-1').click()

#     # 传入总胆固醇
#     driver.find_element_by_id('total-chol').send_keys(total_chol )

#     # 传入高密度脂蛋白胆固醇
#     driver.find_element_by_id('hdl').send_keys(hdl)

#     # 传入收缩压
#     driver.find_element_by_id('sbp').send_keys(sbp)

#     # 传入舒张压
#     driver.find_element_by_id('dbp').send_keys(dbp)

#     # 传入高血压治疗情况
#     if Treated_high_blood:
#         driver.find_element_by_id('treated-1').click()
#     else:
#         driver.find_element_by_id('treated-0').click()

#     # 传入糖尿病
#     if Diabetes:
#         driver.find_element_by_id('diabetes-1').click()
#     else:
#         driver.find_element_by_id('diabetes-0').click()

#     # 传入吸烟情况
#     if Smoker:
#         driver.find_element_by_id('smoker-1').click()
#     else:
#         driver.find_element_by_id('smoker-0').click()

#     driver.find_element_by_xpath('//*[@id="calc-form"]/fieldset/div[11]/button').click()
#     # driver.find_element_by_class_name('btn btn-block btn-lg btn-primar').click()

#     result = float(driver.find_element_by_xpath('/html/body/div/div[2]/div/h1').text.split('%')[0])
#     driver.close()
#     return result
# 病人基本信息
age = 55            #年龄
gender = 'F'
race = 'American'
total_chol = 150    #Total cholesterol (mg/dL)
hdl = 50            #HDL cholesterol (mg/dL)
sbp = 120           #Systolic blood pressure (mmHg)
dbp = 120           #Diastolic blood pressure (mmHg)
Treated_high_blood = True       #高血压是否治疗
Diabetes = True                  #是否糖尿病
Smoker = True                   #是否吸烟

result = cvrisk(age, gender, race, total_chol, hdl, sbp, dbp, Treated_high_blood, Diabetes, Smoker)




print(result)
print(type(result))
# time.sleep(3)
# driver.get_screenshot_as_file(r'.\crossion.png')
