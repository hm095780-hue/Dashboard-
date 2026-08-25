import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_excel("sales_data.xlsx")

print(df.head())
print(df.info())
df['Date'] = pd.to_datetime(df['Date'])

df = df.dropna()

print(df.isnull().sum())
total_sales = df['Sales'].sum()

total_profit = df['Profit'].sum()

total_orders = df['Order_ID'].nunique()

average_order_value = total_sales / total_orders

profit_margin = (total_profit / total_sales) * 100

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)
print("Profit Margin:", profit_margin)
monthly_sales = df.groupby(
    df['Date'].dt.to_period('M')
)['Sales'].sum().reset_index()

monthly_sales['Date'] = monthly_sales['Date'].astype(str)

fig = px.bar(
    monthly_sales,
    x='Date',
    y='Sales',
    title='Month-wise Sales'
)

fig.show()
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

fig = px.bar(
    category_sales,
    x='Category',
    y='Sales',
    title='Category-wise Sales'
)

fig.show()
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

fig = px.pie(
    region_sales,
    names='Region',
    values='Sales',
    title='Region-wise Sales'
)

fig.show()
category_profit = df.groupby('Category')['Profit'].sum().reset_index()

fig = px.bar(
    category_profit,
    x='Category',
    y='Profit',
    title='Category-wise Profit'
)

fig.show()
fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="number",
    value=total_sales,
    title={"text": "Total Sales"}
))

fig.show()
fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="number",
    value=total_sales,
    title={"text": "Total Sales"},
    domain={'row': 0, 'column': 0}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=total_profit,
    title={"text": "Total Profit"},
    domain={'row': 0, 'column': 1}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=total_orders,
    title={"text": "Total Orders"},
    domain={'row': 0, 'column': 2}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=average_order_value,
    title={"text": "Average Order Value"},
    domain={'row': 1, 'column': 0}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=profit_margin,
    title={"text": "Profit Margin %"},
    number={'suffix': "%"},
    domain={'row': 1, 'column': 1}
))

fig.update_layout(
    grid={'rows': 2, 'columns': 3}
)

fig.show()
fig.write_image("KPI_Dashboard.pdf")