# web-forms
Основная идея проекта: заменить power apps microsoft. 
Структура проекта заключется в следующем: есть два основных приложения, которые устанавливают настройки всего проекта. Остальные приложения являются по сути самостоятельными сущностями, которые выполняют какую либо отдельную функцию, будь то заполнение формы для отправки в БД, получение каких-либо данных, построение визуализаций и т.д.

# Запуск

Для запуска проекта необходимо:
- Клонировать проект на компьютер или сервер;
- Установить виртуальное окружение ```python -m venv venv ```;
- Включить вирутальное окружение:
  -  Windows ```venv\Scripts\activate``` 
  -  Linux ```souce venv/bin/actibate```
- Из корня проекта (там где файл requirements.txt) установить зависимости ```pip install -r requirements.txt```
- Найти дирректорию, в которой лежит файл manage.py и запустить его командой ```python manage.py runserver``` или любым другим способом)

Готово. Проект запущен!

## Заполнение файла .env
В проекте использовано много логинов, паролей и прочей особо ценной информации, которую нельзя хранить в коде, поэтому важно правильно создать и заполнить файл с этими переменными.
Итак:

###### Параметры Django
- SECRET_KEY=some_secret_key - секретный ключ Django
- DEBUG=True - запускам проект в режиме разработки или продакшена
###### Параметры OAuth2.0
- GOOGLE_CID=oauth_cid - client id из личного кабинета сервиса авторизации
- GOOGLE_CSECRET=oauth_secret - secret из личного кабинета сервиса авторизации
###### Параметры отправки email, распространяются на все приложения в проекте.
- SEND_EMAIL=True - если False, то ни одна из перечисленных ниже переменных не будут загружены в проект
- EMAIL_HOST=smtp.yandex.abs
- EMAIL_PORT=465
- EMAIL_USE_SSL=True
- DEFAULT_FROM_EMAIL=someone@email.abs - тот, кто будет отображаться в поле "От"
- EMAIL_HOST_USER=someone@email.abs - чей ящик используется, обычно копия предыдущего поля
- EMAIL_HOST_PASSWORD=ijeflskjflks - пароль доступа к серверу (**!=** пароль от почты)
- EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend - подходящий бекенд Django

## Описания доступных приложений
<details>
  <summary>web-form</summary>
  <br>
    Основное приложений. Все что делает - это содержит:
  <ul>
    <li> настройки;</li>
    <li> базовый шаблон и инклюдсы, которые могут быть использованы во всех приложениях;</li>
    <li> исходные пути к каждому приложению. <b> При создании нового приложения, путь к нему добавлятся сюда в urls.py</b></li>
  </ul>
  <details>
    <summary>Описание эндпоинтов</summary>
    <ul>
      <li>'' - перенаправляет в приложение users.</li>
      <li>'saving_tracker/' - перенаправляет в приложениее saving_tracker.</li>
      <li>'admin/' - перенаправляет в админку. Доступна только заранее определенным пользователям.</li>
    </ul> 
  </details>
</details>

<details>
  <summary>users</summary>
  <br>
    Основное приложений пользователей для всех приложений. По сути сюда надо добавлять любого пользователя, а также любого человека, информацию о котором надо хранить.
  <br>
    Так же в этом приложении надо регистрировать любое новое создаанное приложение, так как через таблицу User_App создается список доступных пользователю приложений.

  <details>
    <summary>Описание эндпоинтов</summary>
    <ul>
      <li>'login/' - стандартная форма входа. Логин - email.</li>
      <li>'logout/' - эндпоинт выхода, перенаправляет на страницу входа.</li>
      <li>'' - отображает список доступных пользователю приложений.</li>
    </ul> 
  </details>
</details>

<details>
  <summary>saving-tracker</summary>
  <br>
    Первое полноценное приложение проекта. Занимается ведением списка проектов и его увеличением, рассчитывает их экономию и уведомляет ключевых пользователей каждого из проектов о каких-либо изменениях в них.
  <br>
  <details>
    <summary>Модели</summary>
    <ul>
      <li> 
        SupportFunction - модель-список бизнес функций.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        SavingType - модель-список статусов высокого уровня.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        LowLevelStatus - модель-список статусов низкого уровня.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        Group - модель-список групп.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        RiskAdjustment - модель-список уровней риска.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        LossesForAttack - модель-список типов потерь.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        BusinessArea - модель-список бизнес сегментов.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        Stream - модель-список направлений.
        <ul>
          <li>title - человекочитаемое название
            <ul><li>Максимальная длина 200 символов</li></ul> 
          </li>
          <li>pk - индекс</li>
        </ul>
      </li>
      <li> 
        Project - основная модель приложения. Хранит информацию о каждом проекте.
        <ul>
          <li>title - человекочитаемое название
            <ul>
              <li>Тип поля CharField</li>
              <li>Максимальная длина 200 символов</li>
            </ul> 
          </li>
          <li>pk - индекс</li>
          <li>owner - владелец проекта
            <ul>
              <li>Тип поля ForeignKey</li> 
              <li>Ссылка на модель User</li>
              <li>Не даст удалить объект User, если у него есть проекты</li>
            </ul> 
          </li>
          <li>support_function - функция.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель SupportFunction</li>
              <li>Не даст удалить объект SupportFunction, если у него есть проекты</li>
            </ul> 
          </li>
          <li>initial_start_date - дата старта проекта.
            <ul>
              <li>Тип поля DateField</li>
            </ul> 
          </li>
          <li>planned_start_date - плановая дата старта проекта.
            <ul>
              <li>Тип поля DateField</li>
            </ul> 
          </li>
          <li>project_end_date - дата окончания проекта.
            <ul>
              <li>Тип поля DateField</li>
            </ul> 
          </li>
          <li>saving_potential - функция.
            <ul>
              <li>Тип поля FloatField</li>
            </ul> 
          </li>
          <li>saving_type - функция.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель SavingType</li>
              <li>Не даст удалить объект SavingType, если у него есть проекты</li>
            </ul> 
          </li>
          <li>high_level_status - статус высокого уровня.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель HighLevelStatus</li>
              <li>Не даст удалить объект HighLevelStatus, если у него есть проекты</li>
            </ul> 
          </li>
          <li>low_level_status - статус низкого уровня.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель LowLevelStatus</li>
              <li>Не даст удалить объект LowLevelStatus, если у него есть проекты</li>
            </ul> 
          </li>
          <li>comment - комментарий.
            <ul>
              <li>Тип поля TextField</li>
              <li>Необязательное поле</li>
            </ul> 
          </li>
          <li>coordinator - координатор проекта.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель User</li>
              <li>Не даст удалить объект User, если у него есть проекты</li>
            </ul> 
          </li>
          <li>group - группа.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель Group</li>
              <li>Не даст удалить объект Group, если у него есть проекты</li>
            </ul> 
          </li>
          <li>risk_adjustment - уровень риска.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель RiskAdjustment</li>
              <li>Не даст удалить объект RiskAdjustment, если у него есть проекты</li>
            </ul> 
          </li>
          <li>budget_use - используется ли бюджет.
            <ul>
              <li>Тип поля BooleanField</li>
            </ul> 
          </li>
          <li>approved - согласован ли проект.
            <ul>
              <li>Тип поля BooleanField</li>
            </ul> 
          </li>
          <li>losses_for_attack - тип потерь.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель LossesForAttack</li>
              <li>Не даст удалить объект LossesForAttack, если у него есть проекты</li>
            </ul> 
          </li>
          <li>business_area - бизнес сегмент.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель BusinessArea</li>
              <li>Не даст удалить объект BusinessArea, если у него есть проекты</li>
            </ul> 
          </li>
          <li>stream - направление.
            <ul>
              <li>Тип поля ForeignKey</li>
              <li>Ссылка на модель Stream</li>
              <li>Не даст удалить объект Stream, если у него есть проекты</li>
            </ul> 
          </li>
          <li>local_focus - является ли проект фокусным.
            <ul>
              <li>Тип поля BooleanField</li>
            </ul> 
          </li>
          <li>srs_number - номер SRS (больше не используется, в формах не отображается).
            <ul>
              <li>Тип поля CharField</li>
              <li>Максимальная длина 20 символов</li>
              <li>Необязательное поле</li>
            </ul> 
          </li>
          <li>folder_url - ссылка на папку с проектом.
            <ul>
              <li>Тип поля URLField</li>
              <li>Необязательное поле</li>
            </ul> 
          </li>
          <li>Все поля share - доли в чем либо.
            <ul>
              <li>Значение в каждом поле может быть от 0 до 1</li>
              <li>Суммы по полям (primary_share, secondary_share, wharehose_share), (personal_care_share, home_care_share, tea_share, food_share, ic_share) и (share_2020, share_2021...share_2027) должны быть равны 1. <b>Важно проверять это в формах</b></li>
            </ul> 
          </li>
        </ul>
      </li>
    </ul>
  </details>

  <details>
    <summary>Обязательные проверки</summary>
    <ul>
      <li>Суммы по полям (primary_share, secondary_share, wharehose_share), (personal_care_share, home_care_share, tea_share, food_share, ic_share) и (share_2020, share_2021...share_2027) должны быть равны 1.</li>
      <li>Каждое поле primary_share, secondary_share, wharehose_share, personal_care_share, home_care_share, tea_share, food_share, ic_share, share_2020, share_2021...share_2027 должны быть между 0 и 1.</li>
      <li>Все даты находятся в пределах с 01.01.2020 по 31.12.2020</li>
      <li>Нельзя сохранить проект с полем high_level_status == 'Done', если у него potential_saving >= 40 kE, а поле approved == False.</li>
    </ul> 
  </details>

  <details>
    <summary>Описание эндпоинтов</summary>
    <ul>
      <li>'index/' - страница с основной таблицей. С нее можно зайти в любой проект, ее можно фильтровать, на ней отображается обобщенная инфомрция о проектах в рахных статусах и о суммарных сейвингах по типам. С нее можно скачать таблицу по кнопке.</li>
      <li>'update_project/' - отображает форму проекта с уже заполненными значениями, соответствующими тем, что записаны в проекте. Поля можно корректировать, а затем сохранять. После обновления координатору приходит письмо со списком изменений.</li>
      <li>'create_project/' - отображает форму проекта без заполненных полей. После сохрания создает новый проект.</li>
      <li>'download_table/' - позволяет скачать таблицу со всеми характеристиками всех проектов. Все доли ('_share_') конвертирует в абсолютные значения исходя из saving_poential.</li>
    </ul> 
  </details>

</details>
