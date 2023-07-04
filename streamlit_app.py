%%writefile app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, check out our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Here's your DataFrame
df_t = pd.DataFrame(column_items.csv
    ...  # replace with your actual DataFrame
)
rules = pd.DataFrame(rules_items.csv
    ...  # replace with your actual rules DataFrame
)

column_names = df_t.columns.tolist()

# Add a title
st.title('Top 10 Highest Support')

# Add a multiselect box for the user to select 'pilih barang' from df_t
selected_items = st.multiselect(
    'Select Columns',
    column_names)

# If no items are selected, show top 10 highest support for all data.
# If any item is selected, filter data based on user selection and show top 10 highest support for selected items.
if not selected_items:
    st.subheader('Top 10 for all data')
    rules.sort_values('support', ascending=False, inplace=True)
    fig, ax = plt.subplots()
    rules[:10].plot(kind='bar', x='antecedents', y='support', ax=ax)
    st.pyplot(fig)
else:
    st.subheader(f'Top 10 for selected items')
    # Filter rules where any of the selected_items appear in the antecedents
    filtered_rules = rules[rules['antecedents'].apply(lambda x: any(item in selected_items for item in x))]
    filtered_rules.sort_values('support', ascending=False, inplace=True)
    fig, ax = plt.subplots()
    filtered_rules[:10].plot(kind='bar', x='antecedents', y='support', ax=ax)
    st.pyplot(fig)
