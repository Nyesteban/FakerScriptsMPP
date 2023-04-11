from faker import Faker
import math
import random


def decode(i):
    k = math.floor((1 + math.sqrt(1 + 8 * i)) / 2)
    return k + 1, i - k * (k - 1) // 2 + 1


def rand_pair(n):
    return decode(random.randrange(n * (n - 1) // 2))


def rand_pairs(n, m):
    return [decode(i) for i in random.sample(range(n * (n - 1) // 2), m)]


fake = Faker()

sql = ""

"""
# create INSERT SQL statement
for i in range(0, 1000):
    sql += "INSERT INTO \"Companies\" (\"CompanyName\", \"CompanyDescription\", \"CompanyRevenue\", \"CompanyEstablishmentYear\", \"CompanyRating\") VALUES "
    for j in range(0, 1000):
        sql += "('{}', '{}', {}, {}, {}),".format(fake.company(), fake.catch_phrase(), fake.pyint(0, 100), fake.pyint(1800, 2023), fake.pydecimal(left_digits=1, right_digits=2, positive=True, min_value=1, max_value=5))
    sql = sql[:-1]
    sql += ";\n"

# write SQL statement to file
with open('insert.sql', 'w') as f:
    f.write(sql)
"""

"""
for i in range(0, 1000):
    sql += "INSERT INTO \"Apps\" (\"AppName\", \"AppVersion\", \"AppDescription\", \"AppSize\", \"AppPrice\") VALUES "
    for j in range(0, 1000):
        sql += "('{}', '{}', '{}', {}, {}),".format(fake.word(), fake.md5(), fake.bs(), fake.pyint(1, 100000), fake.pydecimal(left_digits=2, right_digits=2, positive=True, min_value=1, max_value=100))
    sql = sql[:-1]
    sql += ";\n"

# write SQL statement to file
with open('insertapps.sql', 'w') as f:
    f.write(sql)
"""

"""
for i in range(0, 1000):
    sql += "INSERT INTO \"Games\" (\"GameName\", \"GameDescription\", \"GameLength\", \"GameSize\", \"GameRating\", \"CompanyID\") VALUES "
    for j in range(0, 1000):
        sql += "('{}', '{}', {}, {}, {}, {}),".format(fake.word(), fake.sentence(), fake.pyint(1, 100), fake.pyint(1, 100000), fake.pydecimal(left_digits=1, right_digits=2, positive=True, min_value=1, max_value=5), fake.pyint(2, 1000001))
    sql = sql[:-1]
    sql += ";\n"

# write SQL statement to file
with open('insertgames.sql', 'w') as f:
    f.write(sql)
"""

list_of_keys = rand_pairs(1000000, 10000000)
k = 0

for i in range(0, 10000):
    sql += "INSERT INTO \"DevelopmentDetails\" (\"CompanyId\", \"AppId\", \"DevelopmentCosts\", \"DevelopmentTimeInHours\") VALUES "
    for j in range(0, 1000):
        CompanyId = list_of_keys[k][0]
        AppId = list_of_keys[k][1]

        DevelopmentCosts = fake.random_int(min=1, max=10000)
        DevelopmentTimeInHours = fake.random_int(min=1, max=1000)

        # create INSERT SQL statement
        sql += "({}, {}, {}, {}),".format(CompanyId, AppId, DevelopmentCosts, DevelopmentTimeInHours)
        k = k + 1
    sql = sql[:-1]
    sql += ";\n"

# write SQL statement to file
with open('insertdev.sql', 'w') as f:
    f.write(sql)
