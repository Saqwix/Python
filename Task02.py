# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                if not (w or z or y or x) == (not w and not z and not y and not x):
                    print(f'Утверждение (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) истенно при w = {w}, z={z}, y={y}, x={x}')