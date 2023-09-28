**Работа с ORM в Django**

- Создайте новое приложение «Собаки».
- Опишите модель «Собака» с полями: кличка собаки, порода, фотография, дата рождения.
- Добавьте модель «Порода» с полями: название, описание.
- В модели «Собака» замените поле «порода» на ссылку на модель «Порода».
- В админку выведите список пород, а также список собак.
- У списка собак добавьте фильтрацию по породам.
- Сформируйте фикстуры для наполнения базы пород и собак.

**Список задач по теме «Шаблонизация»:**
- Подключите Bootstrap к проекту.
- Сделайте главную страницу с тремя породами из базы.
- Полный список пород выведите на отдельную страницу.
- Для каждой породы реализуйте возможность перехода к списку собак, которые относятся к выбранной породе.
- Каждая кличка должна быть выведена, начиная с заглавной буквы. Например: Маленькая Леди.
- Выделите общий базовый шаблон.
- Вынесите в подшаблоны карточки пород и подключите их на главной странице и на странице со списком пород.
- Добавьте шаблонный фильтр, который убирает необходимость выводить картинку с припиской `/media/` 
в начале пути. То есть чтобы можно было писать 

    ```html
       <a href="{{ object.image|mymedia }}" />
    ```

 вместо 

    ```html
       <a href="/media/{{ object.image }}" />
    ```