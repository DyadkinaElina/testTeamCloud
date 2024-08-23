import os
# Создание директории, если её нет
os.makedirs('testTeamCloud', exist_ok=True)
with open('results.txt', 'w') as file:
    file.write('It is result')