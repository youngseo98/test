import streamlit as st

st.title('우승 예측')
st.header('스포츠를 더 재밌게 즐겨보자')
st.subheader('통계만 내는 사이트 입니다.')

m_nickname = st.text_input('입금 받으실 계좌 입력')
nickname = st.text_input('입금 받는 분')
money = st.number_input('입금액', min_value=5000)

s_options = ['축구', '야구', '농구', '배구']
s_selected_many = st.selectbox('관심있는 스포츠', s_options)



f_options = ['EPL','분데스리가','LaLiga','세리에 A']
choice = st.radio('제일 관심있는 축구리그',f_options)

e_options = ['맨유','리버풀','맨시티','토트넘','아스날','첼시','노팅엄','뉴캐슬', '기타']
b_options = ['뮌헨','도르트문트','라이프치히','레버쿠젠','기타']
l_options = ['바르셀로나','레알마드리드','아틀레티코 마드리드','기타']
ss_options = ['ac밀란','인터밀란','유벤투스','나폴리','라치오','기타']

if choice == 'EPL':
    st.selectbox('누가 우승할거 같습니까',e_options)
elif choice == '분데스리가':
    st.selectbox('누가 우승할거 같습니까',b_options)
elif choice == 'LaLiga':
    st.selectbox('누가 우승할거 같습니까',l_options)
elif choice == '세리에 A':
    st.selectbox('누가 우승할거 같습니까',ss_options)

import random

vic = [1.2, 12, 15, 1, 3, 5, 9, 8, 7, 0.6, 0.3, 11]

vv = random.choice(vic)


if st.button('입력 완료'):
    st.write(f'배당은? {vv}배 입니다.')
    st.write(f'예측 성공식 받으실 금액은: {money*vv}원 입니다.')

import pandas as pd 

data = pd.DataFrame({
    "팀" : ['맨유','리버풀','맨시티','토트넘','아스날','첼시','노팅엄','뉴캐슬', '기타'],
    "승률 (%)": [15, 78, 45, 16, 28, 60, 21, 30, 10],
    "인기도 (%)":[10, 20, 10, 5, 10, 5, 2, 3, 5],
    "우승횟수": [11, 1, 8, 0, 1, 5, 2, 3, 7]
})

st.dataframe(data, use_container_width=True)

st.bar_chart(data.set_index('팀')['승률 (%)'])
st.line_chart(data.set_index('팀')['우승횟수'])

fig1 = data.plot.pie(
    y = '인기도 (%)',
    labels = data["팀"],
    autopct = "%1.1f%%",
    figsize = (6,6),
    legend = False,
    title = '인기도'
).get_figure()

st.pyplot(fig1)


