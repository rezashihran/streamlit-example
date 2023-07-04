import streamlit as st
import pandas as pd

# Here's your DataFrame
df_t = pd.read_csv('column_items.csv')
rules = pd.read_csv('rules_items.csv')

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
    st.dataframe(rules[:10])
else:
    st.subheader(f'Top 10 for selected items')
    # Convert selected_items to a set for efficient membership testing
    selected_items_set = set(selected_items)
    
    # Filter rules where all selected_items appear in the antecedents
    filtered_rules = rules[
        rules['antecedents'].apply(lambda x: selected_items_set.issubset(x))
    ]
    filtered_rules.sort_values('support', ascending=False, inplace=True)
    
    # Extract text inside single quotes from antecedents and consequents columns
    filtered_rules['antecedents'] = filtered_rules['antecedents'].str.extract(r"'([^']*)'")
    filtered_rules['consequents'] = filtered_rules['consequents'].str.extract(r"'([^']*)'")
    
    st.dataframe(filtered_rules[:10])
