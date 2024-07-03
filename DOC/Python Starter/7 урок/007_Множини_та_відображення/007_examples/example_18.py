def worker_max_efficiency(workers):
    maximum = 0
    for worker in workers:
        if workers[worker]['ефективність'] > maximum:
            maximum = workers[worker]['ефективність']
    return maximum


def worker_min_efficiency(workers):
    minimum = 150
    for worker in workers:
        if workers[worker]['ефективність'] < minimum:
            minimum = workers[worker]['ефективність']
    return minimum


workers = {
    'Смирнов': {
        'посада': 'менеджер з продажу',
        'ефективність': 86
    },
    'Колягина': {
        'посада': 'менеджер з продажу',
        'ефективність': 69
    },
    'Костин': {
        'посада': 'менеджер з продажу',
        'ефективність': 78
    },
    'Щербаков': {
        'посада': 'менеджер з продажу',
        'ефективність': 91
    },
    'Борисова': {
        'посада': 'менеджер з продажу',
        'ефективність': 99
    }
}


print('Найкращий результат:', worker_max_efficiency(workers))
print('Найгірший результат:', worker_min_efficiency(workers))
