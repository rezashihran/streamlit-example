import streamlit as st
import pandas as pd
from streamlit.beta_columns import st_beta_columns

# Here's your DataFrame
df_t = pd.read_csv('column_items.csv')
rules = pd.read_csv('rules_items.csv')
rules10 = pd.read_csv('rules10_items.csv')

column_names = df_t.columns.tolist()

# Add a title
st.title('Top 10 Highest Support')

# Replace the antecedents and consequents columns with desired text in rules DataFrame
rules['antecedents'] = rules['antecedents'].apply(lambda x: x.replace("frozenset({'", "").replace("food',", "").replace("(", "").replace("{", "").replace("'", "").replace("})", "").strip())
rules['consequents'] = rules['consequents'].apply(lambda x: x.replace("frozenset({'", "").replace("food',", "").replace("(", "").replace("{", "").replace("'", "").replace("})", "").strip())

# Replace the antecedents and consequents columns with desired text in rules10 DataFrame
rules10['antecedents'] = rules10['antecedents'].apply(lambda x: x.replace("frozenset({'", "").replace("food',", "").replace("(", "").replace("{", "").replace("'", "").replace("})", "").strip())
rules10['consequents'] = rules10['consequents'].apply(lambda x: x.replace("frozenset({'", "").replace("food',", "").replace("(", "").replace("{", "").replace("'", "").replace("})", "").strip())

# Add a multiselect box for the user to select 'pilih barang' from df_t
selected_items = st.multiselect(
    'Select Columns',
    column_names)

# If no items are selected, show top 10 highest support for all data.
# If any item is selected, filter data based on user selection and show top 10 highest support for selected items.
if not selected_items:
    st.subheader('Top 10 for All data with 5% Support')
    rules.sort_values('support', ascending=False, inplace=True)
    
    # Display tables side by side
    col1, col2 = st_beta_columns(2)
    with col1:
        st.dataframe(rules[:10])

    st.subheader('Top 10 for All data with 1% Support')
    rules10.sort_values('support', ascending=False, inplace=True)
    with col2:
        st.dataframe(rules10[:10])
else:
    st.subheader(f'Top 10 for All data with 5% Support')
    filtered_rules = rules[rules['antecedents'].apply(lambda x: any(item in selected_items for item in x.split(',')))]
    filtered_rules.sort_values('support', ascending=False, inplace=True)
    
    # Display tables side by side
    col1, col2 = st_beta_columns(2)
    with col1:
        st.dataframe(filtered_rules[:10])

    st.subheader(f'Top 10 for All data with 1% Support')
    filtered_rules10 = rules10[rules10['antecedents'].apply(lambda x: any(item in selected_items for item in x.split(',')))]
    filtered_rules10.sort_values('support', ascending=False, inplace=True)
    with col2:
        st.dataframe(filtered_rules10[:10])
