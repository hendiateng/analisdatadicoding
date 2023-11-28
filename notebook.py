# -*- coding: utf-8 -*-
"""notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14_NFuu32P30Lv9W5BsSJBuatqpREHEqv

# Proyek Analisis Data: dfharing
- Nama: Hendi
- Email: hendiateng26@gmail.com
- Id Dicoding:

## Menentukan Pertanyaan Bisnis

1. Pada jam berapa peminjaman sepeda mencapai jumlah tertinggi?
2. Pengguna dengan kategori apa yang paling banyak dalam menyewa sepeda?
3. Faktor-faktor apa saja yang memengaruhi jumlah sewa sepeda?
4. Bagaimana frekuensi peminjaman sepeda antara tahun 2011 dan tahun 2012?
5. Kondisi musim dan cuaca seperti apa yang paling memengaruhi jumlah peminjaman sepeda secara signifikan?
"""

!pip install unidecode

"""## Menyaipkan semua library yang dibutuhkan

---


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib
import unidecode
import matplotlib.image as mpimg

from google.colab import files

uploaded = files.upload()

import zipfile
import io

uploaded_file = next(iter(uploaded.keys()))
with zipfile.ZipFile(io.BytesIO(uploaded[uploaded_file]), 'r') as zip_ref:
    zip_ref.extractall("/content/")

"""## Data Wrangling

### Gathering Data

### Tabel day_df
"""

day_df = pd.read_csv("/content/day.csv")
day_df.head()

"""### Tabel hour_df"""

hour_df = pd.read_csv("/content/hour.csv")
hour_df.head()

"""### Assessing Data

### Menilai tabel day_df

### Cek tipe data
"""

day_df.info()

"""### Cek missing value

"""

day_df.isna().sum()

"""### Cek duplikasi data"""

print("Jumlah duplikasi:", day_df.duplicated().sum())

"""### Cek parameter statistik"""

day_df.describe()

"""### Menilai tabel hour_df

### Cek tipe data
"""

hour_df.info()

"""### Cek missing value"""

hour_df.isna().sum()

"""### Cek duplikasi data"""

print("Jumlah duplikasi:", hour_df.duplicated().sum())

"""### Cek parameter statistik"""

hour_df.describe()

"""### Cleaning Data

### Membersihkan tabel day_df

### Memperbaiki tipe data

Mengubah nama kolom agar lebih mudah dibaca dan dipahami
"""

day_df.rename(columns={
    "dteday": "dateday",
    "yr": "year",
    "mnth": "month",
    "weathersit": "weather",
    "cnt": "count"
}, inplace=True)

"""Mengubah tipe data kolom "dateday" ke datetime"""

day_df["dateday"] = pd.to_datetime(day_df["dateday"])

"""Mengganti value dalam beberapa kolom dari integer menjadi string"""

# kolom year
day_df["year"] = day_df["dateday"].dt.year

# kolom month
day_df["month"] = day_df["dateday"].dt.month_name()

# kolom weekday
day_df["weekday"] = day_df["dateday"].dt.day_name()

# kolom season
day_df["season"] = day_df["season"].map({
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
})

# kolom weather
day_df["weather"] = day_df["weather"].map({
    1: "Clear/Partly Cloudy",
    2: "Misty",
    3: "Light Snow/Rain",
    4: "Heavy Rainstorm"
})

# kolom holiday
day_df["holiday"] = day_df["holiday"].map({
    0: "No",
    1: "Yes"
})

# kolom workingday
day_df["workingday"] = day_df["workingday"].map({
    0: "No",
    1: "Yes"
})

"""Mengubah tipe data kolom berikut menjadi kategori"""

columns = ["season", "year", "month", "holiday", "weekday", "workingday", "weather"]

for col in columns:
  day_df[col] = day_df[col].astype("category")

day_df.info()

"""### Membersihkan tabel hour_df

Mengubah nama kolom agar lebih mudah dibaca dan dipahami
"""

hour_df.rename(columns={
    "dteday": "dateday",
    "yr": "year",
    "mnth": "month",
    "hr": "hour",
    "weathersit": "weather",
    "cnt": "count"
}, inplace=True)

hour_df["dateday"] = pd.to_datetime(hour_df["dateday"])

hour_df.info()

"""Mengganti value dalam kolom yang bertipe data kategori dari integer menjadi string"""

# kolom year
hour_df["year"] = hour_df["dateday"].dt.year

# kolom month
hour_df["month"] = hour_df["dateday"].dt.month_name()

# kolom weekday
hour_df["weekday"] = hour_df["dateday"].dt.day_name()

# kolom season
hour_df["season"] = hour_df["season"].map({
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
})

# kolom weather
hour_df["weather"] = hour_df["weather"].map({
    1: "Clear/Partly Cloudy",
    2: "Misty",
    3: "Light Snow/Rain",
    4: "Heavy Rainstorm"
})

# kolom holiday
hour_df["holiday"] = hour_df["holiday"].map({
    0: "No",
    1: "Yes"
})

# kolom workingday
hour_df["workingday"] = hour_df["workingday"].map({
    0: "No",
    1: "Yes"
})

"""Mengubah tipe data kolom berikut menjadi kategori

"""

columns = ["season", "year", "month", "hour", "holiday", "weekday", "workingday", "weather"]

for col in columns:
  hour_df[col] = hour_df[col].astype("category")

"""## Exploratory Data Analysis (EDA)

## Explore day_df
"""

day_df.sample(5)

hour_df.sample(5)

day_df

hour_df

"""Mengelompokkan jumlah sewa sepeda berdasarkan bulan"""

day_df.groupby(by="month").agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum"
})

"""Mengelompokkan jumlah sewa sepeda berdasarkan kondisi musim dan cuaca

"""

day_df.groupby(by=["season", "weather"]).agg({
    "count": ["min", "max", "sum"]
})

"""Mengelompokkan jumlah sewa sepeda berdasarkan kondisi musim dan cuaca

"""

day_df.groupby(by="holiday")["count"].sum()

day_df.groupby(by="workingday")["count"].sum()

"""Melihat hubungan korelasi antar kolom

"""

day_df[["temp", "atemp", "hum", "windspeed", "count"]].corr()

"""## Explore Data hour_df

Mengelompokkan jumlah sewa sepeda berdasarkan jam
"""

hour_df.groupby(by="hour")["count"].sum().sort_values(ascending=False)

"""## Visualization & Explanatory Analysis

### Pertanyaan 1: Pada jam berapa peminjaman sepeda mencapai jumlah tertinggi?
"""

plt.figure(figsize=(10, 5))
colors = ["#72BCD4"]

sns.barplot(
    data=hour_df.groupby(by="hour")["count"].sum().reset_index(),
    x="hour",
    y="count",
    palette=colors
)
plt.title("Number of Rentals by Hours", loc="center", fontsize=15)
plt.xlabel(None)
plt.ylabel(None)

plt.show()

"""### Pertanyaan 2: Pengguna dengan kategori apa yang paling banyak dalam menyewa sepeda?"""

# mengurutkan hari
day_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_df["weekday"] = pd.Categorical(day_df["weekday"], categories=day_order, ordered=True)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=day_df["weekday"],
    y=day_df["registered"],
    label="registered",
    errorbar=None,
    color="#72BCD4"
)

sns.barplot(
    x=day_df["weekday"],
    y=day_df["casual"],
    label="casual",
    errorbar=None,
    color="#D3D3D3"
)

plt.title("Number of Bike Rentals per Week", loc="center", fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend()
plt.show()

"""### Pertanyaan 3: Faktor-faktor apa saja yang memengaruhi jumlah sewa sepeda?"""

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
colors=["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe"]

sns.scatterplot(
    data=day_df,
    x="temp",
    y="count",
    hue="season",
    palette=colors,
    ax=ax[0][0]
)
ax[0][0].set_title("Temperature vs Bike Rental Count", loc="center", fontsize=15)
ax[0][0].set_xlabel(None)
ax[0][0].set_ylabel(None)

sns.scatterplot(
    data=day_df,
    x="atemp",
    y="count",
    hue="season",
    palette=colors,
    ax=ax[0][1]
)
ax[0][1].set_title("Feeling Temperature vs Bike Rental Count", loc="center", fontsize=15)
ax[0][1].set_xlabel(None)
ax[0][1].set_ylabel(None)

sns.scatterplot(
    data=day_df,
    x="hum",
    y="count",
    hue="season",
    palette=colors,
    ax=ax[1][0]
)
ax[1][0].set_title("Humidity vs Bike Rental Count", loc="center", fontsize=12)
ax[1][0].set_xlabel(None)
ax[1][0].set_ylabel(None)

sns.scatterplot(
    data=day_df,
    x="windspeed",
    y="count",
    hue="season",
    palette=colors,
    ax=ax[1][1]
)
ax[1][1].set_title("Windspeed vs Bike Rental Count", loc="center", fontsize=12)
ax[1][1].set_xlabel(None)
ax[1][1].set_ylabel(None)

plt.show()

"""### Pertanyaan 4: Bagaimana frekuensi peminjaman sepeda antara tahun 2011 dan tahun 2012?"""

# mengurutkan bulan
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
day_df["month"] = pd.Categorical(day_df["month"], categories=month_order, ordered=True)

monthly_day_df = day_df.groupby(by=["month", "year"]).agg({
    "casual": "sum",
    "registered": "sum",
    "count":"sum"
}).reset_index()

plt.figure(figsize=(12, 5))
sns.lineplot(
    data=monthly_day_df,
    x="month",
    y="count",
    hue="year",
    marker="o",
    linewidth=2,
    palette=["#FFADA8", "#72BCD4"]
)
plt.title("Frequency of Bike Rentals per Month", loc="center", fontsize=20)
plt.xlabel(None)
plt.ylabel(None)
plt.xticks(rotation=15)

plt.show()

"""### Pertanyaan 5: Kondisi musim dan cuaca seperti apa yang paling memengaruhi jumlah peminjaman sepeda secara signifikan?"""

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    data=day_df,
    x="season",
    y="count",
    palette=colors,
    errorbar=None,
    ax=ax[0]
)
ax[0].set_title("Number of Rentals by Season", loc="center", fontsize=20)
ax[0].set_xlabel(None)
ax[0].set_ylabel(None)


sns.barplot(
    data=day_df,
    x="weather",
    y="count",
    palette=colors,
    errorbar=None,
    ax=ax[1]
)
ax[1].set_title("Number of Rentals by Weather ", loc="center", fontsize=20)
ax[1].set_xlabel(None)
ax[1].set_ylabel(None)

plt.show()

"""## Conclusion

- Conclution pertanyaan 1: Pada jam berapa peminjaman sepeda mencapai jumlah tertinggi?

Jumlah sewa mencapai puncak nya pada pukul 17.00, kemudian pada pukul 18.00 dan pukul 08.00

- Conclusion pertanyaan 2: Pengguna dengan kategori apa yang paling banyak dalam menyewa sepeda?

Pengguna dengan kategori registered merupakan penyewa sepeda

- Conclusion pertanyaan 3: Faktor-faktor apa saja yang memengaruhi jumlah sewa sepeda?

Temperature, feeling temperature, humidity, dan windspeed dengan hubungan seperti berikut:

Semakin besar nilai temperature dan feeling temperature, semakin banyak pula jumlah sewa sepeda. (bersesuaian)
Semakin besar nilai humidity dan windspeed, semakin sedikit pula jumlah sewa sepeda. (berlawanan)

- Conclusion pertanyaan 4: Bagaimana frekuensi peminjaman sepeda antara tahun 2011 dan tahun 2012?

1. Jumlah sewa sepeda terbanyak pada tahun 2011 di bulan Juni, sedangkan pada tahun 2012 di bulan September.
2. Terdapat penurunan jumlah peminjaman sepeda di tahun 2011 dan 2012 pada bulan Oktober, November, dan Desember.

Conclusion pertanyaan 5: Kondisi musim dan cuaca seperti apa yang paling memengaruhi jumlah peminjaman sepeda secara signifikan?

Jumlah sewa sepeda dengan total peminjaman yang paling banyak terjadi di musim gugur (Fall) dan kondisi cuaca relatif cerah (Clear/Partly Cloudy).

Sedangkan yang paling sedikit terjadi di musim semi (Spring) dan kondisi cuaca salju atau hujan ringan (Light Snow/Rain)

## Export Clean Dataset
"""

day_df.to_csv("/content/cleaned_day.csv", index=False)