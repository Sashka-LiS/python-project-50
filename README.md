# Hexlet tests and linter status:
[![Actions Status](https://github.com/Sashka-LiS/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Sashka-LiS/python-project-50/actions)
[![Action Status](https://github.com/Sashka-LiS/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Sashka-LiS/python-project-50/actions)

# Maintainability and test coverage badges:
[![Maintainability](https://api.codeclimate.com/v1/badges/edd85589b4b839947100/maintainability)](https://codeclimate.com/github/Sashka-LiS/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/edd85589b4b839947100/test_coverage)](https://codeclimate.com/github/Sashka-LiS/python-project-50/test_coverage)

# Описание
Это пакет "Генератор разницы" для второго проекта от Хекслет.
Он работает с двумя форматами файлов: JSON и YAML. Находит разницу между ними и выводит ее в консоль в одном из трех форматов: "stylish", "plain", "json". Формат "stylish" используется для вывода по умолчанию.

# Установка пакета
#### 1.Клонируйте репозиторий
```
git clone https://github.com/Sashka-LiS/python-project-50
```
#### 2. Установите зависимости
```
make install
```
#### 3. Осуществите сборку пакета
```
make build
```
#### 4. Установите локально
```
make install_gendiff
```

# Примеры работы
### Сравнение плоских файлов (JSON) в формате "stylish".
[![asciicast](https://asciinema.org/a/qjPcXNgJpN1qSpiRNUY1NfVh9.svg)](https://asciinema.org/a/qjPcXNgJpN1qSpiRNUY1NfVh9)

### Сравнение плоских файлов (YAML) в формате "stylish".
[![asciicast](https://asciinema.org/a/7rK1KOjOfF0jAKuu73qhYNSO4.svg)](https://asciinema.org/a/7rK1KOjOfF0jAKuu73qhYNSO4)

### Вывод разницы между вложенными JSON файлами в формате "stylish".
[![asciicast](https://asciinema.org/a/74mrkiu95Cmrm0Ld6Rf27gu4x.svg)](https://asciinema.org/a/74mrkiu95Cmrm0Ld6Rf27gu4x)

### Вывод разницы между вложенными YAML файлами в формате "stylish".
[![asciicast](https://asciinema.org/a/FDz80csxX1mvZ62gdJzcEI2Bq.svg)](https://asciinema.org/a/FDz80csxX1mvZ62gdJzcEI2Bq)

### Вывод разницы между вложенными JSON файлами в формате "plain".
[![asciicast](https://asciinema.org/a/8CLpiyY7WUXRvHJESdRjmcrUD.svg)](https://asciinema.org/a/8CLpiyY7WUXRvHJESdRjmcrUD)

### Вывод разницы между вложенными YAML файлами в формате "plain".
[![asciicast](https://asciinema.org/a/dgFFTO1JvH5dMf1I2dYbunCda.svg)](https://asciinema.org/a/dgFFTO1JvH5dMf1I2dYbunCda)

### Вывод разницы между файламе в формате JSON.
