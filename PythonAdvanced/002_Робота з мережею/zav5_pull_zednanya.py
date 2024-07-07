# Вивчіть докладніше та спробуйте можливості налаштування pull з'єднань і його режимів. Використовуючи утиліту ab,
# протестуйте ваші напрацювання (https://ru.wikipedia.org/wiki/ApacheBench).


# ab (ApacheBench) - це утиліта командного рядка для тестування продуктивності HTTP-серверів. Вона дозволяє надсилати велику
# кількість запитів до веб-серверу і вимірювати продуктивність, включаючи швидкість відповіді та кількість оброблених
# запитів за секунду.

# Основні параметри утиліти ab
# -n <requests>: Кількість запитів, які будуть надіслані.
# -c <concurrency>: Кількість одночасних запитів.
# -t <timelimit>: Обмеження за часом тесту у секундах.
# -k: Використання постійних з'єднань (Keep-Alive).
# -H <header>: Додавання заголовків до запитів.

# Приклад використання ab

# sh

# ab -n 1000 -c 10 http://www.example.com/
# Цей приклад надсилає 1000 запитів до http://www.example.com/ з 10 одночасними з'єднаннями.

# Режими pull з'єднань та налаштування
# Для налаштування pull з'єднань можна використовувати параметр -k, який включає режим Keep-Alive. У цьому режимі одне
# TCP-з'єднання використовується для кількох HTTP-запитів, що зменшує затримку і підвищує продуктивність.

# Використання утиліти ab для різних режимів з'єднань
# Без Keep-Alive (один запит на з'єднання)

# sh

# ab -n 1000 -c 10 http://www.example.com/
# З Keep-Alive (декілька запитів на одне з'єднання)

# sh

# ab -n 1000 -c 10 -k http://www.example.com/
# Аналіз результатів ab
# Після виконання тесту утиліта ab надасть різноманітні дані про продуктивність сервера, включаючи:

# Time taken for tests: Час, витрачений на виконання всіх запитів.
# Complete requests: Загальна кількість виконаних запитів.
# Failed requests: Кількість невдалих запитів.
# Requests per second: Кількість запитів, оброблених сервером за секунду.
# Time per request: Середній час обробки одного запиту.
# Transfer rate: Швидкість передачі даних

# Приклад результату виконання ab

# sh


# This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
# Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
# Licensed to The Apache Software Foundation, http://www.apache.org/
#
# Benchmarking www.example.com (be patient)
# Completed 100 requests
# Completed 200 requests
# Completed 300 requests
# ...
#
# Finished 1000 requests
#
#
# Server Software:        Apache/2.4.41
# Server Hostname:        www.example.com
# Server Port:            80
#
# Document Path:          /
# Document Length:        234 bytes
#
# Concurrency Level:      10
# Time taken for tests:   2.345 seconds
# Complete requests:      1000
# Failed requests:        0
# Total transferred:      345000 bytes
# HTML transferred:       234000 bytes
# Requests per second:    426.82 [#/sec] (mean)
# Time per request:       23.45 [ms] (mean)
# Time per request:       2.35 [ms] (mean, across all concurrent requests)
# Transfer rate:          143.12 [Kbytes/sec] received
#
# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        1    2   1.2      2      10
# Processing:     5   21   4.3     20      30
# Waiting:        4   19   4.5     18      28
# Total:          6   23   4.5     22      35
#
# Percentage of the requests served within a certain time (ms)
#   50%     22
#   66%     24
#   75%     26
#   80%     28
#   90%     32
#   95%     33
#   98%     34
#   99%     35
#  100%     35 (longest request)
# Ці дані допомагають оцінити продуктивність сервера та виявити потенційні проблеми, такі як тривалі часи відповіді або
# невеликі швидкості обробки запитів.
