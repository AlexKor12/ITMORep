def process_local_file(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().replace(',', '.')
            if line:
                parts = line.split()
                if len(parts) == 2:
                    try:
                        num1 = float(parts[0])
                        num2 = float(parts[1])
                        data.append((num1, num2))
                    except ValueError:
                        print(f"Ошибка в строке: {line}")
    return data

# Пример использования
processed_data = process_local_file("data.txt")

s = 0
for i in range(len(processed_data)):
    s += processed_data[i][1];

print(s/len(processed_data))
