import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
# Draw a title and some text to the app:
'''
# Streamlit magic writes repo:1

This is some _markdown_.
'''
df = pd.DataFrame({'col1': [1,2,3,4,5,6,7,8,9,0], 'col2':[1,2,3,4,5,6,7,8,9,0]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types


st.header("This Will Help you to learn more easily as Accountants")
st.title("Usage")
st.write('''
    By refreashing the app again an again the new graph will be ploted which helps you alot in data handler as a deep learner
''')


random_data = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(random_data, bins=20)

fig  # 👈 Draw a Matplotlib chart