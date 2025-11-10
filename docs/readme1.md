#geometric_lib

## ќписание проекта
geometric_lib Ч это учебна€ библиотека дл€ работы с простыми геометрическими фигурами.  
—одержит функции дл€ вычислени€ площади и периметра круга и квадрата.

## —труктура проекта
"circle.py" Ч функции дл€ работы с окружностью:
"area(r)" Ч возвращает площадь круга радиуса `r`;
"perimeter(r)" Ч возвращает длину окружности радиуса `r`.
"square.py" Ч функции дл€ работы с квадратом:
"area(a)" Ч возвращает площадь квадрата со стороной `a`;
"perimeter(a)" Ч возвращает периметр квадрата со стороной `a`.
"docs/" Ч документаци€:
	"README.md" Ч математические формулы, используемые в проекте;
	"readme1.md" - общее описание проекта;


## ѕример использовани€
```python
from circle import *
from square import area as square_area, perimeter as square_perimeter

print(area(5))          # 78.54
print(perimeter(5))     # 31.41
print(square_area(4))   # 16
print(square_perimeter(4))  # 16

## »стори€ изменений
- 2f79d87 2025-09-29 readme1.md
- cf78fc2 2025-09-29 added documentation
- d078c8d 2021-03-04 L-03: Docs added
- 8ba9aeb 2021-03-04 L-03: Circle and square added