# STEPIC_-Selenium-Python
Автоматизация тестирования с помощью Selenium и Python

Здесь можно будет вносить некоторые заметки по мерер прохождения курса по автоматизированию с помощью Selenium WebDriver

Здесь можно будет сохранить конспект по курсу (отличаня идея!), а после этого настроить интеграцию с trello!

# Работа с GIT
## Помощь по git
git help <команда> или git <команда> --help 

## Создаём репозиторий и клонируем его
git clone *адрес вашего репозитория*

## Для того чтобы добавить файлы под бдительный взор Git, нужно выполнить команду:
git add README.md

## Посмотреть текущий статус
git status 

## Для того чтобы зафиксировать и сохранить свою работу нужно выполнить "коммит". Коммит — это небольшой кусочек вашей работы. Хорошей практикой считается делать коммиты не слишком маленькими. Еще к коммитам пишут короткие сообщения, описывающие изменения — постарайтесь писать их как можно более осмысленными. Просто представьте, что их будут читать ваши коллеги  (или вы сами через год) в попытках разобраться, что вы сделали. Сообщение добавляется с помощью флага -m.
## Если все прошло как надо, в ответе вы увидите, сколько строк и файлов изменилось:
git commit -m "тут ваше сообщение о коммите"

# PUSH Добавление изменений на сервер
## Сейчас у вашего репозитория есть две разные копии — одна локальная, которая уже содержит изменения в файле, и удаленная — на гитхабе. Необходимо наши локальные коммиты положить в удаленный репозиторий. Для этого есть специальная команда git push <репозиторий><название ветки>.
git push origin master
## Или 
git push origin main //для новых репозиториев.
