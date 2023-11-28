import pandas as pd
import numpy as np
import plotly.graph_objs as go
import streamlit as st

st.title('Analisis Data Airtaxi')

# Baca file csv
df = pd.read_csv('data_airtaxi.csv')

# Menampilkan dataframe
st.write('Data Awal:')
st.write(df)

# Fungsi untuk menghitung average sewa per hour
def calculate_average_rent(df):
    average_rent = df.groupby('Hour')['Rent'].mean()
    return average_rent

# Menghitung average sewa per hour
average_rent = calculate_average_rent(df)

# Menampilkan average sewa per hour
st.write('Average Rent per Hour:')
st.write(average_rent)

# Fungsi untuk membuat plot kors
def correlation_heatmap(df):
    fig = go.Figure(
        data=go.Heatmap(
            z=df.corr().abs(),
            x=df.corr().abs().columns,
            y=df.corr().abs().columns,
            hoverongaps=False,
            xgap=3,
            ygap=3,
        ),
        layout=go.Layout(
            title='Plot Kors',
            xaxis=dict(title='Variabel'),
            yaxis=dict(title='Variabel'),
        )
    )
    st.plotly_chart(fig)

# Membuat plot kors
correlation_heatmap(df)

# Fungsi untuk membuat plot distribusi rent
def plot_rent_distribution(df):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df['Rent'], nbinsx=30))
    fig.update_layout(title='Distribusi Rent', xaxis_title='Rent', yaxis_title='Frekuensi')
    st.plotly_chart(fig)

# Membuat plot distribusi rent
plot_rent_distribution(df)

# Fungsi untuk membuat plot average rent per hour
def plot_average_rent_per_hour(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df, mode='lines', name='Average Rent'))
    fig.update_layout(title='Average Rent per Hour', xaxis_title='Hour', yaxis_title='Rent')
    st.plotly_chart(fig)

# Membuat plot average rent per hour
plot_average_rent_per_hour(average_rent)

# Fungsi untuk membuat plot jumlah transaksi per hour
def plot_number_of_transactions_per_hour(df):
    number_of_transactions = df.groupby('Hour')['TransactionID'].count()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=number_of_transactions.index, y=number_of_transactions, mode='lines', name='Number of Transactions'))
    fig.update_layout(title='Number of Transactions per Hour', xaxis_title='Hour', yaxis_title='Number of Transactions')
    st.plotly_chart(fig)

# Membuat plot jumlah transaksi per hour
plot_number_of_transactions_per_hour(df)
