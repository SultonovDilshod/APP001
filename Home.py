import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv('files/kun.csv', sep=';')
st.header("The best company performance")
st.write("Bu dunyodagi eng daxshatli kollective jamoalardan biir hisoblanadi deb takidlab o'tsak mubolaga bulmaydi")
st.subheader("Bu Dilshod's team")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.write(row["role"])
        st.image("kun/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.write(row["role"])
        st.image("kun/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.write(row["role"])
        st.image("kun/" + row["image"])
