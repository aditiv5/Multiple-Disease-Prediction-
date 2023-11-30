import streamlit as st


st.title("Tips To Overcome")

select = ['Heart Disease', 'Gastritis', 'Parkinson disease', 'Diabetes']

selection = st.selectbox("Select To which disease you want to prevent", select)

if selection == 'Heart Disease':
    st.write("1. Don't smoke or use tobacco")
    st.write("2. Get moving: Aim for at least 30 to 60 minutes of activity daily")
    st.write("3. Eat a heart-healthy diet")
    st.write("4. Maintain a healthy weight")
    st.write("5. Get quality sleep")
    st.write("6. Manage stress")
    st.write("7. Get regular health screening tests")
    st.write("8. Take steps to prevent infections")
elif selection == 'Gastritis':
    st.write("1. Engaging in handwashing habits to preventTrusted Source H. pylori infections")
    st.write("2. Managing stressful situations to reduceTrusted Source the chance of having stress-induced gastritis")
    st.write("3. Avoiding eating spicy foods")
    st.write("4. Limiting caffeine consumption")
    st.write("5. Limiting alcohol consumption")
elif selection == 'Parkinson disease':
    st.write("1. Exercising regularly")
    st.write("2. Eating a healthy diet")
    st.write("3. Avoiding exposure to toxins")
    st.write("4. Managing stress")
    st.write("5. Getting enough sleep")
elif selection == 'Diabetes':
    st.write("1. Reduce your total carb intake")
    st.write("2. Exercise regularly")
    st.write("3. Drink water as your primary beverage")
    st.write("4. Try to lose excess weight")
    st.write("5. Minimize your intake of highly processed foods")
    st.write("6. Quit smoking")
