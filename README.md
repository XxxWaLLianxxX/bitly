# Обрезка ссылок с помощью Битли
Программа сокращает ссылки с помощью сервиса [bit.ly](https://bitly.com/) или подсчитывает клики на уже созданный битлинк. Полезно, если надо сократить очень длинную ссылку или узнать количество кликов по битлинку.
### Как установить
Сначала надо скопировать свой токен, он нужен для использования Bitly API. [Где его взять](https://support.bitly.com/hc/en-us/articles/230647907).
Затем токен надо вставить в переменную `token`, отсюда код и будет брать его для работы скрипта.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).