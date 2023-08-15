import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu

#with open('app-style.css') as f:
st.sidebar.markdown('''
 #  Customer Segmentation
- # [Demographic Analysis](#demographic-analysis)
- # [Psychographic Analysis](#psychographic-analysis)
- # [Behavioural Analysis](#behavioural-analysis)
- # [Geographical Analysis](#geographical-analysis)
''', unsafe_allow_html=True)

url='DataScience-updated.csv'
df=pd.read_csv(url)
st.title("""Customer Segmentation""")
st.dataframe(df)

st.header('Demographic Analysis')

gender_select=st.sidebar.selectbox("Select Gender",("Male","Female","Others"))
gender_data=df[(df['Gender']==gender_select)]
st.dataframe(gender_data)

fig, ax= plt.subplots()
ax.hist(gender_data.Age,rwidth=0.9)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Gender specific Age count')
st.pyplot(fig)

#Income_select=st.selectbox("Select Income",("20000","50000","75000","100000"))
#Income_data=df[(df['Income']==Income_select)]
#st.write(gender_data)

#fig=plt.plot(Income_data.Age)
#st.line_chart(Income_data.Age)

fig1= plt.figure()
sns.countplot(df["Income"])
st.pyplot(fig1)

#gender_select1=st.selectbox("Select Gender",("Male","Female","Others"))
#gender_data1=df[(df['Gender']==gender_select)]
fig2=plt.figure()
sns.countplot(gender_data["Income"])
plt.title('Gender specific Income count')
st.pyplot(fig2)

fig3=plt.figure()
sns.barplot(x="Gender", y="Income", data=df, palette="summer")
plt.title('Average Income of specific Gender')
st.pyplot(fig3)

#fig4=plt.figure()
#sns.barplot(x="Income", y="Age", data=df)
#st.pyplot(fig4)

#fig5=plt.figure()
#sns.barplot(x="Gender", y="Age", data=df)
#st.pyplot(fig5)

st.header("Psychographic Analysis")

data=df[["Shopping site","Age"]]
st.dataframe(data)

no=st.sidebar.slider('Select the number of data to be viewed',0,175,50)
fig6=plt.figure()
bx=sns.barplot(x="Shopping site", y="Age", data=data.head(no))
bx.set_xticklabels(bx.get_xticklabels(), rotation=90)
st.pyplot(fig6)
#st.bar_chart(df[["Shopping site","Age"]])

preference_gender_cross_tab=pd.crosstab(df["Shopping preference"],df["Gender"])
#st.dataframe(cross_tab.head())
fig7=px.line(preference_gender_cross_tab, title='Shopping preference according to Gender')
#st.write("""Shopping preference according to Gender""")
st.write(fig7)

payment_age_cross_tab=pd.crosstab(df["Payment Method"],df["Age"])
#payment_age_cross_tab=payment_age_cross_tab.reset_index()
#payment_age_cross_tab.columns=["Payment Method","Age"]
#print(payment_age_cross_tab)
fig8=px.line(payment_age_cross_tab)
st.write("""Payment Method according to Age""",fig8)
#st.write(fig8)

st.header("Behavioural Analysis")

#no2=st.sidebar.slider('Select the number of data to be viewed',0,176,50)
category_tab=df["Category"]
category_tab=category_tab.reset_index()
category_tab.columns=["Count","Category"]
st.dataframe(category_tab)
fig9=px.pie(category_tab.head(no), values="Count", names="Category")
st.write("""Number of People from specific Category""",fig9)

income_budget_cross_tab=pd.crosstab(df["Income"],df["Budget"])
#st.dataframe(income_budget_cross_tab)
fig10=px.line(income_budget_cross_tab)
st.write("""Income v/s Budget""",fig10)

income_budget_cross_tab=pd.crosstab(gender_data["Income"],gender_data["Budget"])
#st.dataframe(income_budget_cross_tab)
fig11=px.line(income_budget_cross_tab)
st.write("""Gender specific Income v/s Budget""",fig11)

st.header("Geographical Analysis")

#location=df["Location"]
#st.dataframe(location)
#st.map(location)

location_tab=df["Location"]
location_tab=location_tab.reset_index()
location_tab.columns=["Value","Location"]
location_cross_tab=pd.crosstab(df["Location"],df["Income"])
st.dataframe(location_tab)
#st.dataframe(location_cross_tab)


fig12=px.line(location_cross_tab)
st.write("""Number of People from specific Location with their respective Income""",fig12)