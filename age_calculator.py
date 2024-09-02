import streamlit as st
from datetime import date
import calendar as cal

# Streamlit app
st.title("**** AGE CALCULATOR ****")

# Gender Input
gender = st.radio("Select your gender", ('Male', 'Female'))

# Name Input
name = st.text_input("Enter your name")

# Date of Birth Input
birth_year = st.number_input("Enter your birth year", min_value=1900, max_value=date.today().year)
birth_month = st.number_input("Enter your birth month", min_value=1, max_value=12)
birth_day = st.number_input("Enter your birth date", min_value=1, max_value=31)

# Age Calculation Mode
age_mode = st.selectbox("Select age display mode", ('Full Age', 'Years, Months, Days'))

if st.button("Calculate Age"):
    today = date.today()
    pd, pm, py = today.day, today.month, today.year

    # Basic input validation
    if birth_month > 12 or birth_day > 31:
        st.error("You have entered wrong input")
    elif py - birth_year < 0:
        st.error("You are not born yet, please contact your representatives for that")
    elif py - birth_year == 0 and pm - birth_month == 0 and pd < birth_day:
        st.error("You are not born yet, please contact your representatives for that")
    elif py - birth_year == 0 and pm - birth_month == 0 and pd == birth_day:
        st.success("You just born today!")
    else:
        # Initialize variables
        ydiff = py - birth_year
        mdiff = 12 * ydiff
        ddiff = 0
        days = 0
        ly = cal.leapdays(birth_year, py)
        ddiff = (365 * ydiff) + ly

        if pm == birth_month and pd == birth_day:
            days = 0
        elif pm == birth_month and pd < birth_day:
            ydiff -= 1
            days = 30 - (birth_day - pd)
            mdiff -= 1
            ddiff -= birth_day - pd
        elif pm > birth_month and pd > birth_day:
            days = pd - birth_day
            mdiff += pm - birth_month
            ddiff += (pd - birth_day) * 30
        elif pm < birth_month and pd < birth_day:
            days = 30 - (birth_day - pd)
            ydiff -= 1
            mdiff -= (birth_month - pm - 1)
            ddiff -= (((birth_month - pm) * 30) + (birth_day - pd))
        else:
            days = pd - birth_day
            mdiff += pm - birth_month

        if age_mode == 'Years, Months, Days':
            if gender == 'Male':
                st.info(f"Mr. {name}, your age is {ydiff} years or {mdiff} months or {ddiff} days")
            else:
                st.info(f"Ms. {name}, your age is {ydiff} year or {mdiff} months or {ddiff} days")
        else:
            # Full Age Display
            mdiff1 = pm - birth_month
            ddiff1 = pd - birth_day

            if pd < birth_day:
                mdiff1 -= 1
                ddiff1 += 30

            if mdiff1 < 0:
                ydiff -= 1
                mdiff1 += 12

            if gender == 'Male':
                st.info(f"Congrats! Mr. {name}, you have completed {ydiff} years, {mdiff1} months, and {ddiff1} days of your life")
            else:
                st.info(f"Bravo! Ms. {name}, you have completed {ydiff} years, {mdiff1} months, and {ddiff1} days of your life")

            if ydiff >= 100:
                st.warning("And I wonder how you're still alive!")

