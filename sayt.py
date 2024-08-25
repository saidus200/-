import streamlit as st
a = st.number_input("number - ")
but = st.radio("next", ('plus','minus','multiplus','division','pow'))
c = st.number_input("number2 - ")
if (but == 'plus'):
    st.success(a+c)
if (but == 'minus'):
    st.success(a-c)
if (but == 'multiplus'):
    st.success(a*c)
if (but == 'division'):
    st.success(a/c)
if (but == 'pow'):
    st.success(a**c)