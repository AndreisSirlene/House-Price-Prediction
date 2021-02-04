import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
import shap
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


st.write('''
# House Prediction App 🏠
This app predict the sales price of houses in **King County**, Washington State – U.S.!
'''
)
st.write('---')

house = pd.read_csv('https://github.com/AndreisSirlene/House-Price-Prediction/raw/main/kc_house_data.csv')
house.drop('id', axis ='columns', inplace=True)
house['date'] = pd.to_datetime(house['date'], format='%Y-%m-%d')
house['month'] = house['date'].dt.month
house['year'] = house['date'].dt.year
# fill in nan values with 0 (0nly two columns with nan)
house['sqft_above'] = house['sqft_above'].fillna('0')
st.write(house.head())
st.write('---')


st.write('''
Price distribution !
''')

price_dist = pd.DataFrame(house['price'].value_counts()).head(20)
st.bar_chart(price_dist)

st.sidebar.header('Specify Input Parameters')

  ############################
X = house.drop(columns=['date','price', 'month', 'year'])
y = house[['price']]  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=9382)
model = RandomForestRegressor()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

st.header('Predictionof Price')
#st.write(prediction)
st.write('----')
##################
# Explain the model predictions using SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

st.header('Feature Importance')
plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, X)
st.pyplot(bbox_inches='tight')
st.write('---')

