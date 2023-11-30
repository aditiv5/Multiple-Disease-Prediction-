import numpy as np
import pickle
import streamlit as st

st.set_page_config(layout="wide")

# loading the saved model
loaded_model = pickle.load(open("prognosis2_model.sav", 'rb'))


def disease_prediction(input_data):
    # Ensure input_data is a list or array
    if not isinstance(input_data, (list, np.ndarray)):
        raise ValueError("Input data should be a list or numpy array")

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Predict the disease
    prediction = loaded_model.predict(input_data_reshaped)

    # Return the prediction as a string
    return prediction[0]
    if (prediction == 'Diabetes'):
        return 'The person has Diabetes'
    elif (prediction == 'Heart disease'):
        return 'The person has Heart disease'
    elif (prediction == 'Parkinsons disease'):
        return 'The person has Parkinsons disease'
    elif (prediction == 'Gastritis'):
        return 'The person has Gastritis'
    else:
        return 'The person is Healthy'


def main():
    # giving a title
    st.title('Multiple Disease Prediction')
    options = [0, 1]
    Chest_pain = 1
    # getting the input data from the user
    # gender,age,hypertension,smoking_history,bmi,Urinating_often,Chest_ pain,Tremor,upper_abdomain_pain

    g1 = ['Male', 'Female']
    g2 = (st.radio('Gender', g1))
    if g2 == 'Male':
        gender = 1
    else:
        gender = 0

    age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)

    place_of_livings = ['Urban', 'Rural']
    place_of_livingss = (st.radio('Place of living', place_of_livings))
    if place_of_livingss == 'Urban':
        place_of_living = 1
    else:
        place_of_living = 0

    smoking_historyS = ['Never', 'Current']
    smoking_historyss = st.radio("Smoking History", smoking_historyS)
    if smoking_historyss == 'Never':
        smoking_history = 0
    else:
        smoking_history = 1

    d = ["Drinker", "Not a Drinker"]
    drinkings = st.radio("Drinking History", d)
    if drinkings == 'Drinker':
        drinking = 0
    else:
        drinking = 1

    c1 = ['Yes', 'No']
    covids = st.radio('Covid History', c1)
    if covids == 'Yes':
        covid = 1
    else:
        covid = 0

    icon_size = '20'
    # code for Prediction
    diagnosis = ''
    # creating a button for Prediction
    if age > 0:
        if st.button("Multiple Disease Test Result"):
            input_data = [gender, age, place_of_living, smoking_history, 23, drinking, 1, Chest_pain, 1, 0, 0, 1]
            diagnosis = disease_prediction(input_data)
            if age <= 35 and drinking == 1 and covid == 0 and smoking_history == 0:
                st.success('The Person is Healthy')
            else:
                st.success(f'The predicted disease is: {diagnosis}')
                s = st.write("Tips to overcome")
                if diagnosis == "Heart_disease":
                    st.write("1. Don't smoke or use tobacco")
                    st.write("2. Get moving: Aim for at least 30 to 60 minutes of activity daily")
                    st.write("3. Eat a heart-healthy diet")
                    st.write("4. Maintain a healthy weight")
                    st.write("5. Get quality sleep")
                    st.write("6. Manage stress")
                    st.write("7. Get regular health screening tests")
                    st.write("8. Take steps to prevent infections")
                elif diagnosis == 'Diabetes':
                    st.write("1. Reduce your total carb intake")
                    st.write("2. Exercise regularly")
                    st.write("3. Drink water as your primary beverage")
                    st.write("4. Try to lose excess weight")
                    st.write("5. Minimize your intake of highly processed foods")
                    st.write("6. Quit smoking")
                elif diagnosis == 'Gastritis':
                    st.write("1. Engaging in handwashing habits to preventTrusted Source H. pylori infections")
                    st.write(
                        "2. Managing stressful situations to reduceTrusted Source the chance of having stress-induced gastritis")
                    st.write("3. Avoiding eating spicy foods")
                    st.write("4. Limiting caffeine consumption")
                    st.write("5. Limiting alcohol consumption")
                elif diagnosis == 'Parkinsons_disease':
                    st.write("1. Exercising regularly")
                    st.write("2. Eating a healthy diet")
                    st.write("3. Avoiding exposure to toxins")
                    st.write("4. Managing stress")
                    st.write("5. Getting enough sleep")


if __name__ == '__main__':
    main()
