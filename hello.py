import streamlit as st
import numpy as np
import datetime

st.header("This is my first we app",divider='rainbow',help="Header_1")
st.header("Stream lit is :blue[cool] :sunglasses:",help="Header_2")

code = '''
def fun():
    print("Hello")
'''
st.code(code,language="python",line_numbers=True)

l = st.checkbox(label="This is just checkbox",value = True, key = 1000,help = "my first check box",\
             label_visibility= "visible")

if l:
    st.write("Successful")


# Create checkboxes with unique keys
checkbox_states = {
    "Option 1": st.checkbox("Option 1", key="checkbox_1"),
    "Option 2": st.checkbox("Option 2", key="checkbox_2"),
    "Option 3": st.checkbox("Option 3", key="checkbox_3")
}

# Create a button to check the status of all checkboxes
if st.button("Submit"):
    st.write(checkbox_states["Option 3"])
    # st.write("Checkbox Summary:")
    # for option, state in checkbox_states.items():
    #     st.write(f"{option}: {'Selected' if state else 'Not Selected'}")

# Define a callback function
def checkbox_callback(value, message):
    st.session_state.last_message = message
    st.write(f"Checkbox state changed: {value}")
    st.write(f"Additional message: {message}")

# Create a checkbox with on_change, args, kwargs, and disabled parameters
checkbox_value = st.checkbox(
    "Click me!",
    key="example_checkbox",
    on_change=checkbox_callback,
    args=(st.session_state, "Sainadh Bahadursha"),
    # kwargs={"message": "This is an extra message."},
    disabled=False # Set to True to disable the checkbox
)

k = st.checkbox("I agree to enter the password",key = "checkbox for password",help = "password agree or not")
d = True
if k:
    d = False
st.text_input(label = "Enter the password",placeholder="PASSWORD",max_chars=16, key = "text_input_1",\
              type = "password",help = "Enter the text", label_visibility="visible", disabled=d)

st.header("COLUMNS",divider=True)
col1,col2 = st.columns(2)
with col1:
    st.subheader("line chart")
    np.random.seed(42)
    st.line_chart(np.random.rand(100))
with col2:
    st.header("bar chart")
    st.bar_chart(np.random.rand(100))

st.date_input(label="Enter the Date",key="date_input_1",help = "this is help for date input",\
              format = "DD/MM/YYYY", min_value=datetime.date(2023,1,1),max_value=datetime.date.today())


