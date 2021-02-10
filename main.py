from bs4 import BeautifulSoup
import pandas as pd
import requests

major_list = []
early_career_pay_list = []
mid_career_pay_list = []

for i in range(1,35):
    salary_report_endpoint = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}"

    response = requests.get(url=salary_report_endpoint)
    data = response.text

    soup = BeautifulSoup(data, "html.parser")

    page_data = soup.find_all(class_="data-table__value")
    info = [row.getText() for row in page_data]
    major = [major for major in info if info.index(major)%6==1]
    major_list.append(major)
    early_career_pay = [pay.replace(",", "").strip("$") for pay in info if info.index(pay)%6==3]
    early_career_pay_list.append(early_career_pay)
    mid_career_pay = [pay.replace(",", "").strip("$") for pay in info if info.index(pay)%6==4]
    mid_career_pay_list.append(mid_career_pay)

for i in range(len(major_list)):
    career_pay_info = pd.DataFrame({"Major": major_list[i], "Early Career Pay": early_career_pay_list[i], "Mid-Career Pay": mid_career_pay_list[i]})
    if i == 0:
        career_pay_info.to_csv("college_salary_report.csv", index=False, mode='a')
    else:
        career_pay_info.to_csv("college_salary_report.csv", index=False, mode='a', header=False)





