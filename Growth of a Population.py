def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year +=1
    return year
nb_year(1500, 5, 100, 5000)

# 比较标准的写法,就是不知道100.是啥意思