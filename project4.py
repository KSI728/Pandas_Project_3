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

# 파일 읽어오기 
gs_df=pd.read_excel('company_ESG.xlsx',sheet_name='GS')
print(gs_df.columns)

# 데이터 시각화
fig,axs=plt.subplots(2,3,figsize=(12,10))
xdata=gs_df['Unnamed: 0']

# 친환경 제품 서비스 구매액
ydata=gs_df['제품 서비스 구매액(친환경/억원)']
axs[0,0].plot(xdata, ydata, 'o-', color='#ADFF2F')
axs[0,0].set_title('친환경 제품 서비스 구매액', {'size': 'xx-large'})
axs[0,0].set_xlabel('연도')
axs[0,0].set_ylabel('단위 : 억 원')
axs[0,0].set_xticks(list(gs_df['Unnamed: 0']))
    
# 친환경 제품 서비스 매출액
ydata=gs_df['친환경 제품 서비스 매출액(억원)']
axs[0,1].plot(xdata, ydata, 'o-', color='#30D5C8')
axs[0,1].set_title('친환경 제품 서비스 매출액', {'size': 'xx-large'})
axs[0,1].set_xlabel('연도')
axs[0,1].set_ylabel('단위 : 억 원')
axs[0,1].set_xticks(list(gs_df['Unnamed: 0']))

# 친환경 매장 수
ydata=gs_df['SEMS 설치 점포(친환경 매장)']
axs[0,2].plot(xdata, ydata, 'o-', color='#808000')
axs[0,2].set_title('친환경 매장 수', {'size': 'xx-large'})
axs[0,2].set_xlabel('연도')
axs[0,2].set_ylabel('매장 수')
axs[0,2].set_xticks(list(gs_df['Unnamed: 0']))
    
# 온실가스 집약도(Scope 1,2)
ydata=gs_df['Scope 1,2 온실가스 집약도(tCO2-eq/억 원)']
axs[1,0].plot(xdata, ydata, 'o-', color='#808000')
axs[1,0].set_title('온실가스 집약도', {'size': 'xx-large'})
axs[1,0].set_xlabel('연도')
axs[1,0].set_ylabel('단위 : tCO2-eq/ 억 원')
axs[1,0].set_xticks(list(gs_df['Unnamed: 0']))

# 에너지 감축률
ydata=gs_df['에너지 감축률(TJ/억원)']
axs[1,1].plot(xdata, ydata, 'o-', color='#ADFF2F')
axs[1,1].set_title('에너지 감축률', {'size': 'xx-large'})
axs[1,1].set_xlabel('연도')
axs[1,1].set_ylabel('단위 : TJ/억원')
axs[1,1].set_xticks(list(gs_df['Unnamed: 0']))

# 재생에너지 발전 및 사용량
ydata=gs_df['재생에너지 발전 및 사용량(kWh)']
axs[1,2].plot(xdata, ydata, 'o-', color='#30D5C8')
axs[1,2].set_title('재생에너지 발전 및 사용량', {'size': 'xx-large'})
axs[1,2].set_xlabel('연도')
axs[1,2].set_ylabel('단위 : kWh')
axs[1,2].set_xticks(list(gs_df['Unnamed: 0']))

fig.suptitle('GS리테일 ESG Data', fontsize=24)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------------------------
# 파일 읽어오기 / 멀티 인덱스 지정
sk_df=pd.read_excel('company_ESG.xlsx',sheet_name='SK',index_col=[0,1])

# 데이터 확인 및 수정 
print(sk_df)

# 데이터 시각화 
fig,axs=plt.subplots(2,2,figsize=(12,8))
xdata1=sk_df.columns[1:]

# 재생에너지 소비
ydata1=sk_df.loc[('Renewable energy consumption','Green Premium purchase volume'),2020:2023]
axs[0,0].bar(xdata1, ydata1, color='#ADFF2F')
axs[0,0].set_title('그린 프리미엄', {'size': 'xx-large'})
axs[0,0].set_xlabel('연도')
axs[0,0].set_ylabel('단위 : MWh')
axs[0,0].set_xticks(list(xdata1))

# 태양광 에너지 소비
ydata1=sk_df.loc[('Renewable energy consumption','solar energy'),2020:2023]
axs[0,1].plot(xdata1, ydata1, 'o-', color='#30D5C8')
axs[0,1].set_title('태양광 에너지 소비', {'size': 'xx-large'})
axs[0,1].set_xlabel('연도')
axs[0,1].set_ylabel('단위 : MWh')
axs[0,1].set_xticks(list(xdata1))

# 환경 친화적 제품 및 서비스
xdata2=sk_df.columns[2:]
ydata1=sk_df.loc[('eco-friendly products and services','Low-carbon/Carbon-offset products'),2021:2023]
ydata2=sk_df.loc[('eco-friendly products and services','Eco-friendly certified hardware products'),2021:2023]
axs[1,0].plot(xdata2, ydata1, 'o-', color='#ADFF2F',label='저탄소/탄소회피제품')
axs[1,0].plot(xdata2, ydata2, 'o-', color='#30D5C8',label='친환경인증 HW제품')
axs[1,0].set_title('환경 친화적 제품 및 서비스 매출', {'size': 'xx-large'})
axs[1,0].set_xlabel('연도')
axs[1,0].set_ylabel('단위 : 억 원')
axs[1,0].set_xticks(list(xdata2))
axs[1,0].legend()

# 태양광 에너지 소비
ydata1=sk_df.loc[('Direct greenhouse gas emissions (Scope 1)','Intensity per revenue'),2020:2023]
axs[1,1].plot(xdata1, ydata1, 'o-', color='#30D5C8')
axs[1,1].set_title('온실가스 집약도(Scope1)', {'size': 'xx-large'})
axs[1,1].set_xlabel('연도', fontdict={'size': 'large'})
axs[1,1].set_ylabel('단위 : tCO₂eq/십억 원')
axs[1,1].set_xticks(list(xdata1))

fig.suptitle('SK ESG Data', fontsize=24)
plt.tight_layout()
plt.show()