import streamlit as st
import math

st.title("Calculator")

num1 = st.number_input("Enter the first number: ")
num2 = st.number_input("Enter the second number: ")

operation = st.selectbox("Choose an operation: ",
["Addition", "Subtraction", "Multiplication", "Division", "Power", "Natural Logarithm"])

if operation == "Addition":
    result = num1 + num2
    
elif operation == "Subtraction":
    result = num1 - num2

elif operation == "Multiplication":
    result = num1 * num2

elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")

elif operation == "Power":
    result = num1 ** num2

elif operation == "Natural Logarithm":
    if num1 > 0:
        result = math.log(num1)
    else:
        print("Natural logarithm is only defined for positive numbers.")
        

st.write("Result: ", result)