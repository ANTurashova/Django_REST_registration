### Регистрация, авторизация по номеру телефона по API, получение данных

Регистрация пользователя: 
![alt tag](https://sun9-87.userapi.com/impf/D9WtTbHCJW8PhVtWHnLsn6Dv0N5YFqbTNuU5rw/uJX8Z0fMPbM.jpg?size=882x513&quality=95&sign=2cd91b0cc25acddf60bab4ccd8d3243a&type=album "Описание будет тут")

Авторизация пользователя, получение токена: 
![alt tag](https://sun9-79.userapi.com/impf/eQXAPj_3t62hfv-HwGnTyIae-7vIYC3fufitBg/PVAZ0PjxSKk.jpg?size=877x500&quality=95&sign=b68ed2dcb164de88447a547e3a79377a&type=album "Описание будет тут")

Получение информации о пользователе по его токену:
![alt tag](https://sun9-63.userapi.com/impf/Yhw-Ux9FQDC5fWU_cqLruUv4yHUCXh8bqEO8fQ/JBFlhqMts4c.jpg?size=881x466&quality=95&sign=9ac9e751c54c94fff52308676c72eeb1&type=album "Описание будет тут")



**Реализована логика и API для следующего функционала:**

● Регистрация и авторизация по номеру телефона;

● Запрос на профиль пользователя;

● Пользователю при первой авторизации нужно присвоить рандомно сгенерированный 10-значный инвайт-код (цифры и символы)

● В профиле у пользователя должна быть возможность ввести чужой инвайт-код (при вводе проверять на существование). В своем профиле можно активировать только 1 инвайт код, если пользователь уже когда-то активировал инвайт код, то нужно выводить его в соответсвующем поле в запросе на профиль пользователя

● В API профиля должен выводиться список пользователей(номеров телефона), которые ввели инвайт код текущего пользователя.