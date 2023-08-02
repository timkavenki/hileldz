'''Написати функцію яка частково приховуватиме e-mail'''

def hide_email(email):
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]

    hidden_username = username[:3] + '...' + username[-1]
рш
    domain_parts = domain.split('.')
    hidden_domain = domain_parts[0][:3] + '...' + domain_parts[-1]

    return hidden_username + '@' + hidden_domain

user_email = input("Введіть e-mail: ")
hidden_email = hide_email(user_email)
print("Прихований e-mail:", hidden_email)