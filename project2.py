# 모듈 로딩   
import pandas as pd                         # 데이터 분석 및 전처리 모듈
import matplotlib.pyplot as plt             # 데이터 시각화 모듈
import matplotlib.font_manager as fm        # 폰트 설정
import numpy as np                          # 배열 관련 모듈
import seaborn as sns                       # 데이터 시각화 모듈
import koreanize_matplotlib                 # 데이터 시각화 한국어 모듈
from tabulate import tabulate               # 터미널 창 시각화 개선 모듈

#----------------------------------------------------------------------------------------------------------------
# [1] 정부 차원의 노력

# 파일 불러오기
charge_df=pd.read_csv('charge.csv',encoding='iso-8859-1')

# 컬럼명 수정
charge_df.columns=['year','급속','완속']


# 맨 앞열을 인덱스로
charge_df.set_index(charge_df['year'],inplace=True)

# 결측치가 있어 임의로 0
charge_df['완속']=charge_df['완속'].fillna(0)
charge_df=charge_df.astype(int)

# 데이터 시각화
plt.figure(figsize=(12, 8))

xdata=charge_df['year']
ydata1=charge_df['급속'].astype(int)
ydata2=charge_df['완속'].astype(int)
ydata3=charge_df['완속'].iloc[0:-1]

w=0.4
plt.bar(xdata,ydata1,width=w,color='#000080',edgecolor='black',label='급속 충전소')
plt.bar(xdata+0.4,ydata2,width=w,color='#ADD8E6',edgecolor='black',label='완속 충전소')
plt.plot(xdata,ydata1,color='#000080')

# 제목, 라벨 설정
plt.title(f'연도별 전기차 충전소 설치 수',{'size':'xx-large'})
plt.xlabel('연도',fontdict={'size':'large'})
plt.ylabel('설치 수',fontdict={'size':'large'})

# 격자 설정
plt.grid(True, linestyle='--', linewidth=0.5, color='grey',axis='y')

plt.legend()
plt.xticks(rotation=45)
plt.show()

