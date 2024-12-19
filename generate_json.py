import pandas as pd
import json

# Чтение excel файла
df = pd.read_excel('genjson.xlsx')

# Создание списка словарей
data = []
for index, row in df.iterrows():
    item = {
        "client_item_code": str(row['client_item_code']),
        "model_ids": [int(row['model_ids'])]
    }
    data.append(item)

# Запись в JSON файл
with open('genjson.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Json файл успешно создан: genjson.json")
