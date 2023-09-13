import json

# Создаем словарь для подсчета ошибок с соответствующими ключами
error_count = {
    "bus_id": 0,
    "stop_id": 0,
    "stop_name": 0,
    "next_stop": 0,
    "stop_type": 0,
    "a_time": 0
}

# Получаем данные из ввода
jdata_dict = json.loads(input())

# Проверяем каждую запись в данных
for line in jdata_dict:
    if not isinstance(line['bus_id'], int) or not line['bus_id']:
        error_count["bus_id"] += 1
    if not isinstance(line['stop_id'], int) or not line['stop_id']:
        error_count["stop_id"] += 1
    if not isinstance(line['stop_name'], str) or not line['stop_name']:
        error_count["stop_name"] += 1
    if not isinstance(line['next_stop'], int):
        error_count["next_stop"] += 1
    if not isinstance(line['stop_type'], str) or line['stop_type'] not in ['O', 'S', 'F', '']:
        error_count["stop_type"] += 1
    if not isinstance(line['a_time'], str) or not line['a_time']:
        error_count["a_time"] += 1

# Выводим результаты
print(f"Type and required field validation: {sum(error_count.values())} errors")
for key, value in error_count.items():
    print(f"{key}: {value}")
