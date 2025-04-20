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


def gov():
    # 파일 불러오기
    law_df=pd.read_excel('law.xlsx')

    # 데이터 확인
    print(law_df.info())

    # 데이터 시각화 - 바 그래프
    plt.figure(figsize=(12, 8))
    xdata=list(law_df['sort'].values)
    ydata=law_df['count']
    plt.bar(xdata,ydata,color='lightcoral',edgecolor='black')

    # 제목, 라벨 설정
    plt.title(f'키워드별 기후에너지 관련 법안 발의(건)',{'size':'xx-large'})
    plt.xlabel('키워드별 분류',fontdict={'size':'large'})
    plt.ylabel('발의 건수',fontdict={'size':'large'})
    plt.xticks(rotation=45)

    for i, count in enumerate(ydata):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom', fontdict={'size': 'large'})

    plt.tight_layout()
    plt.show()



#----------------------------------------------------------------------------------------------------------------



def div_show():
    # 파일 불러오기
    car_df=pd.read_excel('seoul_car.xlsx',header=0)
    car_df=car_df.T

    # 컬럼 수정
    column_list=['종류','소계','승용차','승합차','화물차','특수차']
    car_df.drop('Unnamed: 0',inplace=True)
    car_df.columns=column_list

    # 데이터 수정
    car_df.drop(car_df.columns[0],axis=1,inplace=True)
    
    # 결측치 확인 
    print(car_df.info())
  
    # 데이터 시각화 1
    year_list=list(range(2008,2025))
    i_list=['휘발유','경유','LPG','전기','CNG','하이브리드','수소']
    ydata_list=[]
    ydata_list2=[]
    ydata_list3=[]

    # 연도별 친환경 자동차 등록수 그래프
    for i in year_list:
        xdata=year_list
        ydata_list.append(car_df.loc[f'{i}.6','소계'])
        ydata_list2.append(car_df.loc[f'{i}.4','소계'])
        ydata_list3.append(car_df.loc[f'{i}.7','소계'])

    plt.figure(figsize=(12, 8))
    xdata=year_list
    plt.plot(xdata,ydata_list,'o-',color="#ADFF2F",label="하이브리드")
    plt.plot(xdata,ydata_list2,'o-',color="#30D5C8",label='전기')
    plt.plot(xdata,ydata_list3,'o-',color="#808000",label='수소')
    plt.legend()

    # 제목, 라벨 설정
    plt.title(f'친환경 자동차 누적 등록건수',{'size':'xx-large'})
    plt.xlabel('연도',fontdict={'size':'large'})
    plt.ylabel('누적 등록 건수',fontdict={'size':'large'})
    plt.xticks(year_list,rotation=45)

    # 격자 설정
    plt.grid(which='both',linestyle='--',linewidth=0.5,color='grey')

    plt.show()
    
    # 데이터 시각화 2 
    year_list=list(range(2008,2025))
    ydata_list=[]
    ydata_list2=[]
    ydata_list3=[]
    ydata_list4=[]
    
    for i in year_list:
        xdata=year_list
        ydata_list.append(car_df.loc[f'{i}.6','소계'])
        ydata_list2.append(car_df.loc[f'{i}.4','소계'])
        ydata_list3.append(car_df.loc[f'{i}.7','소계'])
        ydata_list4.append(car_df.loc[f'{i}.5','소계'])
    
   # 서브플롯 생성
    fig,axs=plt.subplots(2,2,figsize=(20,14))
    
    # 하이브리드 자동차 그래프
    axs[0,0].plot(year_list, ydata_list, 'o-', color='#ADFF2F')
    axs[0,0].set_title('하이브리드 자동차 누적 등록건수', {'size': 'xx-large'})
    axs[0,0].set_xlabel('연도', fontdict={'size': 'large'})
    axs[0,0].set_ylabel('누적 등록 건수', fontdict={'size': 'large'})
    axs[0,0].grid(which='both', linestyle='--', linewidth=0.5, color='grey')
    
    # 전기 자동차 그래프
    axs[0,1].plot(year_list, ydata_list2, 'o-', color='#30D5C8')
    axs[0,1].set_title('전기 자동차 누적 등록건수', {'size': 'xx-large'})
    axs[0,1].set_xlabel('연도', fontdict={'size': 'large'})
    axs[0,1].set_ylabel('누적 등록 건수', fontdict={'size': 'large'})
    axs[0,1].grid(which='both', linestyle='--', linewidth=0.5, color='grey')

    # 수소 자동차 그래프
    axs[1,0].plot(year_list, ydata_list3, 'o-', color='#808000')
    axs[1,0].set_title('수소 자동차 누적 등록건수', {'size': 'xx-large'})
    axs[1,0].set_xlabel('연도', fontdict={'size': 'large'})
    axs[1,0].set_ylabel('누적 등록 건수', fontdict={'size': 'large'})
    axs[1,0].grid(which='both', linestyle='--', linewidth=0.5, color='grey')
    
    # CNG(천연가스) 자동차 그래프
    axs[1,1].plot(year_list, ydata_list4, 'o-', color='#98FF98')
    axs[1,1].set_title('CNG(천연가스) 자동차 누적 등록건수', {'size': 'xx-large'})
    axs[1,1].set_xlabel('연도', fontdict={'size': 'large'})
    axs[1,1].set_ylabel('누적 등록 건수', fontdict={'size': 'large'})
    axs[1,1].grid(which='both', linestyle='--', linewidth=0.5, color='grey')
    

    plt.tight_layout
    plt.show()
    
    # 데이터 시각화 3 
    year_list=list(range(2008,2025))
    ydata_list=[]
    ydata_list2=[]
    ydata_list3=[]
    ydata_list4=[]
    ydata_list5=[]
    ydata_list6=[]
    ydata_list7=[]
    

    # 연도별 누적 모든 연료의 자동차 등록수 그래프
    for i in year_list:
        xdata=year_list
        ydata_list.append(car_df.loc[f'{i}.6','소계'])
        ydata_list2.append(car_df.loc[f'{i}.4','소계'])
        ydata_list3.append(car_df.loc[f'{i}.7','소계'])
        ydata_list4.append(car_df.loc[f'{i}.1','소계'])
        ydata_list5.append(car_df.loc[f'{i}.2','소계'])
        ydata_list6.append(car_df.loc[f'{i}.3','소계'])
        ydata_list7.append(car_df.loc[f'{i}.5','소계'])

    plt.figure(figsize=(12, 8))
    xdata=year_list
    plt.plot(xdata,ydata_list,'o-',color="#ADFF2F",label="하이브리드")
    plt.plot(xdata,ydata_list2,'o-',color="#30D5C8",label='전기')
    plt.plot(xdata,ydata_list3,'o-',color="#808000",label='수소')
    plt.plot(xdata,ydata_list4,'o-',color="#FFA500",label='휘발유')
    plt.plot(xdata,ydata_list5,'o-',color="#FFC0CB",label='경유')
    plt.plot(xdata,ydata_list6,'o-',color="#800020",label='LPG')
    plt.plot(xdata,ydata_list7,'o-',color="#98FF98",label='CNG')
    plt.legend()

    # 제목, 라벨 설정
    plt.title(f'연료별 자동차 누적 등록건수',{'size':'xx-large'})
    plt.xlabel('연도',fontdict={'size':'large'})
    plt.ylabel('누적 등록 건수',fontdict={'size':'large'})
    plt.xticks(year_list,rotation=45)

    # 격자 설정
    plt.grid(which='both',linestyle='--',linewidth=0.5,color='grey')

    plt.show()
    
div_show()