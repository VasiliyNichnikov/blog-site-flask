# blog-site-flask
Тестовое задание ЦИСМ

##Запуск программы.
#####Проверка всех компонентов перед запуском программы:
1) Версия python 3.9
2) Установлены все компоненты из requirements.txt *(Можно использовать команду __pip install -r requirements.txt__)*
#####Запуск.
Чтобы запустить программу, файл setup.py и после этого перейти по ссылке __http://127.0.0.1:5000/__

##Вход в аккаунт.
1) Прежде чем пользоваться возможностями сервиса, нужно войти в аккаунт. Делается это с помощью Яндекс ID.
Поэтому убедитесь, что он у вас есть. 
2) После того как нажмете кнопку "Зайти с помощью Яндекс ID", разрешите сайту получить доступ к таким данным, как: email, имя, фамилия и аватарка.
3) Добро пожаловать в приложение.

##Редактирование профиля.
1) Для редактирования профиля, нажмите в правом верхнем углу на кнопку __"Профиль"__.
2) Здесь нужно нажать на кнопку __"Редактировать"__.
3) Тут вы можете поменять Имя и информацию "Обо мне".
4) После изменения информации, нажмите на __"Сохранить изменения"__, если все пройдет успешно, вам выведется сообщение, что профиль успешно изменен.

##Создание блога.
1) Для создания блога, нажмите на кнопку __"Написать блог"__
2) Тут вам необходима придумать уникальное название, написать основной текст и выбрать превью разрешением 1590x400. Тут стоит отметить, что название должно быть уникальным, а фото __обязательно__ должно иметь разрешение 1590x400.
3) После этого, нажимаем __"Опубликовать пост"__.
4) Ура, пост создан.

##Редактирование блогов.
Редактирование блогов, происходит во вкладке __"Профиль"__. Тут мы можем посмотреть на все наши написанные блоги и сделать с ними следующее:
##### 1) Редактировать.
При нажатии на эту кнопку, вы перейдете к редактированию поста и сможете поменять: или название или описание или превью поста, или все разом.
##### 2) Скрыть статью от остальных пользователей.
При нажатии на эту кнопку, вы скрываете статью от остальных пользователей и они не смогут увидеть этот пост в своей ленте.
##### 3) Посмотреть
При нажатии на эту кнопку, вы можете посмотреть как выглядит блог.
##### 4) Удалить
При нажатии на эту кнопку, вы удаляете пост из базы данных и его нельзя восстановить.

##Выход из аккаунта.
Для выхода из аккаунта, нажмите на кнопку "Выйти" в правом верхнем углу.

##Примечания.
##### Выбор БД:
Выбор sqlite был связан с тем, что у меня был опыт работы с sqlite. А также, потому что он простой и его очень легко настроить.
И плюс sqlite является файловой и тем самым все данные хранятся в одном файле.
##### Баг при загрузках изображения на сервер:
При загрузке различных изображений на сервер, я столкнулся с проблемой, что файлы имеющие русские буквы в названиях, некорректно создаются и в дальнейшем не изображаются на сервере.
Я обнаружил эту ошибку слишком поздно и за короткий срок решить мне ее не удалось.
##### Выбор технологии входа пользователя:
Вход пользователя реализован через Яндекс ID, чтобы не заставлять клиента создавать еще один лишний аккаунт, 
а просто привязать сервис к уже существующему. Изначально я хотел прикрутить вход по Google аккаунту, но впоследствии нашел документацию по Яндекс ID.
