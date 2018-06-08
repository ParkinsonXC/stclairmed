from django.db.models import Q


def practice_or_lookup(query):
    sql_string = (Q(name__icontains=query) |
                             Q(address__icontains=query) |
                             Q(city__icontains=query) |
                             Q(state__icontains=query) |
                             Q(zip_code__icontains=query) |
                             Q(phone_number__icontains=query)|
                             Q(website__icontains=query)
                             )
    return sql_string

def doctor_or_lookup(query):
    sql_string = (Q(first_name__icontains=query) |
                             Q(last_name__icontains=query) |
                             Q(title__icontains=query)
                             )
    return sql_string

def event_or_lookup(query):
    sql_string = (Q(title__icontains=query) |
                    Q(description__icontains=query) |
                    Q(date_of__icontains=query)
                    )
    return sql_string

def announcement_or_lookup(query):
    sql_string = (Q(title__icontains=query) |
                    Q(body__icontains=query)
                    )
    return sql_string

def newsletter_or_lookup(query):
    sql_string = (Q(month__icontains=query) |
                    Q(year__icontains=query)
                    )
    return sql_string