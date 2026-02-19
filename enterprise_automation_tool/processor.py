def process_data(df):
    df['Total'] = df['Quantity'] * df['UnitPrice']
    summary = df.groupby('Category')['Total'].sum().reset_index()
    return summary