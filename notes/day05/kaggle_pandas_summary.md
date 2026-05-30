# Kaggle Learn Pandas Özeti

Bu dosya, Kaggle Learn Pandas kursundaki ana dersleri staj hazırlığı için özetler.  
Amaç: pandas temelini özellikle data analysis, veri temizleme, SQL sonrası analiz ve Power BI öncesi hazırlık için tekrar etmek.

## İçindekiler

1. Creating, Reading and Writing  
2. Indexing, Selecting and Assigning  
3. Summary Functions and Maps  
4. Grouping and Sorting  
5. Data Types and Missing Values  
6. Renaming and Combining  
7. En Önemli pandas Kavramları  
8. Sık Kullanılan Tek Satırlık pandas Çözümleri  
9. Staj İçin pandas Çalışma Notları  

---

# 1. Creating, Reading and Writing

Bu bölüm pandas’ta veri oluşturmayı, CSV/Excel gibi dosyalardan veri okumayı ve sonuçları dosyaya yazmayı anlatır.

## pandas import

```python
import pandas as pd
```

## DataFrame nedir?

DataFrame, satır ve kolonlardan oluşan tablo yapısıdır. SQL tablosuna veya Excel sheet’ine benzetilebilir.

```python
data = {
    "product": ["Laptop", "Mouse", "Keyboard"],
    "price": [35000, 750, 1500],
    "quantity": [2, 5, 3]
}

df = pd.DataFrame(data)
```

## Series nedir?

Series, tek kolonluk veri yapısıdır.

```python
prices = pd.Series([35000, 750, 1500])
```

İsimli index ile Series oluşturulabilir:

```python
prices = pd.Series(
    [35000, 750, 1500],
    index=["Laptop", "Mouse", "Keyboard"]
)
```

## CSV okuma

```python
df = pd.read_csv("data/sales.csv")
```

## Excel okuma

```python
df = pd.read_excel("data/sales.xlsx")
```

## İlk satırları görme

```python
df.head()
df.head(10)
```

## Dosyaya yazma

```python
df.to_csv("data/cleaned_sales.csv", index=False)
df.to_excel("data/cleaned_sales.xlsx", index=False)
```

## Tek satırlık çözümler

```python
import pandas as pd
df = pd.read_csv("data/sales.csv")
df.head()
df.head(10)
df.to_csv("data/cleaned_sales.csv", index=False)
```

## Tüyo

`index=False` kullanmazsan pandas CSV’ye fazladan index kolonu ekleyebilir. Çoğu durumda dışa aktarırken `index=False` kullanmak daha temizdir.

---

# 2. Indexing, Selecting and Assigning

Bu bölüm DataFrame içinden kolon, satır ve belirli hücreleri seçmeyi anlatır.

## Kolon seçme

```python
df["price"]
```

Alternatif nokta notasyonu:

```python
df.price
```

Ama en güvenli yöntem köşeli parantezdir:

```python
df["price"]
```

## Birden fazla kolon seçme

```python
df[["product", "price"]]
```

## Satır seçme: iloc

`iloc`, integer position ile seçim yapar.

```python
df.iloc[0]
df.iloc[:5]
df.iloc[:5, :2]
```

## Satır/kolon seçme: loc

`loc`, label yani kolon/index isimleriyle seçim yapar.

```python
df.loc[0, "product"]
df.loc[:, ["product", "price"]]
```

## Koşullu filtreleme

```python
df[df["price"] > 1000]
```

Birden fazla koşul:

```python
df[(df["price"] > 1000) & (df["quantity"] > 1)]
```

`or` mantığı:

```python
df[(df["city"] == "Izmir") | (df["city"] == "Istanbul")]
```

## isin()

```python
df[df["city"].isin(["Izmir", "Istanbul", "Ankara"])]
```

## Yeni kolon oluşturma

```python
df["total_sales"] = df["price"] * df["quantity"]
```

## Sabit değer atama

```python
df["currency"] = "TRY"
```

## Tek satırlık çözümler

```python
df["price"]
df[["product", "price"]]
df.iloc[0]
df.iloc[:5]
df.loc[:, ["product", "price"]]
df[df["price"] > 1000]
df[(df["price"] > 1000) & (df["quantity"] > 1)]
df[df["city"].isin(["Izmir", "Istanbul"])]
df["total_sales"] = df["price"] * df["quantity"]
```

## Tüyo

Koşullu filtrelemede her koşulu paranteze al:

```python
df[(df["price"] > 1000) & (df["quantity"] > 1)]
```

---

# 3. Summary Functions and Maps

Bu bölüm veri hakkında hızlı özet bilgiler almayı ve değerleri dönüştürmeyi anlatır.

## Hızlı özet fonksiyonları

```python
df.describe()
df.info()
df.shape
df["category"].unique()
df["category"].value_counts()
```

## Ortalama, medyan, min, max

```python
df["price"].mean()
df["price"].median()
df["price"].min()
df["price"].max()
```

## map()

Series üzerinde değer dönüştürmek için kullanılır.

```python
df["category_lower"] = df["category"].map(lambda x: x.lower())
```

## apply()

Satır veya kolon bazlı fonksiyon uygulamak için kullanılır.

```python
df["total_sales"] = df.apply(lambda row: row["price"] * row["quantity"], axis=1)
```

## Tek satırlık çözümler

```python
df.describe()
df.info()
df.shape
df["category"].unique()
df["category"].value_counts()
df["price"].mean()
df["price"].median()
df["price"].max()
df["category_lower"] = df["category"].map(lambda x: x.lower())
df["total_sales"] = df.apply(lambda row: row["price"] * row["quantity"], axis=1)
```

## Tüyo

Basit kolonlar arası matematik için `apply()` yerine vektörel işlem daha iyidir:

```python
df["total_sales"] = df["price"] * df["quantity"]
```

Bu kullanım genelde daha kısa, daha okunabilir ve daha hızlıdır.

---

# 4. Grouping and Sorting

Bu bölüm veriyi kategorilere göre gruplamayı ve sıralamayı anlatır.

## groupby()

```python
df.groupby("category")
```

## Kategoriye göre toplam satış

```python
df.groupby("category")["total_sales"].sum()
```

## Şehre göre ortalama satış

```python
df.groupby("city")["total_sales"].mean()
```

## Birden fazla aggregate

```python
df.groupby("category")["total_sales"].agg(["count", "sum", "mean", "max"])
```

## Birden fazla kolona göre gruplama

```python
df.groupby(["city", "category"])["total_sales"].sum()
```

## sort_values()

```python
df.sort_values("price")
df.sort_values("price", ascending=False)
```

## groupby sonucu sıralama

```python
df.groupby("category")["total_sales"].sum().sort_values(ascending=False)
```

## reset_index()

Groupby sonucunu tekrar tablo gibi görmek için kullanılır.

```python
category_sales = df.groupby("category")["total_sales"].sum().reset_index()
```

## Tek satırlık çözümler

```python
df.groupby("category")["total_sales"].sum()
df.groupby("city")["total_sales"].mean()
df.groupby("category")["total_sales"].agg(["count", "sum", "mean"])
df.groupby(["city", "category"])["total_sales"].sum()
df.sort_values("price", ascending=False)
df.groupby("category")["total_sales"].sum().sort_values(ascending=False)
category_sales = df.groupby("category")["total_sales"].sum().reset_index()
```

## Tüyo

SQL’deki `GROUP BY` mantığı pandas’ta çoğunlukla `groupby()` ile yapılır.

SQL:

```sql
SELECT category, SUM(total_sales)
FROM sales
GROUP BY category;
```

pandas:

```python
df.groupby("category")["total_sales"].sum()
```

---

# 5. Data Types and Missing Values

Bu bölüm veri tiplerini kontrol etmeyi, dönüştürmeyi ve eksik verilerle çalışmayı anlatır.

## dtypes

```python
df.dtypes
```

## astype()

```python
df["price"] = df["price"].astype(float)
df["product_id"] = df["product_id"].astype(str)
```

## to_datetime()

```python
df["order_date"] = pd.to_datetime(df["order_date"])
```

## Eksik değer kontrolü

```python
df.isnull()
df.isnull().sum()
df.notnull()
```

## fillna()

```python
df["city"] = df["city"].fillna("Unknown")
df["price"] = df["price"].fillna(df["price"].mean())
```

## dropna()

```python
df = df.dropna()
```

## replace()

```python
df["city"] = df["city"].replace("İzmir", "Izmir")
```

## Tek satırlık çözümler

```python
df.dtypes
df["price"] = df["price"].astype(float)
df["order_date"] = pd.to_datetime(df["order_date"])
df.isnull().sum()
df["city"] = df["city"].fillna("Unknown")
df["price"] = df["price"].fillna(df["price"].mean())
df = df.dropna()
df["city"] = df["city"].replace("İzmir", "Izmir")
```

## Tüyo

Eksik değerleri direkt silmeden önce neden eksik olduklarını düşün. Her `NaN` yanlış veri anlamına gelmez. Bazen bilgi gerçekten yoktur, bazen veri toplama hatası vardır.

---

# 6. Renaming and Combining

Bu bölüm kolon isimlerini değiştirmeyi ve farklı DataFrame’leri birleştirmeyi anlatır.

## rename()

```python
df = df.rename(columns={"old_name": "new_name"})
df = df.rename(columns={"total_amount": "total_sales"})
```

## index adı değiştirme

```python
df = df.rename_axis("row_id", axis="rows")
```

## concat()

DataFrame’leri alt alta veya yan yana birleştirmek için kullanılır.

```python
combined = pd.concat([df_january, df_february])
```

## join()

Index üzerinden birleştirme yapar.

```python
joined = left_df.join(right_df)
```

## merge()

Ortak kolon üzerinden birleştirme için çok kullanılır.

```python
merged = pd.merge(customers, orders, on="customer_id")
```

Farklı kolon adları varsa:

```python
merged = pd.merge(
    customers,
    orders,
    left_on="id",
    right_on="customer_id"
)
```

## Tek satırlık çözümler

```python
df = df.rename(columns={"old_name": "new_name"})
df = df.rename(columns={"total_amount": "total_sales"})
combined = pd.concat([df_january, df_february])
merged = pd.merge(customers, orders, on="customer_id")
merged = pd.merge(customers, orders, left_on="id", right_on="customer_id")
```

## Tüyo

SQL’deki `JOIN` mantığının pandas karşılığı çoğu durumda `merge()` fonksiyonudur.

SQL:

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

pandas:

```python
merged = pd.merge(customers, orders, on="customer_id")
```

---

# 7. En Önemli pandas Kavramları

```python
pd.read_csv()       # CSV dosyası okur
pd.DataFrame()      # tablo oluşturur
Series              # tek kolonluk veri yapısı
DataFrame           # tablo veri yapısı
df.head()           # ilk satırları gösterir
df.info()           # kolon ve tip bilgisi gösterir
df.describe()       # özet istatistik verir
df.shape            # satır/kolon sayısı verir
df["column"]        # kolon seçer
df.loc[]            # label ile seçim yapar
df.iloc[]           # index pozisyonu ile seçim yapar
df.groupby()        # gruplama yapar
df.sort_values()    # sıralama yapar
df.isnull().sum()   # eksik değer sayısı verir
df.fillna()         # eksik değer doldurur
df.dropna()         # eksik değerli satırları siler
pd.to_datetime()    # tarih tipine çevirir
pd.merge()          # tabloları ortak kolondan birleştirir
pd.concat()         # tabloları alt alta/yan yana birleştirir
df.to_csv()         # CSV dosyasına yazar
```

---

# 8. Sık Kullanılan Tek Satırlık pandas Çözümleri

## CSV oku

```python
df = pd.read_csv("data/sales.csv")
```

## İlk satırları göster

```python
df.head()
```

## Veri hakkında hızlı bilgi al

```python
df.info()
```

## Eksik değerleri say

```python
df.isnull().sum()
```

## Belirli kolonları seç

```python
df[["product", "price", "quantity"]]
```

## Fiyatı 1000’den büyük ürünleri filtrele

```python
df[df["price"] > 1000]
```

## Yeni total_sales kolonu oluştur

```python
df["total_sales"] = df["price"] * df["quantity"]
```

## Kategoriye göre toplam satış

```python
df.groupby("category")["total_sales"].sum()
```

## Şehre göre toplam satış

```python
df.groupby("city")["total_sales"].sum()
```

## Aylık satış trendi

```python
df["order_date"] = pd.to_datetime(df["order_date"])
monthly_sales = df.groupby(df["order_date"].dt.to_period("M"))["total_sales"].sum()
```

## En yüksek satış yapan kategoriler

```python
df.groupby("category")["total_sales"].sum().sort_values(ascending=False)
```

## Eksik şehir bilgisini doldur

```python
df["city"] = df["city"].fillna("Unknown")
```

## Temizlenmiş CSV üret

```python
df.to_csv("data/cleaned_sales.csv", index=False)
```

---

# 9. Staj İçin pandas Çalışma Notları

Staj hazırlığında pandas tarafında özellikle şunlara odaklan:

```text
CSV okuma
DataFrame mantığı
Kolon seçme
Satır filtreleme
Yeni kolon oluşturma
Eksik veri kontrolü
Veri tipi dönüştürme
groupby ile özet çıkarma
sort_values ile sıralama
merge ile tablo birleştirme
to_csv ile çıktı üretme
```

Bir data analytics görevinde pandas genelde şu amaçlarla kullanılır:

```text
SQL’den veya CSV’den gelen veriyi incelemek
Eksik/veri tipi sorunlarını temizlemek
Yeni metrik kolonları oluşturmak
Kategori, şehir, tarih gibi alanlara göre analiz yapmak
Grafik veya dashboard öncesi veri hazırlamak
Temizlenmiş veri dosyası üretmek
```

## pandas çalışırken düşünme sırası

```text
1. Veri dosyasını okudum mu?
2. İlk satırlara baktım mı?
3. Kolonları ve veri tiplerini kontrol ettim mi?
4. Eksik değer var mı?
5. Duplicate var mı?
6. Gerekli yeni kolonları oluşturdum mu?
7. Hangi business question’ı cevaplıyorum?
8. groupby veya filtre gerekiyor mu?
9. Sonucu dışa aktarmam gerekiyor mu?
```

## Mini pratik önerisi

Bir satış datası üzerinde şu işlemleri yap:

```text
CSV oku
Eksik değerleri kontrol et
total_sales = price * quantity kolonu oluştur
Kategoriye göre toplam satış bul
Şehre göre toplam satış bul
Aylık satış trendi çıkar
En çok satan 10 ürünü bul
Temizlenmiş CSV dosyası üret
```

---

# Repo İçinde Önerilen Konum

Bu dosyayı repo içinde şu konuma koyabilirsin:

```text
notes/kaggle_pandas_summary.md
```

README link önerisi:

```md
- [Kaggle Pandas summary - Markdown](notes/kaggle_pandas_summary.md)
```
