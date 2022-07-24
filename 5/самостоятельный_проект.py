# -*- coding: utf-8 -*-
"""Самостоятельный проект.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ayxNm4fVqi1mRt_jE07Lt-z0_FnW9oMN

# Добро пожаловать в самостоятельный проект

Самостоятельный проект — это практическая проверка знаний, приобретённых вами на вводном курсе. Каждый раздел посвящён отдельной стадии анализа данных с экскурсом в основы Python. 

Проект выполняется в пять этапов:

•	Постановка задачи

•	Получение данных

•	Предобработка данных

•	Анализ данных

•	Оформление результатов

Для каждой части описаны шаги выполнения c теоретическим приложением. В Jupyter Notebook эти шаги связаны между собой выводами и результатами.

**Исследование: Музыка больших городов**

Яндекс.Музыка — это крупный продукт с огромным запасом данных для исследований. Команды таких сервисов для поддержания интереса к продукту и привлечения новых пользователей часто проводят исследования про пользователей. Чтобы удержать клиентов и привлечь новых, сделать бренд более узнаваемым, команда сервиса проводит исследования аудитории, и публикует интересные результаты. Например, интересно сравнить тексты, сочинённые нейросетью, с произведениями настоящих рэперов.
Есть исследование, которое напоминает наше: о музыкальных предпочтениях в разных городах России.
Итак, вопрос вам: как музыка, которая звучит по дороге на работу в понедельник утром, отличается от той, что играет в среду или в конце рабочей недели? Возьмите данные для Москвы и Петербурга. Сравните, что и в каком режиме слушают их жители.

План исследования

1.	Получение данных. Прочитайте данные, ознакомьтесь с ними.

2.	Предобработка данных. Избавьтесь от дубликатов, проблем с названиями столбцов и пропусками.

3.	Анализ данных. Ответьте на основные вопросы исследования, подготовьте отчётную таблицу или опишите полученный результат.

4.	Подведение итогов. Просмотрите выполненную работу и сформулируйте выводы.

# Этап 1. Получение данных

Изучим данные, предоставленные сервисом для проекта.

Прочитайте файл music_project.csv и сохраните его в переменной df.

Получите  первых 10 строк таблицы, а также общую информацию о данных таблицы df.
"""

import pandas as pd
# <чтение файла с данными с сохранением в df>
df = pd.read_csv('yandex_music.csv')
# <получение первых 10 строк таблицы df>
df.head(10)

# <получение общей информации о данных в таблице df>
df.info()

"""Рассмотрим полученную информацию подробнее.
Всего в таблице 7 столбцов, тип данных у каждого столбца - строка.
Подробно разберём, какие в df столбцы и какую информацию они содержат:
•	userID — идентификатор пользователя;
•	Track — название трека;
•	artist — имя исполнителя;
•	genre — название жанра;
•	City — город, в котором происходило прослушивание;
•	time — время, в которое пользователь слушал трек;
•	Day — день недели.
Количество значений в столбцах различается. Это говорит о том, что в данных есть пропущенные значения.

## Выводы: 

Каждая строка таблицы содержит информацию о композициях определённого жанра в определённом исполнении, которые пользователи слушали в одном из городов в определённое время и день недели. Две проблемы, которые нужно решать: пропуски и некачественные названия столбцов. Для проверки рабочих гипотез особенно ценны столбцы 'City', 'time', 'Day'. Данные из столбца 'genre'  позволят узнать самые популярные жанры.

# Этап 2. Предобработка данных

Исключим пропуски, переименуем столбцы, а также проверим данные на наличие дубликатов.

Получаем перечень названий столбцов. Какая наблюдается проблема — кроме тех, что уже были названы ранее?
"""

# <перечень названий столбцов таблицы df>
df.columns

"""В названиях столбцов есть пробелы, которые могут затруднять доступ к данным.

Переименуем столбцы для удобства дальнейшей работы. Проверим результат.

"""

# <переименование столбцов>
new_names = ['user_id', 'track_name', 'artist_name', 'genre_name', 'city', 'time', 'weekday']
df.set_axis(new_names, axis = 'columns', inplace = True)
# <проверка результатов - перечень названий столбцов>
df.columns

"""Проверим данные на наличие пропусков вызовом набора методов для суммирования пропущенных значений."""

# <суммарное количество пропусков, выявленных методом isnull() в таблице df>
df.isnull().sum()

"""Пустые значения свидетельствуют, что для некоторых треков доступна не вся информация. Причины могут быть разные: скажем, не назван конкретный исполнитель народной песни. Хуже, если проблемы с записью данных. Каждый отдельный случай необходимо разобрать и выявить причину.

Заменяем пропущенные значения в столбцах с названием трека и исполнителя на строку 'unknown'. После этой операции нужно убедиться, что таблица больше не содержит пропусков.

"""

# <замена пропущенных значений в столбце 'track_name' на строку 'unknown' специальным методом замены>
df['track_name'] = df['track_name'].fillna('unknown')
# <замена пропущенных значений в столбце 'artist_name' на строку 'unknown' специальным методом замены>
df['artist_name'] = df['artist_name'].fillna('unknown')

# <проверка: вычисление суммарного количества пропусков, выявленных в таблице df>
df.isnull().sum()

"""Удаляем в столбце с жанрами пустые значения; убеждаемся, что их больше не осталось."""

# <удаление пропущенных значений в столбце 'genre_name'>
df.dropna(subset=['genre_name'],inplace=True)
# <проверка>
df.isnull().sum()

"""Необходимо установить наличие дубликатов. Если найдутся, удаляем, и проверяем, все ли удалились."""

# <получение суммарного количества дубликатов в таблице df>
df.duplicated().sum()

# <удаление всех дубликатов из таблицы df специальным методом>
df = df.drop_duplicates().reset_index(drop = True)
# <проверка на отсутствие>
df.duplicated().sum()

"""Дубликаты могли появиться вследствие сбоя в записи данных. Стоит обратить внимание и разобраться с причинами появления такого «информационного мусора».

Сохраняем список уникальных значений столбца с жанрами в переменной genres_list.

Объявим функцию find_genre() для поиска неявных дубликатов в столбце с жанрами. Например, когда название одного и того же жанра написано разными словами.

"""

# <сохранение в переменной genres_list списка уникальных значений, 
# выявленных специальным методом в столбце 'genre_name'>
genres_list = df['genre_name'].unique()

# <создание функции find_genre()>
# функция принимает как параметр строку с названием искомого жанра
# в теле объявляется переменная-счётчик, ей присваивается значение 0,
# затем цикл for проходит по списку уникальных значений
# если очередной элемент списка равен параметру функции, 
# то значение счётчика увеличивается на 1
# по окончании работы цикла функция возвращает значение счётчика
def find_genre(genreName):
  count = 0
  for elem in genres_list:
    if elem == genreName:
      count += 1
  return count

"""Вызов функции find_genre() для поиска различных вариантов названия жанра хип-хоп в таблице.

Правильное название — hiphop. Поищем другие варианты:

•	hip

•	hop

•	hip-hop

"""

# <вызовом функции find_genre() проверяется наличие варианта 'hip'>
find_genre('hip')

# <проверяется наличие варианта 'hop'>
find_genre('hop')

# <проверяется наличие варианта 'hip-hop'>
find_genre('hip-hop')

"""Объявим функцию find_hip_hop(), которая заменяет неправильное название этого жанра в столбце 'genre_name' на 'hiphop' и проверяет успешность выполнения замены.

Так исправляем все варианты написания, которые выявила проверка.

"""

# <создание функции find_hip_hop()>
# функция принимает как параметры таблицу df и неверное название
# к столбцу 'genre_name' применяется специальный метод, 
# который заменяет второй параметр на строку 'hiphop'
# результат работы равен подсчитанному методом count() числу
#значений столбца, 
# которые равны второму параметру
# функция возвращает результат
def find_hip_hop(df, name):
  df['genre_name'] = df['genre_name'].replace(name, 'hiphop')
  count = df.loc[ df.loc[:,'genre_name'] == 'wrong' ]['genre_name'].count()
  return count

# <замена одного неверного варианта на hiphop вызовом функции find_hip_hop()>
find_hip_hop(df, 'hip-hop')

"""Получаем общую информацию о данных. Убеждаемся, что чистка выполнена успешно."""

# <получение общей информации о данных таблицы df>
df.info()

"""## Вывод

На этапе предобработки в данных обнаружились не только пропуски и проблемы с названиями столбцов, но и всяческие виды дубликатов. Их удаление позволит провести анализ точнее. Поскольку сведения о жанрах важно сохранить для анализа, не просто удаляем все пропущенные значения, но заполним пропущенные имена исполнителей и названия треков. Имена столбцов теперь корректны и удобны для дальнейшей работы.

# Действительно ли музыку в разных городах слушают по-разному?

Была выдвинута гипотеза, что в Москве и Санкт-Петербурге пользователи слушают музыку по-разному. Проверяем это предположение по данным о трёх днях недели — понедельнике, среде и пятнице.

Для каждого города устанавливаем количество прослушанных в эти дни композиций с известным жанром, и сравниваем результаты.
Группируем данные по городу и вызовом метода count() подсчитываем композиции, для которых известен жанр.
"""

# <группировка данных таблицы df по столбцу 'city' и подсчёт количества значений столбца 'genre_name'>
df.groupby('city')['genre_name'].count()

"""В Moscow прослушиваний больше, чем в Saint-Petersburg, но это не значит, что Moscow более активна. У Яндекс.Музыки в целом больше пользователей в Москве, поэтому величины сопоставимы.
Сгруппируем данные по дню недели и подсчитаем прослушанные в понедельник, среду и пятницу композиции, для которых известен жанр.

"""

# <группировка данных по столбцу 'weekday' и подсчёт количества значений столбца 'genre_name'>
df.groupby('weekday')['genre_name'].count()

"""Понедельник и пятница — время для музыки; по средам пользователи немного больше вовлечены в работу.

Создаём функцию number_tracks(), которая принимает как параметры таблицу, день недели и название города, а возвращает количество прослушанных композиций, для которых известен жанр. Проверяем количество прослушанных композиций для каждого города и понедельника, затем среды и пятницы.

"""

# <создание функции number_tracks()>
# объявляется функция с тремя параметрами: df, day, city
# в переменной track_list сохраняются те строки таблицы df, для которых 
# значение в столбце 'weekday' равно параметру day
# и одновременно значение в столбце 'city' равно параметру city
# в переменной track_list_count сохраняется число значений столбца 'genre_name',
# рассчитанное методом count() для таблицы track_list
# функция возвращает значение track_list_count
def number_tracks(df, day, city):
  track_list = df[(df['weekday'] == day) & (df['city'] == city)]
  track_list_count = track_list['genre_name'].count()
  return track_list_count

# <список композиций для Москвы в понедельник>
number_tracks(df, 'Monday', 'Moscow')

# <список композиций для Санкт-Петербурга в понедельник>
number_tracks(df, 'Monday', 'Saint-Petersburg')

# <список композиций для Москвы в среду>
number_tracks(df, 'Wednesday', 'Moscow')

# <список композиций для Санкт-Петербурга в среду>
number_tracks(df, 'Wednesday', 'Saint-Petersburg')

# <список композиций для Москвы в пятницу>
number_tracks(df, 'Friday', 'Moscow')

# <список композиций для Санкт-Петербурга в пятницу>
number_tracks(df, 'Friday', 'Saint-Petersburg')

"""Сведём полученную информацию в одну таблицу, где ['city', 'monday', 'wednesday', 'friday'] названия столбцов."""

# <таблица с полученными данными>
data = [
        ['Moscow', number_tracks(df, 'Monday', 'Moscow'), number_tracks(df, 'Wednesday', 'Moscow'), number_tracks(df, 'Friday', 'Moscow')],
        ['Saint-Petersburg', number_tracks(df, 'Monday', 'Saint-Petersburg'), number_tracks(df, 'Wednesday', 'Saint-Petersburg'), number_tracks(df, 'Friday', 'Saint-Petersburg')]
        ]
columns = ['city','monday','wednesday','friday']
table = pd.DataFrame(data = data, columns = columns)
print(table)

"""## Вывод

Проанализировав данные можно с увереностью сказать, что гипотиза (которую выдвигали ранее) подтвердилась. В Москве пик слушателей приходятся на понедельник и пятницу, а Санкт-Петербурге наблюдается пик слушателей в среду. Отсюда можно сделать вывод, что в Москве и Санкт-Петербурге пользователи слушают музыку по-разному.

# Утро понедельника и вечер пятницы — разная музыка или одна и та же?

Ищем ответ на вопрос, какие жанры преобладают в разных городах в понедельник утром и в пятницу вечером. Есть предположение, что в понедельник утром пользователи слушают больше бодрящей музыки (например, жанра поп), а вечером пятницы — больше танцевальных (например, электронику).
Получим таблицы данных по Москве moscow_general и по Санкт-Петербургу spb_general.
"""

# получение таблицы moscow_general из тех строк таблицы df, 
# для которых значение в столбце 'city' равно 'Moscow'
moscow_general = df[df['city'] == 'Moscow']
# <получение таблицы spb_general>
spb_general = df[df['city']=='Saint-Petersburg']

"""Создаём функцию genre_weekday(), которая возвращает список жанров по запрошенному дню недели и времени суток с такого-то часа по такой-то."""

# объявление функции genre_weekday() с параметрами df, day, time1, time2
# в переменной genre_list сохраняются те строки df, для которых одновременно:
# 1) значение в столбце 'weekday' равно параметру day,
# 2) значение в столбце 'time' больше time1 и
# 3) меньше time2.
# в переменной genre_list_sorted сохраняются в порядке убывания  
# первые 10 значений Series, полученной подсчётом числа значений 'genre_name'
# сгруппированной по столбцу 'genre_name' таблицы genre_list
# функция возвращает значение genre_list_sorted
def genre_weekday(df, day, time1, time2):
  genre_list = df[(df['weekday'] == day) & (df['time'] > time1) & (df['time'] < time2)]
  genre_list_sorted = genre_list.groupby('genre_name')['genre_name'].count().sort_values(ascending = False).head(10)
  return genre_list_sorted

"""Cравниваем полученные результаты по таблице для Москвы и Санкт-Петербурга в понедельник утром (с 7 до 11) и в пятницу вечером (с 17 до 23)."""

# <вызов функции для утра понедельника в Москве (вместо df таблица moscow_general)>
genre_weekday(moscow_general, 'Monday', '07:00:00', '11:00:00')

# <вызов функции для утра понедельника в Петербурге (вместо df таблица spb_general)>
genre_weekday(spb_general, 'Monday', '07:00:00', '11:00:00')

# <вызов функции для вечера пятницы в Москве>
genre_weekday(moscow_general, 'Friday', '17:00:00', '23:00:00')

# <вызов функции для вечера пятницы в Питере>
genre_weekday(spb_general, 'Friday', '17:00:00', '23:00:00')

"""Популярные жанры в понедельник утром в Питере и Москве оказались похожи: везде, как и предполагалось, популярен pop. Несмотря на это, концовка топ-10 для двух городов различается: в Питере в топ-10 входит джаз и русский рэп, а в Москве жанр world.

В конце недели pop музыка остается популярной в Москве, в Санкт-Петербурге лидером становиться electronic. ТОП-10 в конце недели отличается не только в разных городах, но и с началом текущей недели.

## Вывод
Жанр pop безусловный лидер, а топ-5 в целом не различается в обеих столицах. При этом видно, что концовка списка более «живая»: для каждого города выделяются более характерные жанры, которые действительно меняют свои позиции в зависимости от дня недели и времени.

# Москва и Питер — две разные столицы, два разных направления в музыке. Правда?

Гипотеза: Питер богат своей рэп-культурой, поэтому это направление там слушают чаще, а Москва — город контрастов, но основная масса пользователей слушает попсу.

Сгруппируем таблицу moscow_general по жанру, сосчитаем численность композиций каждого жанра методом count(), отсортируем в порядке убывания и сохраним результат в таблице moscow_genres.

Просмотрим первые 10 строк этой новой таблицы.
"""

# одной строкой: группировка таблицы moscow_general по столбцу 'genre_name', 
# подсчёт числа значений 'genre_name' в этой группировке методом count(), 
# сортировка Series в порядке убывания и сохранение в moscow_genres 
moscow_genres = moscow_general.groupby('genre_name')['genre_name'].count().sort_values(ascending = False)

# <просмотр первых 10 строк moscow_genres>
moscow_genres.head(10)

"""Сгруппируем таблицу spb_general по жанру, сосчитаем численность композиций каждого жанра методом count(), отсортируем в порядке убывания и сохраним результат в таблице spb_genres.

Просматриваем первые 10 строк этой таблицы. Теперь можно сравнивать два города.

"""

# <группировка таблицы spb_general, расчёт, сохранение в spb_genres>
spb_genres = spb_general.groupby('genre_name')['genre_name'].count().sort_values(ascending = False)

# <просмотр первых 10 строк spb_genres>
spb_genres.head(10)

"""## Вывод
В Москве, кроме абсолютно популярного жанра поп, есть направление русской популярной музыки. Значит, что интерес к этому жанру шире. А рэп, вопреки предположению, занимает в обоих городах близкие позиции.

# Результаты исследования

Рабочие гипотезы:

•	музыку в двух городах — Москве и Санкт-Петербурге — слушают в разном режиме;

•	списки десяти самых популярных жанров утром в понедельник и вечером в пятницу имеют характерные отличия;

•	население двух городов предпочитает разные музыкальные жанры.

**Общие результаты**

Москва и Петербург сходятся во вкусах: везде преобладает популярная музыка. При этом зависимости предпочтений от дня недели в каждом отдельном городе нет — люди постоянно слушают то, что им нравится. Но между городами в разрезе дней неделей наблюдается зеркальность относительно среды: Москва больше слушает в понедельник и пятницу, а Петербург наоборот - больше в среду, но меньше в понедельник и пятницу.
В результате первая гипотеза подтверждена, вторая гипотеза подтверждена и третья не подтверждена >. не подтверждена
"""



