# -*- coding: utf-8 -*-
"""занятие 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QRvaUbEipwWk0Dc7Ons6s0-x3v8TFZn9

## Охота на мусор
Процесс подготовки данных для дальнейшего анализа называется предобработка. Заключается она в поиске проблем, которые могут быть в данных, и в решении этих проблем.
В информатике работает принцип GIGO (от англ. garbage in — garbage out, буквально «мусор на входе — мусор на выходе»). Это значит, что при ошибках во входных данных даже правильный алгоритм работы выдаёт неверные результаты.
Посмотрите на этот срез данных 

![image.png](attachment:image.png)
В столбце genre для одного жанра есть два названия: джаз и jazz. Если принять всё как есть, подсчёт прослушанных джазовых композиций даст два ответа — для жанра джаз и для жанра jazz, которые представляют одну и ту же сущность. Это помешает сделать правильные выводы об интересе пользователей к джазу, и может повлечь неверные решения.
Вообще сложности с данными бывают двух видов:

•	данные содержат мусор;

•	данные корректны, но представлены в такой форме, что малопригодны для анализа.

В этой теме мы раскроем базовые механизмы борьбы с часто встречаемыми проблемами. Из них самые очевидные, но в то же время самые опасные:

• некорректное именование столбцов

• дублирование значений

• отсутствующие значения (NaN)

Механизмы борьбы с ними — основа, с которой вы можете начать своё развитие как специалист по предобработке данных.

**Задача**
1. Загрузите датасет с данными из Яндекс.Музыка Вызовите метод info(), чтобы просмотреть сводку по всему набору данных.
"""

import pandas as pd
df = pd.read_csv('yandex_music.csv')
df.info()

"""Метод info() возвращает названия столбцов таблицы и сведения о типах данных в ней. Итак, наши проблемы:

•	В начале названия одного столбца явно есть несколько лишних пробелов. От них нужно избавиться.

•	Название из двух слов содержит пробел, который необходимо заменить на символ нижнего подчёркивания.

•	Названия должны быть на одном языке и набраны в одном регистре, чтобы не заучивать уникальный формат для каждого столбца.

•	Каждый столбец содержит определённый признак — крайне желательно, чтобы название столбца отражало в краткой форме, какая информация в нём содержится.

Рассмотрим  таблицу с расстояниями (в миллионах километров) от Земли до небесных тел.

"""

import pandas as pd
measurements = [['Солнце',146,152], # Измерения хранятся в списке списков 
              ['Луна',0.36, 0.41], # measurements (англ. measurement, «измерение»).
              ['Меркурий',82, 217], 
              ['Венера',38, 261],
              ['Марс',56,401],
              ['Юпитер',588, 968],
              ['Сатурн',1195, 1660],
              ['Уран',2750, 3150],
              ['Нептун', 4300, 4700],
              ['Комета Галлея', 6, 5400]]
# Названия столбцов хранятся в переменной header.
header = ['Небесные тела ','MIN', 'MAX'] 
# Сохраним структуру данных в переменной celestial (англ. celestial, «небесный»).
celestial = pd.DataFrame(data = measurements, columns = header)

"""Заметно, что столбцы называются на разных языках. Название Небесные тела содержит опасный пробел в конце, и слова этого названия разделены пробелом.

Символы за пределами базовой латиницы — недруги аналитика; от них надо избавляться в первую очередь. Правильно будет переименовать «Небесные тела» в celestial_bodies. MIN и MAX уже написаны латиницей, но эти сокращения мало говорят о том, что за цифры записаны в соответствующих столбцах. Хорошее решение — назвать их min_distance и max_distance. Так сразу понятно, что это минимальные и максимальные расстояния.

Чтобы изменить названия столбцов, воспользуйтесь методом set_axis(). Он принимает три аргумента:

•	cписок с новыми названиями столбцов;

•	axis — ось, которой новые названия присваиваются: 'index', если они даются строкам, и 'columns', если это список новых названий столбцов;

•	inplace. Принимает значения True либо False. В первом случае метод set_axis() перестраивает структуру данных так, что она замещает прежнюю в переменной с тем же именем.

![image.png](attachment:image.png)


"""

#Заменим названия столбцов таблицы с небесными телами.
celestial.set_axis(['celestial_bodies','min_distance','max_distance'], axis = 'columns', inplace = True) 
#Проверим результат:

print(celestial)

"""Готово! Теперь эта таблица годится для анализа. Давайте проверим названия столбцов в данных Яндекс.Музыки.

**Задача**   
1.
Выведите список столбцов.

2.
Подготовьте список new_names с новыми именами для столбцов.

•	user_id → user_id

•	total play → total_play_seconds

•	Artist → artist_name

•	genre → genre_name

•	track → track_name

3.
Переименуем столбцы таблицы, которая хранится в переменной df.
Вызовите метод set_axis() и передайте ему список new_names, а значением аргумента inplace установите True.

4.
Проверьте, что получилось, запросив для нашей структуры данных df атрибут columns.


"""

#Выведем список столбцов
print(df.columns)

#Подготовим список new_names с новыми именами для столбцов.
#• user_id → user_id
#• total play → total_play_seconds
#• Artist → artist_name
#• genre → genre_name
#• track → track_name
new_names = ['user_id', 'track_name', 'artist_name', 'genre_name', 'city', 'total_play_seconds', 'day']

df.head(10)

#Переименуем столбцы таблицы, которая хранится в переменной df. 
#Вызовим метод set_axis() и передадим ему список new_names, а значением аргумента inplace установим True.
df.set_axis(new_names, axis = 'columns', inplace = True)

#Проверим, что получилось, запросив для нашей структуры данных df атрибут columns.
print(df.columns)

"""## Обработка пропущенных значений

Замены пропущенных значений в DataFrame бывают трёх видов:

1) Ожидаемые: None или NaN. None — это эквивалент null в других языках программирования: особое значение, указывающее, что в этой ячейке таблицы никакого значения нет. None относится к NoneType. NaN говорит о том, что в ячейке находится «не число». Основное отличие NaN в том, что его можно использовать в математических операциях, так как по типу это число с плавающей запятой.

2) Странные: плейсхолдеры (тексты-заполнители) какого-нибудь общепринятого стандарта, иногда неизвестного вам, но которого придерживаются составители. Чаще всего это n/a, na, NA, и N.N. либо NN.

3) Неожиданные: например, разработчики решили, что пустые значения в таблице будут заполняться знаками вопроса или нулями. В лучшем случае этот факт укажут в документации, в худшем – придётся просматривать данные самостоятельно. Если какой-нибудь спецсимвол или число встречаются часто, и этому нет внятного объяснения, то высока вероятность, что так передаются пропущенные значения.

Но будьте осторожны: иногда нули — это действительно нули, как в наборе данных Яндекс.Музыкка, где ноль показывает, что трек был пропущен (его слушали 0 секунд).

Рассмотрим методы борьбы с пропущенными значениями на примере данных ВОЗ о заболеваемости холерой в 2017 году:
"""

cholera=pd.read_csv('D:/My Doc/сholera.csv', sep=';')

print(cholera)

"""Для разных регионов (столбец 'region') и стран ('country') указано общее число случаев заболевания холерой
('total_cases'), в том числе завозные случаи ('imported_cases') и смертельные ('deaths'). 

Всё это целые числа, поскольку данные приведены с точностью до человека. 
Источник: Всемирная организация здравоохранения, Weekly Epidemiological Record), 21 September 2018, vol. 93, 38, pp. 489–500.

Посчитать в каждом столбце отсутствующие значения можно методом **.isnull()**. 
Если значение элемента не существует, **.isnull()** возвращает True, а иначе — False. 
Суммируют эти True вызовом метода **sum()**, который в этом случае возвращает общее число элементов без 
определённых значений.

"""

print(cholera.isnull().sum())

"""Также подойдёт метод **isna()**, подсчитывающий пустые значения. В таблице по холере пропущенные значения качественные, так что этот метод отыщет их все."""

print(cholera.isna().sum())

"""Метод борьбы с пропущенными значениями, который вы выберете, должен учитывать интересы решения конечной задачи бизнеса. В целом есть два пути: заполнить пропущенные значения на основе имеющихся данных или удалить все строки с пропущенными значениями.

Бизнес разрывается между двумя решениями: как потратить не слишком много времени и как не упустить данные, которые обычно чего-то стоят.

Если сейчас пойти по пути удаления всех строк, где есть пропущенные значения, можно потерять важные данные, например, в Африке было зафиксировано 179835 случаев заболевания, но ни одного завозного случая (это сейчас отмечено NaN). Удалив эту строку, мы потеряем важные данные для статистики.

Другая ситуация с Европой. Вся строка состоит из пропущенных значений. Примечание сообщает, что в 2017 году европейцы холерой не болели. Значит, строку можно удалить и это никак не повлияет на результат.
Чтобы не лишиться строк с важными данными, заполним значения NaN в столбце **'imported_cases'** нулями.
Для этого лучше всего использовать метод **fillna()**, где в качестве аргумента выступает заменитель отсутствующих значений.

![image.png](attachment:image.png)
"""

cholera['imported_cases']=cholera['imported_cases'].fillna(0)
print(cholera)

"""От строк с нулевыми значениями избавляются методом **dropna()**. Он удаляет любую строку, где есть хоть одно отсутствующее значение.

У этого метода есть аргументы:

1.	**subset = [ ]**. Его значением указывают названия столбцов, где нужно искать пропуски.

2.	Уже знакомый нам **inplace**.

![image.png](attachment:image.png)

"""

cholera.dropna(subset=['total_cases', 'deaths'], inplace=True)
print(cholera)

"""Теперь удалим правый столбец с пропущенными значениями. 

Снова вызываем метод **dropna()**. Как и **set_axis()**, он имеет ещё и аргумент **axis**. Если этому аргументу присвоить значение **'columns'**, он удалит любой столбец, где есть хоть один пропуск.

![image.png](attachment:image.png)

"""

cholera.dropna(axis = 'columns', inplace = True) 
print(cholera)

"""Теперь таблица готова к дальнейшему изучению: ненужные пропуски удалены, но при этом сохранены важные данные.
Пропуски в данных появляются разными путями. Например, пользователь не указал о себе какие-нибудь сведения или автоматизированная система сбора информации дала сбой. Иногда пропуски оставляют умышленно, рассчитывая на автозаполнение спецсимволами.


Давайте разберёмся с пропущенными значениями в данных для задачи Яндекс.Музыки.

# Задача

1.Просмотрите информацию о наборе данных: воспользуйтесь методом info().

2. Посчитайте количество пропущенных значений и выведите его на экран.

3. Для решения поставленной менеджером задачи важно сохранить содержание столбца 'genre_name'. Если по какой-то причине имя исполнителя и название трека оказались упущены, а жанр композиции известен, эту строку надо сберечь.
Заполните отсутствующие значения столбца 'track_name' строкой 'unknown'.

4. Заполните отсутствующие значения столбца 'artist_name' словом unknown.

5. Удалите пропущенные значения из столбца 'genre_name'.

6. Проверьте полученный результат. Просмотрите информацию о наборе данных: воспользуйтесь методом info().


"""

#1.Просмотрите информацию о наборе данных: воспользуйтесь методом info().
df.info()

#2. Посчитайте количество пропущенных значений и выведите его на экран.
print(df.isnull().sum())

maskGenreNameIsNull = df['genre_name'].isnull()
genreNameIsNull = df.loc[maskGenreNameIsNull]
genreNameIsNull.head(10)

#3. Для решения поставленной менеджером задачи важно сохранить содержание столбца 'genre_name'. 
# Если по какой-то причине имя исполнителя и название трека оказались упущены, а жанр композиции известен, эту строку надо сберечь. 
# Заполните отсутствующие значения столбца 'track_name' строкой 'unknown'.
df['track_name'] = df['track_name'].fillna('unknown')
genreNameIsNull2 = df.loc[maskGenreNameIsNull]
genreNameIsNull2.head(10)

#4. Заполните отсутствующие значения столбца 'artist_name' словом unknown.
df['artist_name'] = df['artist_name'].fillna('unknown')
genreNameIsNull3 = df.loc[maskGenreNameIsNull]
genreNameIsNull3.head(10)

#5. Удалите пропущенные значения из столбца 'genre_name'.
df.dropna(subset=['genre_name'], inplace=True)
genreNameIsNull4 = df.loc[maskGenreNameIsNull]
genreNameIsNull4.head(10)

#6. Проверьте полученный результат. Просмотрите информацию о наборе данных: воспользуйтесь методом info().
df.info()

print(df.isnull().sum())

"""## Обработка дубликатов

Когда мы говорим о дубликатах (дублированных записях), то представляем себе две одинаковых строки с идентичной информацией. Действительно, это дубликаты, и мы ещё разберём, как от них избавляться.


Но бывают и менее явные дубликаты: скажем, две якобы разные категории публикаций. К примеру, «Политика» и «Политическая ситуация». При агрегировании данных эти две категории будут отражены как разные подмножества набора данных, хотя на самом деле все публикации о политике нужно объединить в одну категорию. При всех возможностях Pandas важно изучать данные глазами и обдумывать их. Иначе вас ожидает масса неприятных сюрпризов.


Помимо вредного влияния дубликатов на результат, их наличие затягивает процесс анализа. Большое количество повторов неоправданно раздувает размер таблицы, а значит, увеличивает время обработки данных.
Грубые дубликаты — повторы — обнаруживают методом **duplicated()**. Он возвращает **Series** со значением **True** при наличии дубликатов, и **False**, когда их нет.

**print(df.duplicated())**

Чтобы посчитать количество дубликатов в наборе данных, нужно вызвать метод **sum()**:

**print(df.duplicated().sum())** 
 
Для удаления дубликатов есть метод **drop_duplicates()**:

**df.drop_duplicates(inplace = True)** 

При вызове метода **drop_duplicates()** вместе с повторяющимися строками удаляются их индексы.

Последовательность индексов нарушается: после 0 следует 2 и т.д.

Поэтому вызов **drop_duplicates()** соединяют в цепочку с вызовом метода **reset_index()**. Тогда создаётся новый **DataFrame**, где старые индексы превращаются в обычный столбец под названием **index**, а индексы всех строк снова следуют в естественном порядке.
Если же мы не хотим создавать новый столбец **index**, то при вызове **reset_index()** передаётся аргумент **drop** со значением **True**. Все индексы переписываются в порядке возрастания, без пропусков.

![image.png](attachment:image.png)

Дубликаты в названиях категорий отследить сложнее, но всё-таки можно. Для просмотра всех уникальных значений в столбце используется метод **unique()**.

Рассмотрим таблицу с рейтингом первой ракетки мира.
"""

rating = ['date','name','points']
players = [
['2018.01.01',    'Рафаэль Надаль',10645],
['2018.01.08',    'Рафаэль Надаль',    10600],
['2018.01.29',    'Рафаэль Надаль',    9760],
['2018.02.19',    'Роджер Федерер',    10105],    
['2018.03.05',    'Роджер Федерер',    10060],
['2018.03.19',    'Роджер Федерер',    9660],
['2018.04.02',    'Рафаэль Надаль',    8770],
['2018.06.18',    'Roger Federer',    8920],
['2018.06.25',    'Рафаэль Надаль',    8770],
['2018.07.16',    'Рафаэль Надаль',    9310],
['2018.08.13',    'Рафаэль Надаль',    10220],
['2018.08.20',    'Рафаэль Надаль',    10040],
['2018.09.10',    'Рафаэль Надаль',    8760],
['2018.10.08',    'Рафаэль Надаль',    8260],
['2018.10.15',    'Рафаэль Надаль',    7660],
['2018.11.05',    'Новак Джокович',    8045],
['2018.11.19',    'Новак Джокович',    9045]
]
tennis = pd.DataFrame(data = players, columns= rating)
print(tennis)

"""В 2018 году рейтинг первой ракетки мира по версии ATP обновлялся 17 раз. Но спортсменов с самым большим в мире профессионального тенниса рейтингом гораздо меньше. Если применить ко второму столбцу метод **unique()**, возвращаются только три имени."""

print(tennis['name'].unique())

"""Кроме имени Роджера Федерера на русском языке, вернулось его же имя латиницей. Это тоже дубликат. Нужно заменить этот артефакт правильным именем на русском языке.
Такие задачи решает метод **replace()**, где первый аргумент — текущее значение, а второй — новое, нужное.

"""

tennis['name'] = tennis['name'].replace('Roger Federer', 'Роджер Федерер') 
print(tennis['name'])

"""Теперь всё хорошо. Настало время разобраться с дубликатами в таблице данных Яндекс.Музыки.
# Задача  

1.Сохраните текущий размер таблицы в переменной shape_table.

2. Посчитайте и выведите на экран суммарное количество дубликатов в таблице.

3. Удалите дубликаты. Используйте метод reset_index() для сохранения порядка индексов.

4. Сохраните в переменную shape_table_update размер таблицы после удаления дубликатов.

5. Сравните переменные shape_table и shape_table_update. Если они равны, выведите сообщение 'Размер таблицы не изменился, текущий размер: ' и значение переменной shape_table_update.

6. Получите уникальные значения столбца 'genre_name', используйте метод unique(). Просмотрите результат и найдите название жанра, которое выпадает из общего ряда.

7. В столбце 'genre_name' замените значение 'электроника' на 'electronic' .

8. Оцените изменения: пересчитайте количество значений 'электроника' в столбце 'genre_name'. Если удалось всё заменить, результат должен быть равен 0. Сохраните этот результат в переменной genre_final_count, выведите на экран.


"""

#1.Сохраним текущий размер таблицы в переменной shape_table.
shape_table = df.shape
print('Размер таблицы: ', shape_table)

#2.Посчитаем и выведем на экран суммарное количество дубликатов в таблице.
print(df.duplicated().sum())

#3.Удалим дубликаты. Используем метод reset_index() для сохранения порядка индексов.
df = df.drop_duplicates().reset_index(drop = True)

#4.Сохраним в переменную shape_table_update размер таблицы после удаления дубликатов.
shape_table_update = df.shape
print('Размер таблицы после удаления дубликатов: ', shape_table_update)

#5.Сравните переменные shape_table и shape_table_update. 
#Если они равны, выведите сообщение 'Размер таблицы не изменился, текущий размер: ' и значение переменной shape_table_update.
if  shape_table == shape_table_update:
    print('Размер таблицы не изменился, текущий размер: ', shape_table_update)

#6.Получите уникальные значения столбца 'genre_name', используйте метод unique(). 
#Просмотрите результат и найдите название жанра, которое выпадает из общего ряда.
print(df['genre_name'].unique())

#7.В столбце 'genre_name' замените значение 'электроника' на 'electronic'.
df['genre_name'] = df['genre_name'].replace('электроника', 'electronic') 
print(df['genre_name'])

#8.Оцените изменения: пересчитайте количество значений 'электроника' в столбце 'genre_name'. 
#Если удалось всё заменить, результат должен быть равен 0. 
#Сохраните этот результат в переменной genre_final_count, выведите на экран.
maskGenreName = df['genre_name'] == 'электроника'
genre_final_count = df['genre_name'].loc[maskGenreName].count()
print(genre_final_count)