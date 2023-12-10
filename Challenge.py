import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


st.title("Sunu Deukkuway NaÑ Ko aar")
# Chargeons les données
df= pd.read_csv("Data.csv")

# Traitements de données NAN
df["Sunshine"].fillna(0, inplace=True)
df["WindSpeed"].fillna(0, inplace=True)

# Séléction du variabe cible 
X = df.drop("RainTomorrow",axis=1).values
y = df["RainTomorrow"].values

# Standardisons les données, elles sont à des échelles très différentes
minmax = MinMaxScaler()
X = minmax.fit_transform(X)

# Séparation des données test en train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Passons à SVM algorithmes
model = SVC().fit(X_train, y_train)
previsor_svc = model.predict(X_test)

st.sidebar.info("Seytu asamaan si ⛅🌨️")
st.sidebar.header("🌐Taww bi🌐")
st.sidebar.success("Waaw🌨️🌨️ \n Deedeete⛅⛅")

# Fonction données d'entrée 
def user_input(Evaporation,Sunshine,WindSpeed,Humidity,Pressure,Cloud,Temp):
    data = np.array([Evaporation,Sunshine,
                     WindSpeed,Humidity,
                     Pressure,Cloud,Temp])
    
    prediction_data = model.predict(data.reshape(1,-1))
    return prediction_data

# L'utilisateur saisie une valeur pour chaque caractére
st.info("Dalal akk jàmm si xarala biy seytu asamaan si ⛅🌨️")
Evaporation = st.number_input("Évaporation:")
Sunshine = st.number_input("Soleil:")
WindSpeed = st.number_input("Vitesse du Vent:")
Humidity = st.number_input("Humidité:")
Pressure = st.number_input("Pression:")
Cloud = st.number_input("Nuage:")
Temp = st.number_input("Température:")

# Création du bouton de prediction 
if st.button("▶️"):
    prediction = user_input(Evaporation,Sunshine,WindSpeed,Humidity,Pressure,Cloud,Temp)
    st.success(prediction)


# Prévoir la creation de bot
st.sidebar.info("🤖🤖")

def main():
    question = st.sidebar.text_input("👨")
    reponse=""
    if st.sidebar.button("🆗"):
        if question == "bonjour":
             st.sidebar.write("🤖",question)  
        elif question == 'donne moi la meteo':
            reponse = "renseignez les données"
            st.sidebar.write("🤖",reponse)   
if __name__ == "__main__":
    main()