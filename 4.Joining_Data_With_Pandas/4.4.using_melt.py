import pandas as pd
import matplotlib.pyplot as plt
# Wide vs Tall format
# Wide - each subject's repeated responses will be separated in columns
# income per year
# name      2018    2019    2020    2021    2022    2023    2024
# Claire    5000    5500    6000    6500    7000    7500    8000

# Tall - each row is a one time point per subject
# income
# name      income  year
# Claire    5000    2018
# Claire    5500    2019
# Claire    6000    2020
# Claire    6500    2021
# Claire    7000    2022
# Claire    7500    2023
# Claire    8000    2024

# https://psa.gov.ph/statistics/labor-force-survey

philippineUnemploymentRateFile = pd.read_csv('philippine_unemployment_rate.csv')
php_unempl_rate = pd.DataFrame(philippineUnemploymentRateFile)
print(php_unempl_rate)

# var_name = columns, value_name = row data in context of wide format (not tall format)
php_unempl_rate_v1 = php_unempl_rate.melt(id_vars='year', var_name='month', value_name='unempl_rate')
pd.set_option('display.max_rows', None)
print(php_unempl_rate_v1)

php_unempl_rate_v1["date"] = pd.to_datetime(php_unempl_rate_v1["year"].astype(str) + "-" + php_unempl_rate_v1["month"], format='%Y-%b')
php_unempl_rate_v1_sorted = php_unempl_rate_v1.sort_values("date", ascending=True)
php_unempl_rate_v1_sorted.plot(y="unempl_rate", x="date")
plt.show()