import streamlit as st

st.image("C:\\Users\\PC1\\OneDrive - GFI\\Documents\\Master EHTP\\Mod_VI_Machine_learning\\Labs\\10_deploiement\\Streamlit\\app build\\Data\\logo_ehtp.png")

st.sidebar.image("https://cdn.britannica.com/39/91239-004-44353E32/Diagram-flowering-plant.jpg")
st.title("MSDE6: ML Course ")
st.header("Iris Flower Prediction App")
st.markdown("This app predicts the **iris flower** type")

st.sidebar.title("User input parameters")
data_choice = st.selectbox("Data",["Single","From file"])

# Show the sidebar inputs only if "Single" is selected
if data_choice == "Single":
    sl = st.sidebar.slider("Sepal length", 0, 10)
    sw = st.sidebar.slider("Sepal width", 0, 6)
    pl = st.sidebar.slider("Petal length", 0, 10)
    pw = st.sidebar.slider("Petal width", 0, 6)
    
    # Store values in a list
    values = [sl, sw, pl, pw]
    
    import pandas as pd

    # Create a DataFrame from the list and transpose it to store as a row
    df = pd.DataFrame(values).T
    
    
    
