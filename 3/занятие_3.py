# -*- coding: utf-8 -*-
"""Занятие 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k--gv-fe3wMO2G0buTruoW7--3G8Fdei

Итак, перед тем, как браться за статистику, нужно:

**1. Прочесть исходный файл и превратить его в структуру данных**

К заданию прилагается файл в формате csv, где все значения разделены запятыми. Это наши исходные данные. Чтобы применить к ним все возможности языка Python и библиотеки Pandas, надо импортировать эту библиотеку и сохранить её в переменной. По сокращённому названию панельных данных (panel data), с которых начиналась Pandas, эту переменную принято называть pd:
 
**import pandas as pd**

Для чтения csv-файла в библиотеке Pandas есть готовая функция — метод **read_csv()**. Как и все методы, он вызывается записью через точку после имени своего объекта. В скобках указывается аргумент (параметр) метода. У read_csv() это имя файла с данными. Прочтение превращает файл в структуру данных DataFrame. Имя переменной, в которой эта структура данных сохраняется, чаще всего df либо отражает тематику данных:

**df = pd.read_csv('music_log.csv')**

**2. Посмотреть на данные**

Вывести на экран таблицу и оценить данные:

print(df) 
Как правило, таблица очень велика. Практичнее запросить определённое количество первых строк, методом head().

**3. Оценить качество предподготовки**

Нужно убедиться в том, что данные прошли предподготовку. По крайней мере, не должно быть пропусков и повторов. Пропущенные и неопределённые значения выявляет метод **isna()**, а суммарное количество таких значений — метод **sum()**.

**print(df.isna().sum())**


Повторяющиеся строки — дубликаты — выявляются методом **duplicated()** и подсчитываются тем же sum():

**print(df.duplicated().sum())**
Если возвращаются нули, всё хорошо — данные пригодны для исследования.

## Задача

1. Загрузите таблицу **exoplanet_catalog**, содержащую данные о планетах за пределами Солнечной системы, или экзопланетах. Сформируйте из данной таблицы новый датасет под назанием **exoplanet**, коорая будет содердать стоблцы name, mass, radius, discovered. Проверьте, чтобы название всех столбцов было корректным, при необходмости измените названия.

2. Удалите из получившейся таблица строки с нулевыми значениями.

3. Убедитесь, что таблица не содержит ни пропущенных значений, ни дубликатов.
"""

#Загрузите таблицу exoplanet_catalog, содержащую данные о планетах за пределами Солнечной системы, или экзопланетах. 
#Сформируйте из данной таблицы новый датасет под назанием exoplanet, коорая будет содердать стоблцы name, mass, radius, discovered. 
#Проверьте, чтобы название всех столбцов было корректным, при необходмости измените названия.
import pandas as pd
df = pd.read_csv('exoplanet_catalog.csv')
exoplanet = pd.DataFrame({'name': df['# name'], 'mass': df['mass'], 'radius': df['radius'], 'discovered': df['discovered'], })
print(exoplanet.head(10))

#Удалите из получившейся таблица строки с нулевыми значениями.
exoplanet.dropna(inplace=True)
print(exoplanet)
print(exoplanet.isnull().sum())

#Убедитесь, что таблица не содержит ни пропущенных значений, ни дубликатов.
print(exoplanet.isna().sum())
print(exoplanet.duplicated().sum())

"""# Группировка данных

Слово «анализ» означает разбор, рассмотрение с разных сторон. Анализ данных начинают с разделения их на группы по какому-нибудь признаку. Эта операция называется группировка данных. Она помогает изучить материал более подробно, чтобы затем перейти к поиску взаимосвязей между отдельными группами.


Группировка оправданна, если данные чётко делятся по значимому признаку, а полученные группы близки к теме задачи. Например, когда есть данные обо всех покупках в супермаркете, можно смело заниматься группировкой. Так можно установить время наплыва покупателей и решить проблему пиковых нагрузок. Или посчитать средний чек — обычно для магазинов это ключевая метрика.


Стадии группировки хорошо укладываются в словесную формулу **split-apply-combine**:

•	разделить, **split** — разбиение на группы по определённому критерию;

•	применить, **apply** — применение какого-либо метода к каждой группе в отдельности, например, подсчёт численности группы методом count() или суммирование вызовом sum();

•	объединить, **combine** — сведение результатов в новую структуру данных, в зависимости от условий разделения и выполнения метода это бывает DataFrame и Series.

В библиотеке Pandas есть отличные инструменты группировки. Рассмотрим обращение с ними на примере анализа данных о планетах за пределами Солнечной системы, или экзопланетах. Орбитальные обсерватории засекли уже тысячи таких небесных тел. Их выявляют на снимках космических телескопов наши коллеги, аналитики данных. Поищем среди экзопланет похожие на Землю. Возможно, это наши будущие колонии, или там уже обитают разумные существа, с которыми однажды предстоит установить контакт.

DataFrame с данными по нескольким тысячам экзопланет сохранён в переменной **exoplanet**. Посмотрим на первые 30 строк таблицы:

"""

exoplanet.head(30)

"""**Документация**

Столбцы:

•	name: название экзопланеты;

•	mass: масса в массах планеты Юпитер;

•	radius: радиус, пересчитанный в радиусах Земли;

•	discovered: год открытия экзопланеты.

*Источник: каталог экзопланет на портале exoplanet.eu*

На картинке изображен принцип **split-apply-combine** для таблицы с экзопланетами. Посмотрим, как вообще идут дела с поиском экзопланет. Сначала данные делят по группам, где каждая группа — это год. Потом метод **count()** подсчитывает численность каждой группы. В итоге получаем новую структуру данных с группами, где каждая содержит год и число открытых за этот год экзопланет.

![image.png](attachment:image.png)

В Рandas для группировки данных есть метод **groupby()**. Он принимает как аргумент название столбца, по которому нужно группировать. В случае с делением экзопланет по годам открытия:

**print(exoplanet.groupby('discovered'))**

**<pandas.core.groupby.DataFrameGroupBy object at 0x7fc1e1ca3400>**


Применение метода **groupby()** к объекту типа DataFrame приводит к созданию объекта особого типа — **DataFrameGroupBy**. Это сгруппированные данные. Если применить к ним какой-нибудь метод Pandas, они станут новой структурой данных типа **DataFrame** или **Series**.
Подсчитаем сгруппированные по годам экзопланеты методом **count()**:
"""

print(exoplanet.groupby('discovered').count())

"""Если нужно сравнить наблюдения по одному показателю, метод применяют к **DataFrameGroupBy** с указанием на один столбец. Нас в первую очередь интересует радиус экзопланет: мы ищем другую Землю. Давайте получим таблицу с единственным столбцом 'radius':

**exo_number = exoplanet.groupby('discovered')['radius'].count()**

**print(exo_number)** 
"""

exo_number = exoplanet.groupby('discovered')['radius'].count()
print(exo_number)

"""Получили Series, где по годам открытия расписано количество экзопланет, для которых удалось установить радиус.

Посмотрим, как меняется средний радиус открытых экзопланет год от года. Для этого надо сложить радиусы планет, открытых за определённый год, и поделить на их количество (которое мы уже нашли).

Сумма радиусов считается методом **sum()**:

**exo_radius_sum = exoplanet.groupby('discovered')['radius'].sum()**


**print(exo_radius_sum)**


"""

exo_radius_sum = exoplanet.groupby('discovered')['radius'].sum()
print(exo_radius_sum)

"""Очень кстати, что объекты Series можно делить друг на друга. Это позволит нам разделить перечень сумм радиусов на перечень количеств экзопланет без перебора в цикле:


**exo_radius_mean = exo_radius_sum/exo_number**

**print(exo_radius_mean)**

"""

exo_radius_mean = exo_radius_sum/exo_number
print(exo_radius_mean)

"""Точность наших приборов растёт, и новые экзопланеты по размерам всё ближе к Земле. 

А теперь вернемся к анализу датафрейма с музыкльными предпочтениями слушателей Яндекс.Музыки. Идею объединения сервисов Музыка и Радио тестировали на небольшой группе пользователей. Результаты сведены в csv-файл, который вам предстоит изучить. Итог анализа таких данных — это метрики: величины, значения которых отражают пользовательские впечатления. Одна из важнейших — **happiness**. Здесь это среднее время, которое пользователь слушает музыку в течение выбранного периода времени (в нашей задаче — за сутки). Чем дольше пользователь слушает музыку, тем он довольнее. Ваша задача: найти значение happiness и посмотреть, как оно менялось.

Тем же методом **groupby()**, которым мы ищем новую Землю, можно поискать и необыкновенного человека в данных Яндекс.Музыки. Тем более, что без этого не выполнить поставленной менеджером задачи.

Прежде, чем рассчитывать метрику happiness, нужно изучить пользователей, чьё «счастье» мы собираемся оценить. Какие они, эти люди, которые слушают действительно много музыки? Есть ли у них особые предпочтения, или они потребляют всё подряд?

## Задача

1. Меломаны у нас есть. Сейчас узнаем идентификатор **user_id** одного из них. Для этого сгруппируем данные по каждому пользователю, чтобы собрать жанры прослушанных им композиций.

Сгруппируйте DataFrame по столбцу user_id, сохраните полученный результат в переменной genre_grouping.

Посчитайте количество жанров, которые выбрали пользователи, методом count(), указав, что выбираем один столбец genre_name.

Сохраните результат в переменной genre_counting и выведите первые 30 строк этой таблицы.

2. Быть может, те, кто за день слушает больше 50 песен, имеют более широкие предпочтения. Чтобы найти такого, изготовим универсальный инструмент.

Напишите функцию user_genres, которая принимает некую группировку как свой аргумент group. Функция должна перебирать группы, входящие в эту группировку.

В каждой группе два элемента — имя группы с индексом 0 и список значений с индексом 1.

Обнаружив такую группу, в которой список (элемент с индексом 1) содержит более 50 значений, функция возвращает имя группы (значение элемента с индексом 0).

3. Вызовите функцию **user_genres**, как аргумент передайте ей **genre_grouping**. Результат – **user_id** неведомого нам любителя музыки – сохраните в переменной **search_id** и выведите значение на экран.
"""

#Меломаны у нас есть. Сейчас узнаем идентификатор user_id одного из них. 
#Для этого сгруппируем данные по каждому пользователю, чтобы собрать жанры прослушанных им композиций.
#Сгруппируйте DataFrame по столбцу user_id, сохраните полученный результат в переменной genre_grouping.
#Посчитайте количество жанров, которые выбрали пользователи, методом count(), указав, что выбираем один столбец genre_name.
#Сохраните результат в переменной genre_counting и выведите первые 30 строк этой таблицы.

import pandas as pd
yandex_music = pd.read_csv('yandex_music.csv')
new_names = ['user_id', 'track_name', 'artist_name', 'genre_name', 'city', 'total_play_seconds', 'day']
yandex_music.set_axis(new_names, axis = 'columns', inplace = True)
genre_grouping = yandex_music.groupby('user_id')
genre_counting = genre_grouping['genre_name'].count()
print(genre_counting.head(30))

#Быть может, те, кто за день слушает больше 50 песен, имеют более широкие предпочтения. 
#Чтобы найти такого, изготовим универсальный инструмент.
#Напишите функцию user_genres, которая принимает некую группировку как свой аргумент group. 
#Функция должна перебирать группы, входящие в эту группировку.
#В каждой группе два элемента — имя группы с индексом 0 и список значений с индексом 1.
#Обнаружив такую группу, в которой список (элемент с индексом 1) содержит более 50 значений, функция возвращает имя группы (значение элемента с индексом 0).
def user_genres(group):
    for column in group:
        if len(column[1]) > 50:
            return column[0]

#Вызовите функцию user_genres, как аргумент передайте ей genre_grouping. 
#Результат – user_id неведомого нам любителя музыки – сохраните в переменной search_id и выведите значение на экран.
search_id = user_genres(genre_grouping)
print(search_id)

"""# Сортировка данных

Поиск необычного в группе — что среди планет, что среди меломанов — это прежде всего поиск чемпионов: объектов с выдающимися показателями по разным статьям. Как всю таблицу, так и отдельные группы изучают, сортируя строки по какому-либо столбцу. 

В Pandas для этой операции есть метод **sort_values()**. У него два аргумента:

• **by = 'имя столбца'** — имя столбца, по которому нужно сортировать;

• **ascending:** по умолчанию True. Для сортировки по убыванию установите значение False.

![image.png](attachment:image.png)


Среди экзопланет интересны близкие по размерам к Земле. Есть ли такие? Отсортируем список по радиусу в порядке возрастания. Тогда в голове таблицы окажутся самые малые, на которых гравитация не прижмёт нас к полу.

**print(exoplanet.sort_values(by='radius').head(30))**
"""

print(exoplanet.sort_values(by='radius').head(30))

"""Оказывается, некоторые из уже открытых экзопланет по размерам близки не то что к Земле, но уже и к Луне! Получим список экзопланет с радиусом меньше земного. Смотрите, как логический оператор (здесь это <) задействуется в отборе элементов столбца. Дальше нам этот приём не раз понадобится.


**print(exoplanet[exoplanet['radius'] < 1])**
"""

print(exoplanet[exoplanet['radius'] < 1])

"""Но и этот список такой длинный, что изучать его лучше по частям. Экзопланеты, близкие по размерам к Земле, за последнее десятилетие открывали нередко. Можно изучать список открытых за каждый год. Например, для 2014 года (вновь обратите внимание на работу логического оператора, теперь это ==):

**print(exoplanet[exoplanet['discovered'] == 2014])**

"""

print(exoplanet[exoplanet['discovered'] == 2014])

"""А чтобы не тратить время на лишнее, поставим оба условия сразу. Для этого в Pandas есть логический оператор &, подобный оператору and языка Python. Напомним, его смысл на русском языке можно передать словами «и ещё»:

**# экзопланеты меньше Земли __ и ещё __ открытые в 2014 году**

**exo_small_14 = exoplanet[ (exoplanet['radius']<1) & (exoplanet['discovered']==2014)]**

**print(exo_small_14)**


"""

exo_small_14 = exoplanet[ (exoplanet['radius']<1) & (exoplanet['discovered']==2014)]
print(exo_small_14)

"""Отсортируем результат в порядке убывания радиуса.

**print(exo_small_14.sort_values(by = 'radius', ascending = False))**

"""

print(exo_small_14.sort_values(by = 'radius', ascending = False))

"""Самая крупная планета, Kepler 106 d – почти как Земля, вращается вокруг звезды Kepler 106 в созвездии Лебедя. Эта звезда очень похожа на наше Солнце. Правда, до неё 1435 световых лет — далековато. Но, возможно, учёные что-нибудь придумают. А мы пока применим эту технологию к нашему бизнесу, в «приземлённой» задаче.
## Задача

1. Космический телескоп Kepler открыл похожую на Землю планету у похожей на Солнце звезды. А вы в данных Яндекс.Музыки обнаружили меломана с уникальными данными. Он за день послушал больше 50 композиций.
Получите таблицу с прослушанными им треками.

Для этого запросите из структуры данных df строки, отвечающие сразу двум условиям:

1) значение в столбце 'user_id' должно быть равно значению переменной search_id;

2) время прослушивания, т.е. значение в столбце 'total_play_seconds', не должно равняться 0.

Сохраните результат в переменной music_user.

2. Теперь узнаем, сколько времени он слушал музыку каждого жанра.

Сгруппируйте данные таблицы music_user по столбцу 'genre_name' и получите сумму значений столбца 'total_play_seconds'. Сохраните результат в переменной sum_music_user и выведите её значение на экран.

3. Кажется, предпочтения нашего меломана начинают проявляться. Но, возможно, длительность композиций от жанра к жанру сильно различается. Важно знать, сколько треков каждого жанра он включил.

Сгруппируйте данные по столбцу genre_name и посчитайте, сколько значений в столбце genre_name. Сохраните результат в переменной count_music_user и выведите её значение на экран.

4. Чтобы предпочтения были видны сразу, нужно крупнейшие значения расположить наверху. Отсортируйте данные в группировке sum_music_user по убыванию. Внимание: когда применяете метод sort_values() к Series с единственным столбцом, аргумент by указывать не нужно, только порядок сортировки.

Сохраните результат в переменной final_sum и выведите её значение на экран.

5. Теперь то же самое надо сделать с числом прослушанных меломаном композиций. Отсортируйте данные группировки count_music_user по убыванию. Сохраните результат в переменной final_count, значение которой выведите на экран.

"""

#1. Космический телескоп Kepler открыл похожую на Землю планету у похожей на Солнце звезды. 
#А вы в данных Яндекс.Музыки обнаружили меломана с уникальными данными. Он за день послушал больше 50 композиций. Получите таблицу с прослушанными им треками.
#Для этого запросите из структуры данных df строки, отвечающие сразу двум условиям:
#1) значение в столбце 'user_id' должно быть равно значению переменной search_id;
#2) время прослушивания, т.е. значение в столбце 'total_play_seconds', не должно равняться 0.
#Сохраните результат в переменной music_user.
music_user = yandex_music[(yandex_music['user_id'] == search_id) & (yandex_music['total_play_seconds'] != '00:00:00')]
print(music_user)

#2. Теперь узнаем, сколько времени он слушал музыку каждого жанра.
#Сгруппируйте данные таблицы music_user по столбцу 'genre_name' и получите сумму значений столбца 'total_play_seconds'. 
#Сохраните результат в переменной sum_music_user и выведите её значение на экран.
sum_music_user = music_user.groupby("genre_name")['total_play_seconds'].sum()
print(sum_music_user)

#3. Кажется, предпочтения нашего меломана начинают проявляться. Но, возможно, длительность композиций от жанра к жанру сильно различается. 
#Важно знать, сколько треков каждого жанра он включил.
#Сгруппируйте данные по столбцу genre_name и посчитайте, сколько значений в столбце genre_name. 
#Сохраните результат в переменной count_music_user и выведите её значение на экран.
count_music_user = music_user.groupby("genre_name")['genre_name'].count()
print(count_music_user)

#4. Чтобы предпочтения были видны сразу, нужно крупнейшие значения расположить наверху. Отсортируйте данные в группировке sum_music_user по убыванию. 
#Внимание: когда применяете метод sort_values() к Series с единственным столбцом, аргумент by указывать не нужно, только порядок сортировки.
#Сохраните результат в переменной final_sum и выведите её значение на экран.
final_sum = sum_music_user.sort_values(ascending=False)
print(final_sum)

#5. Теперь то же самое надо сделать с числом прослушанных меломаном композиций. 
#Отсортируйте данные группировки count_music_user по убыванию. Сохраните результат в переменной final_count, значение которой выведите на экран.
final_count = count_music_user.sort_values(ascending=False)
print(final_count)