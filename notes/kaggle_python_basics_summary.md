# Kaggle Learn Python Basics Özeti

Bu dosya Kaggle Learn Python kursundaki 7 ana dersi staj hazırlığı için özetler.  
Amaç: Python temelini, özellikle data analysis ve pandas hazırlığı için tekrar etmek.

## İçindekiler

1. Hello, Python  
2. Functions and Getting Help  
3. Booleans and Conditionals  
4. Lists  
5. Loops and List Comprehensions  
6. Strings and Dictionaries  
7. Working with External Libraries  
8. En Önemli Python Tipleri  
9. Tek Satırlık Faydalı Çözümler
  
---

# 1. Hello, Python

Bu ders Python’un en temel yazım mantığını anlatır: değişkenler, sayılar, aritmetik işlemler, yorum satırları ve `print()`.

Python’da değişken tanımlarken tür belirtmezsin:

```python
x = 10
name = "Can"
price = 99.99
is_active = True
```

Python tipi otomatik anlar:

```python
type(x)
```

## Temel veri tipleri

```python
int       # tam sayı
float     # ondalıklı sayı
str       # metin
bool      # True / False
```

## Aritmetik işlemler

```python
a + b     # toplama
a - b     # çıkarma
a * b     # çarpma
a / b     # normal bölme, sonuç float olur
a // b    # tam sayı bölme
a % b     # kalan
a ** b    # üs alma
```

Örnek:

```python
print(5 / 2)    # 2.5
print(5 // 2)   # 2
print(5 % 2)    # 1
print(2 ** 3)   # 8
```

## Tek satırlık çözümler

```python
average = sum(numbers) / len(numbers)
rounded_value = round(3.14159, 2)
absolute_value = abs(-15)
max_value = max(10, 25, 7)
min_value = min(10, 25, 7)
```

## Tüyo

Python’da işlem önceliği matematikteki gibidir. Önce parantez, sonra üs, sonra çarpma/bölme, sonra toplama/çıkarma.

```python
result = (3 + 2) * 4
```

---

# 2. Functions and Getting Help

Bu ders fonksiyonları, hazır fonksiyonları ve yardım alma yöntemlerini anlatır.

## Fonksiyon tanımlama

```python
def calculate_total(price, quantity):
    return price * quantity
```

Kullanım:

```python
total = calculate_total(100, 3)
print(total)
```

Fonksiyon parametre alabilir ve değer döndürebilir:

```python
def greet(name):
    return "Hello " + name
```

Default parametre:

```python
def greet(name="Guest"):
    return "Hello " + name
```

Docstring:

```python
def calculate_total(price, quantity):
    """Returns total price by multiplying price and quantity."""
    return price * quantity
```

## Yardım alma

```python
help(round)
help(len)
dir("hello")
```

## `print()` vs `return`

`print()` ekrana yazdırır.  
`return` fonksiyonun dışarı değer döndürmesini sağlar.

Yanlış:

```python
def add(a, b):
    print(a + b)

result = add(3, 5)
# result None olur.
```

Doğru:

```python
def add(a, b):
    return a + b

result = add(3, 5)
```

## Tek satırlık çözümler

```python
def square(x): return x ** 2
def is_even(x): return x % 2 == 0
def calculate_total(price, quantity): return price * quantity
def get_discounted_price(price, discount): return price * (1 - discount)
```

---

# 3. Booleans and Conditionals

Bu ders `True`, `False`, karşılaştırmalar ve `if/elif/else` yapılarını anlatır.

## Boolean değerler

```python
True
False
```

## Karşılaştırma operatörleri

```python
x == y    # eşit mi?
x != y    # eşit değil mi?
x > y     # büyük mü?
x < y     # küçük mü?
x >= y    # büyük veya eşit mi?
x <= y    # küçük veya eşit mi?
```

## Mantıksal operatörler

```python
and
or
not
```

Örnek:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Not adult")
```

Birden fazla koşul:

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

`and`:

```python
if age >= 18 and has_id:
    print("Can enter")
```

`or`:

```python
if is_student or is_employee:
    print("Discount available")
```

`not`:

```python
if not is_active:
    print("Account inactive")
```

Python’da bazı değerler otomatik False kabul edilir:

```python
0
0.0
""
[]
{}
None
False
```

## Tek satırlık çözümler

```python
status = "adult" if age >= 18 else "minor"
is_valid = price > 0 and quantity > 0
can_login = username != "" and password != ""
category = "high" if value > 100 else "low"
```

## Tüyo

`=` atama, `==` karşılaştırmadır.

Yanlış:

```python
if x = 5:
    pass
```

Doğru:

```python
if x == 5:
    pass
```

---

# 4. Lists

Liste, birden fazla değeri tek değişkende tutmak için kullanılır.

## Liste oluşturma

```python
numbers = [10, 20, 30, 40]
names = ["Can", "Ali", "Ayşe"]
mixed = [1, "hello", True, 3.14]
```

## Index ile erişim

```python
numbers[0]    # ilk eleman
numbers[1]    # ikinci eleman
numbers[-1]   # son eleman
```

## Slicing

```python
numbers[0:2]
numbers[:3]
numbers[2:]
numbers[-2:]
```

## Liste işlemleri

```python
len(numbers)
numbers.append(50)
numbers.remove(20)
last_item = numbers.pop()
numbers[0] = 99
20 in numbers
```

## Sıralama

```python
sorted_numbers = sorted(numbers)
numbers.sort()
numbers.reverse()
```

`sorted(numbers)` yeni sıralı liste döndürür.  
`numbers.sort()` mevcut listeyi değiştirir.

## Tek satırlık çözümler

```python
total = sum(numbers)
average = sum(numbers) / len(numbers)
highest = max(numbers)
lowest = min(numbers)
first_three = numbers[:3]
last_item = numbers[-1]
contains_value = 10 in numbers
sorted_desc = sorted(numbers, reverse=True)
```

## Data örneği

```python
sales = [100, 250, 300, 150]
total_sales = sum(sales)
average_sales = sum(sales) / len(sales)
```

---

# 5. Loops and List Comprehensions

Bu ders döngüleri ve Python’un kısa liste üretme yöntemini anlatır.

## for döngüsü

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Liste elemanları üzerinde işlem:

```python
for number in numbers:
    print(number * 2)
```

## range()

```python
for i in range(5):
    print(i)
```

Çıktı:

```text
0
1
2
3
4
```

Belirli aralık:

```python
for i in range(1, 6):
    print(i)
```

Adım vererek:

```python
for i in range(0, 10, 2):
    print(i)
```

## while döngüsü

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

## break ve continue

```python
for number in numbers:
    if number == 20:
        break
```

```python
for number in numbers:
    if number == 20:
        continue
    print(number)
```

## List comprehension

```python
squares = [x ** 2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
labels = ["high" if x > 100 else "low" for x in sales]
```

## Tek satırlık çözümler

```python
doubled = [x * 2 for x in numbers]
squares = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
positives = [x for x in numbers if x > 0]
names_upper = [name.upper() for name in names]
long_names = [name for name in names if len(name) > 5]
total_sales = [price * quantity for price, quantity in orders]
```

## Tüyo

List comprehension kısa ve güçlüdür ama çok karmaşık olursa okunabilirliği düşürür. Basit dönüşüm ve filtrelerde kullan, karmaşık işlerde normal `for` döngüsü daha okunur.

---

# 6. Strings and Dictionaries

Bu ders metinleri ve dictionary yapısını anlatır.

## Strings

```python
name = "Can"
message = "Hello Python"
```

Index:

```python
name[0]
name[-1]
```

Uzunluk:

```python
len(name)
```

String metotları:

```python
name.upper()
name.lower()
name.title()
name.strip()
name.replace("a", "A")
```

Metin içinde arama:

```python
"Py" in "Python"
```

String parçalama:

```python
words = "Python is useful".split()
items = "apple,banana,cherry".split(",")
```

Listeyi string’e çevirme:

```python
text = ", ".join(items)
```

f-string:

```python
name = "Can"
age = 22

message = f"My name is {name} and I am {age} years old."
```

## String tek satırlık çözümler

```python
clean_text = text.strip().lower()
words = sentence.split()
csv_line = ",".join(items)
message = f"Total sales: {total_sales} TL"
is_email = "@" in email
first_char = text[0]
last_char = text[-1]
```

## Dictionaries

Dictionary key-value yapısıdır.

```python
student = {
    "name": "Can",
    "department": "Software Engineering",
    "year": 3
}
```

Değere erişim:

```python
student["name"]
student.get("name")
student.get("gpa", "Not available")
```

Yeni değer ekleme:

```python
student["gpa"] = 3.2
```

Değer güncelleme:

```python
student["year"] = 4
```

Key, value ve item erişimi:

```python
student.keys()
student.values()
student.items()
```

Dictionary üzerinde dönmek:

```python
for key, value in student.items():
    print(key, value)
```

## Data örneği

```python
sale = {
    "product": "Laptop",
    "price": 35000,
    "quantity": 2
}

total = sale["price"] * sale["quantity"]
```

Liste içinde dictionary:

```python
sales = [
    {"product": "Laptop", "price": 35000, "quantity": 2},
    {"product": "Mouse", "price": 750, "quantity": 5},
]
```

## Dictionary tek satırlık çözümler

```python
name = student.get("name", "Unknown")
keys = list(student.keys())
values = list(student.values())
most_expensive = max(products, key=products.get)
total_price = sale["price"] * sale["quantity"]
filtered = [item for item in sales if item["quantity"] > 1]
```

## Tüyo

`student["gpa"]` olmayan key için hata verir.  
`student.get("gpa")` daha güvenlidir.

---

# 7. Working with External Libraries

Bu ders Python’da dış kütüphaneleri kullanmayı anlatır.

## Import

```python
import math
math.sqrt(16)
```

Alias ile import:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Belirli fonksiyonu import etmek:

```python
from math import sqrt
sqrt(16)
```

Yardım:

```python
dir(math)
help(math.sqrt)
```

## Sık kullanılan kütüphaneler

```python
math        # matematik fonksiyonları
random      # rastgele değerler
datetime    # tarih/saat
pandas      # veri analizi
numpy       # sayısal işlemler
matplotlib  # grafik çizme
```

`math` örnekleri:

```python
import math

math.sqrt(25)
math.ceil(3.2)
math.floor(3.8)
math.pi
```

`random` örnekleri:

```python
import random

random.randint(1, 10)
random.choice(["A", "B", "C"])
```

`datetime` örneği:

```python
from datetime import datetime

today = datetime.now()
```

## Tek satırlık çözümler

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
random_item = random.choice(items)
today = datetime.now()
df = pd.read_csv("data.csv")
```

## Tüyo

Data analysis tarafında standart alias’lar:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Bunları ezberle. Notebooklarda ve iş ortamında sürekli göreceksin.

---

# 8. En Önemli Python Tipleri

```python
age = 22                         # int
price = 99.99                    # float
name = "Can"                     # str
is_active = True                 # bool
numbers = [1, 2, 3]              # list
student = {"name": "Can"}        # dict
result = None                    # NoneType
```

---

# 9. En Çok İşine Yarayacak Tek Satırlık Çözümler

```python
average = sum(numbers) / len(numbers)
max_value = max(numbers)
min_value = min(numbers)
sorted_numbers = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)
evens = [x for x in numbers if x % 2 == 0]
squares = [x ** 2 for x in numbers]
clean_names = [name.strip().title() for name in names]
total_sales = [sale["price"] * sale["quantity"] for sale in sales]
expensive_sales = [sale for sale in sales if sale["price"] > 1000]
most_expensive_product = max(products, key=products.get)
safe_value = data.get("key", "default")
message = f"{product}: {price * quantity} TL"
words = sentence.split()
csv_line = ",".join(items)
is_valid = price > 0 and quantity > 0
label = "high" if value > 100 else "low"
```
