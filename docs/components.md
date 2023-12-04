# Компонентная архитектура
<!-- Состав и взаимосвязи компонентов системы между собой и внешними системами с указанием протоколов, ключевые технологии, используемые для реализации компонентов.
Диаграмма контейнеров C4 и текстовое описание. 
-->
## Компонентная диаграмма

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="microservice")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

Person(admin, "Администратор")
Person(moderator, "Модератор")
Person(user, "Пользователь")

System_Ext(delivery_site, "Клиентский веб-сайт", "HTML, CSS, JavaScript, React", "Веб-интерфейс")

System_Boundary(conference_site, "Сайт блогов") {
   Container(client_service, "Сервис авторизации", "C++", "Сервис управления пользователями", $tags = "microService")    
   Container(package_service, "Сервис посылок", "C++", "Сервис управления посылками", $tags = "microService") 
   Container(delivery_service, "Сервис доставок", "C++", "Сервис управления доставками", $tags = "microService")   
   ContainerDb(db, "База данных", "MariaDB", "Хранение данных о пользователях, ролях, посылках и доставках", $tags = "storage")
   
}

Rel(admin, delivery_site, "Просмотр, добавление и редактирование информации о пользователях, доставках, посылках")
Rel(moderator, delivery_site, "Модерация доставок")
Rel(user, delivery_site, "Действия с сервисом: регистрация, логин, создание и получение посылки, создание доставки и т.д.")

Rel(delivery_site, client_service, "Работа с пользователями", "localhost/users")
Rel(client_service, db, "INSERT/SELECT/UPDATE", "SQL")

Rel(delivery_site, package_service, "Работа с посылками", "localhost/package")
Rel(package_service, db, "INSERT/SELECT/UPDATE", "SQL")

Rel(delivery_site, delivery_service, "Работа с достваками", "localhost/delivery")
Rel(delivery_service, db, "INSERT/SELECT/UPDATE", "SQL")

@enduml
```
## Список компонентов  

### Сервис авторизации
**API**:
-	Создание нового пользователя
      - входные параметры: login, пароль, имя, фамилия, email, обращение (г-н/г-жа)
      - выходные параметры: отсутствуют
-	Поиск пользователя по логину
     - входные параметры:  login
     - выходные параметры: имя, фамилия, email, обращение (г-н/г-жа)
-	Поиск пользователя по маске имени и фамилии
     - входные параметры: маска фамилии, маска имени
     - выходные параметры: login, имя, фамилия, email, обращение (г-н/г-жа)

### Сервис посылок
**API**:
- Создание посылки
  - Входные параметры: название посылки, описание, идентификатор пользователя
  - Выходные параметры: идентификатор посылки
- Получение посылок пользователя
  - Входные параметры: идентифифкатор посылки
  - Выходные параметры: массив из посылок, где для каждой указан идентификатор, название, описание, дата создания.

### Сервис доставок
**API**:
- Создание доставки от пользователя к пользователю
  - Входные параметры: идентификатор отправителя, идентификатор получаеля, дата отправки, дата получения, массив идентификаторов посылок.
  - Выходные параметры: идентификатор доставки
- Получение информации о доставке по получателю  
  - Входные параметры: идентификатор получателя, идентификатор доставки
  - Выходные параметры: идентификатор доставки, идентификатор получателя, идентификатор отправителя, дата отправки, дата получения, статус, массив идентификаторов посылок.
- Получение информации о доставке по отправителю
  - Входнае параметры: идентификатор получателя, идентификатор доставки
  - Выходные парамтеры: идентификатор доставки, идентификатор получателя, идентификатор отправителя, дата отправки, дата получения, статус, массив идентификаторов посылок.


### Модель данных
```puml
@startuml

class User {
  id
  login
  first_name
  last_name
  email
  insert_date
  update_date
}

class Package {
  id
  title
  description
  delivery_id
  insert_date
  update_date
}

class Delivery {
  id
  title
  sender_id
  applier_id
  status
  insert_date
  update_date
}

User <- Delivery
Delivery <- Package

@enduml
```