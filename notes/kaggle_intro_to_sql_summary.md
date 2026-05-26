# Kaggle Learn Intro to SQL Özeti

Bu dosya, Kaggle Learn Intro to SQL kursundaki ana dersleri staj hazırlığı için özetler.  
Amaç: SQL temelini özellikle data analysis, pandas ve Power BI hazırlığı için tekrar etmek.

## İçindekiler

1. Getting Started With SQL and BigQuery  
2. SELECT, FROM & WHERE  
3. GROUP BY, HAVING & COUNT  
4. ORDER BY  
5. AS & WITH  
6. JOINING DATA  
7. En Önemli SQL Komutları  
8. Sık Kullanılan Tek Satırlık SQL Çözümleri  
9. Staj İçin SQL Çalışma Notları  

---

# 1. Getting Started With SQL and BigQuery

Bu bölüm SQL’in veri tabanlarından veri çekmek için kullanılan temel sorgulama dili olduğunu ve Kaggle ortamında Google BigQuery üzerinden SQL sorguları çalıştırıldığını anlatır.

## Temel kavramlar

```text
Database  -> Verilerin tutulduğu genel sistem
Dataset   -> BigQuery içinde tablo grupları
Table     -> Satır ve kolonlardan oluşan veri yapısı
Column    -> Veri alanı / attribute
Row       -> Tek kayıt / record
Query     -> Veri çekmek için yazılan SQL sorgusu
```

## SQL ne işe yarar?

SQL ile şunları yaparsın:

```text
Veri seçme
Veri filtreleme
Veri sıralama
Veri gruplama
Aggregate hesaplama
Tabloları birleştirme
Analiz için özet tablo üretme
```

## Basit sorgu yapısı

```sql
SELECT column_name
FROM table_name;
```

Örnek:

```sql
SELECT name
FROM customers;
```

## Tüyo

SQL’de sorgular genelde şu sırayla yazılır:

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

Ama çalışma mantığı tam olarak yazım sırası gibi değildir. Örneğin `WHERE`, satırlar gruplanmadan önce çalışır. `HAVING`, `GROUP BY` sonrası oluşan grupları filtreler.

---

# 2. SELECT, FROM & WHERE

Bu bölüm en temel SQL sorgu yapısını anlatır.

## SELECT

Hangi kolonları görmek istediğini belirtir.

```sql
SELECT name, age
FROM users;
```

Tüm kolonları almak için `*` kullanılır:

```sql
SELECT *
FROM users;
```

## FROM

Verinin hangi tablodan geleceğini belirtir.

```sql
SELECT city
FROM customers;
```

## WHERE

Satırları filtrelemek için kullanılır.

```sql
SELECT *
FROM customers
WHERE country = 'Turkey';
```

## Karşılaştırma operatörleri

```sql
=       -- eşittir
!=      -- eşit değildir
<>      -- eşit değildir
>       -- büyüktür
<       -- küçüktür
>=      -- büyük veya eşit
<=      -- küçük veya eşit
```

Örnek:

```sql
SELECT *
FROM orders
WHERE total_amount > 1000;
```

## AND / OR / NOT

Birden fazla koşul yazmak için kullanılır.

```sql
SELECT *
FROM orders
WHERE total_amount > 1000
  AND city = 'Izmir';
```

```sql
SELECT *
FROM customers
WHERE city = 'Izmir'
   OR city = 'Istanbul';
```

```sql
SELECT *
FROM products
WHERE NOT category = 'Electronics';
```

## BETWEEN

Belirli aralık için kullanılır.

```sql
SELECT *
FROM orders
WHERE total_amount BETWEEN 500 AND 1500;
```

## IN

Birden fazla olası değeri kısa yazmak için kullanılır.

```sql
SELECT *
FROM customers
WHERE city IN ('Izmir', 'Istanbul', 'Ankara');
```

## LIKE

Metin içinde pattern aramak için kullanılır.

```sql
SELECT *
FROM customers
WHERE name LIKE 'A%';
```

```text
'A%'   -> A ile başlayanlar
'%a'   -> a ile bitenler
'%an%' -> içinde an geçenler
```

## NULL kontrolü

```sql
SELECT *
FROM customers
WHERE email IS NULL;
```

```sql
SELECT *
FROM customers
WHERE email IS NOT NULL;
```

## Tek satırlık çözümler

```sql
SELECT * FROM customers;
SELECT name, city FROM customers;
SELECT * FROM orders WHERE total_amount > 1000;
SELECT * FROM customers WHERE city IN ('Izmir', 'Istanbul');
SELECT * FROM products WHERE category != 'Electronics';
SELECT * FROM customers WHERE email IS NOT NULL;
```

## Tüyo

SQL’de string değerler genelde tek tırnakla yazılır:

```sql
WHERE city = 'Izmir'
```

Sayılar tırnaksız yazılır:

```sql
WHERE age > 18
```

---

# 3. GROUP BY, HAVING & COUNT

Bu bölüm veriyi gruplamayı ve özet sonuç üretmeyi anlatır.

## COUNT

Satır saymak için kullanılır.

```sql
SELECT COUNT(*)
FROM customers;
```

Belirli bir kolondaki NULL olmayan değerleri sayar:

```sql
SELECT COUNT(email)
FROM customers;
```

## GROUP BY

Veriyi belli bir kolona göre gruplar.

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city;
```

Bu sorgu her şehirde kaç müşteri olduğunu gösterir.

## Aggregate fonksiyonlar

```sql
COUNT(*)     -- satır sayısı
SUM(column)  -- toplam
AVG(column)  -- ortalama
MIN(column)  -- minimum
MAX(column)  -- maksimum
```

Örnek:

```sql
SELECT category, SUM(total_sales) AS category_sales
FROM sales
GROUP BY category;
```

## HAVING

Gruplanmış sonuçları filtrelemek için kullanılır.

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
HAVING COUNT(*) > 10;
```

## WHERE vs HAVING

`WHERE`, gruplama yapılmadan önce satırları filtreler.

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
WHERE country = 'Turkey'
GROUP BY city;
```

`HAVING`, gruplama yapıldıktan sonra grupları filtreler.

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
HAVING COUNT(*) > 10;
```

## Tek satırlık çözümler

```sql
SELECT COUNT(*) FROM customers;
SELECT city, COUNT(*) FROM customers GROUP BY city;
SELECT category, SUM(total_sales) FROM sales GROUP BY category;
SELECT city, AVG(total_amount) FROM orders GROUP BY city;
SELECT category, MAX(price) FROM products GROUP BY category;
SELECT city, COUNT(*) FROM customers GROUP BY city HAVING COUNT(*) > 10;
```

## Tüyo

`GROUP BY` kullanıyorsan, `SELECT` içinde aggregate olmayan kolonlar genelde `GROUP BY` içinde de yer almalıdır.

Yanlış:

```sql
SELECT city, name, COUNT(*)
FROM customers
GROUP BY city;
```

Doğru:

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city;
```

---

# 4. ORDER BY

Bu bölüm sorgu sonuçlarını sıralamayı anlatır.

## ASC

Küçükten büyüğe / A’dan Z’ye sıralar. Varsayılan sıralama budur.

```sql
SELECT *
FROM products
ORDER BY price ASC;
```

## DESC

Büyükten küçüğe / Z’den A’ya sıralar.

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

## Birden fazla kolona göre sıralama

```sql
SELECT *
FROM customers
ORDER BY city ASC, name ASC;
```

## LIMIT

Sonuç sayısını sınırlar.

```sql
SELECT *
FROM products
ORDER BY price DESC
LIMIT 10;
```

Bu sorgu en pahalı 10 ürünü getirir.

## Aggregate sonuçları sıralama

```sql
SELECT category, SUM(total_sales) AS category_sales
FROM sales
GROUP BY category
ORDER BY category_sales DESC;
```

## Tek satırlık çözümler

```sql
SELECT * FROM products ORDER BY price DESC;
SELECT * FROM products ORDER BY price DESC LIMIT 10;
SELECT * FROM customers ORDER BY name ASC;
SELECT city, COUNT(*) AS count FROM customers GROUP BY city ORDER BY count DESC;
SELECT category, SUM(total_sales) AS sales FROM sales GROUP BY category ORDER BY sales DESC;
```

## Tüyo

SQL’de sonuç sırası garanti değildir. Belirli bir sıra istiyorsan mutlaka `ORDER BY` kullan.

---

# 5. AS & WITH

Bu bölüm kolon/tablo alias’larını ve CTE kullanımını anlatır.

## AS

Kolon veya tabloya geçici isim vermek için kullanılır.

```sql
SELECT total_amount AS revenue
FROM orders;
```

Aggregate kolonlara anlamlı isim vermek için çok kullanılır:

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city;
```

## Tablo alias’ı

```sql
SELECT c.name, c.city
FROM customers AS c;
```

`AS` bazı durumlarda yazılmadan da kullanılabilir:

```sql
SELECT c.name
FROM customers c;
```

## WITH

CTE yani Common Table Expression oluşturmak için kullanılır. Uzun sorguları daha okunabilir hale getirir.

```sql
WITH city_sales AS (
    SELECT city, SUM(total_amount) AS total_sales
    FROM orders
    GROUP BY city
)
SELECT *
FROM city_sales
WHERE total_sales > 10000;
```

## CTE neden kullanılır?

```text
Uzun sorguyu parçalara bölmek
Ara sonuç üretmek
Okunabilirliği artırmak
Aynı hesaplamayı daha düzenli kullanmak
```

## Tek satırlık çözümler

```sql
SELECT price * quantity AS total_price FROM order_items;
SELECT city, COUNT(*) AS customer_count FROM customers GROUP BY city;
WITH top_cities AS (SELECT city, SUM(total_amount) AS sales FROM orders GROUP BY city) SELECT * FROM top_cities;
```

## Tüyo

Alias isimlerini anlamlı seç:

Kötü:

```sql
SELECT COUNT(*) AS c
FROM customers;
```

Daha iyi:

```sql
SELECT COUNT(*) AS customer_count
FROM customers;
```

---

# 6. JOINING DATA

Bu bölüm birden fazla tabloyu bağlamayı anlatır.

## JOIN ne işe yarar?

Farklı tablolardaki ilişkili verileri birleştirir.

Örneğin:

```text
customers tablosu -> müşteri bilgileri
orders tablosu    -> sipariş bilgileri
```

Bu iki tabloyu `customer_id` üzerinden bağlayabilirsin.

## INNER JOIN

Sadece iki tabloda da eşleşen kayıtları getirir.

```sql
SELECT customers.name, orders.order_id
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

## LEFT JOIN

Soldaki tablodaki tüm kayıtları getirir. Sağ tabloda eşleşme yoksa NULL döner.

```sql
SELECT customers.name, orders.order_id
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

Bu sorgu siparişi olmasa bile tüm müşterileri getirir.

## Tablo alias ile JOIN

```sql
SELECT c.name, o.order_id
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.customer_id;
```

## JOIN + GROUP BY

```sql
SELECT c.city, COUNT(o.order_id) AS order_count
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.customer_id
GROUP BY c.city;
```

## JOIN + WHERE

```sql
SELECT c.name, o.total_amount
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE o.total_amount > 1000;
```

## Tek satırlık çözümler

```sql
SELECT c.name, o.order_id FROM customers c JOIN orders o ON c.customer_id = o.customer_id;
SELECT c.name, o.order_id FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id;
SELECT c.city, COUNT(o.order_id) AS order_count FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.city;
SELECT c.name, SUM(o.total_amount) AS total_spent FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;
```

## Tüyo

JOIN yaparken en çok hata `ON` koşulunda yapılır.  
Her zaman şu soruyu sor:

```text
Bu iki tablo hangi ortak kolon üzerinden bağlanıyor?
```

Örnek:

```sql
ON customers.customer_id = orders.customer_id
```

---

# 7. En Önemli SQL Komutları

```sql
SELECT      -- hangi kolonları getireceğini seçer
FROM        -- hangi tablodan veri çekileceğini belirtir
WHERE       -- satır filtreler
GROUP BY    -- veriyi gruplar
HAVING      -- gruplanmış sonuçları filtreler
COUNT       -- satır sayar
SUM         -- toplam alır
AVG         -- ortalama alır
MIN         -- minimum değeri bulur
MAX         -- maksimum değeri bulur
ORDER BY    -- sonucu sıralar
ASC         -- küçükten büyüğe sıralar
DESC        -- büyükten küçüğe sıralar
LIMIT       -- sonuç sayısını sınırlar
AS          -- alias verir
WITH        -- CTE oluşturur
JOIN        -- tabloları birleştirir
LEFT JOIN   -- soldaki tüm kayıtları koruyarak birleştirir
ON          -- join eşleşme koşulunu belirtir
```

---

# 8. Sık Kullanılan Tek Satırlık SQL Çözümleri

## Tüm tabloyu gör

```sql
SELECT *
FROM table_name;
```

## Belirli kolonları seç

```sql
SELECT name, city
FROM customers;
```

## Filtreleme

```sql
SELECT *
FROM orders
WHERE total_amount > 1000;
```

## Birden fazla koşul

```sql
SELECT *
FROM orders
WHERE total_amount > 1000
  AND city = 'Izmir';
```

## Şehir bazlı müşteri sayısı

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city;
```

## En yüksek satış yapan kategoriler

```sql
SELECT category, SUM(total_sales) AS sales
FROM sales
GROUP BY category
ORDER BY sales DESC;
```

## En pahalı 10 ürün

```sql
SELECT *
FROM products
ORDER BY price DESC
LIMIT 10;
```

## Siparişi olmayan müşterileri bul

```sql
SELECT c.name
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

## CTE ile şehir satışlarını filtrele

```sql
WITH city_sales AS (
    SELECT city, SUM(total_amount) AS sales
    FROM orders
    GROUP BY city
)
SELECT *
FROM city_sales
WHERE sales > 10000;
```

---

# 9. Staj İçin SQL Çalışma Notları

Staj hazırlığında SQL tarafında özellikle şunlara odaklan:

```text
SELECT
WHERE
AND / OR / NOT
GROUP BY
HAVING
COUNT / SUM / AVG
ORDER BY
LIMIT
AS
WITH
JOIN
LEFT JOIN
```

Bir data analytics görevinde SQL genelde şu amaçlarla kullanılır:

```text
Ham veriyi çekmek
Gereksiz satırları filtrelemek
Kategorilere göre özet çıkarmak
Toplam, ortalama, adet gibi metrikler üretmek
Tabloları birleştirmek
Dashboard veya pandas için temiz veri hazırlamak
```

## SQL sorgusu yazarken düşünme sırası

```text
1. Hangi soruyu cevaplıyorum?
2. Hangi tabloya ihtiyacım var?
3. Hangi kolonları görmek istiyorum?
4. Satırları filtrelemem gerekiyor mu?
5. Gruplama gerekiyor mu?
6. Aggregate fonksiyon gerekiyor mu?
7. Sonucu sıralamam gerekiyor mu?
8. Sonuç sayısını sınırlamam gerekiyor mu?
```

## Mini pratik önerisi

Bir satış datası veya world.sql üzerinde şu soruları çöz:

```text
En çok satış yapan kategori hangisi?
En yüksek ciro hangi şehirde?
Her şehirde kaç müşteri var?
Siparişi olmayan müşteriler kimler?
Ortalama sipariş tutarı nedir?
En pahalı 10 ürün hangisi?
Satış toplamı 10000’den yüksek şehirler hangileri?
```

