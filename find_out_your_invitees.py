from psycopg2.extras import DictCursor
import psycopg2


def find(entered_invite_code):
    date = None
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="anna30.08",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="clients_db")
        with connection.cursor(cursor_factory=DictCursor) as cursor:
            postgres_insert_query = """SELECT phone, entered_invite_code FROM user_registrations_user;"""
            cursor.execute(postgres_insert_query)
            date = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    if date:
        your_invitees = [d[0] for d in date if d[1] == entered_invite_code]
        return your_invitees
    else:
        return []


print(find(entered_invite_code='ib90jau7qd'))
