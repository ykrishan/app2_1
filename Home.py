import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("The Best Company")
content_1 = """
The best company is defined not just by profitability but by its commitment to innovation, 
employee welfare, and societal impact. It fosters a culture of inclusivity, 
where diverse perspectives thrive and creativity flourishes. 
Transparency in operations builds trust with stakeholders, while ethical practices underscore its integrity. 
Such a company embraces sustainability, striving for environmental stewardship and community engagement. 
It invests in cutting-edge technology to stay ahead in its field and adapt to evolving markets. 
Above all, it values its people, empowering them to grow professionally and personally.
"""
st.write(content_1)

st.header("Our Team")

col1, col2, col3 = st.columns(3)
dt = pd.read_csv("data-2.csv")
with col1:
    for index, row in dt[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in dt[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in dt[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image(f"images/{row['image']}")
