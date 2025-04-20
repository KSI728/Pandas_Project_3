# 모듈 로딩   
import pandas as pd                         # 데이터 분석 및 전처리 모듈
import matplotlib.pyplot as plt             # 데이터 시각화 모듈
import matplotlib.font_manager as fm        # 폰트 설정
import numpy as np                          # 배열 관련 모듈
import seaborn as sns                       # 데이터 시각화 모듈
import koreanize_matplotlib                 # 데이터 시각화 한국어 모듈
from tabulate import tabulate               # 터미널 창 시각화 개선 모듈

#----------------------------------------------------------------------------------------------------------------
# [2] 기업 차원의 노력

# 파일 불러오기
grade_df=pd.read_excel('grade.xlsx')

# 데이터 확인 
print(grade_df.info())

# 2024년도 환경 - ESG 등급별 기업 수 구하기
print(grade_df['환경'].value_counts().sort_index())

# 별도의 리스트에 데이터 담기
grade_list=['A+등급','A등급','B+등급','B등급','C등급','D등급','등급없음']
count_list=[40,208,159,65,286,243,65]
total=sum(grade_df['환경'].value_counts())

# 시각화 - pie chart
plt.figure(figsize=(10, 6))

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']
plt.pie(count_list, labels=grade_list, colors=colors,autopct='%1.1f%%',startangle=90,counterclock=False,labeldistance=0.8)
plt.title(f'2024년 기업 환경 ESG 등급({total}개 기업)')
plt.axis('equal')  
plt.show()