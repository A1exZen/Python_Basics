# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
# Пароль является надежным если:
# – его длина не менее 10 символов; 
# – он содержит как минимум одну заглавную букву (верхний регистр);
# – он содержит как минимум одну строчную букву (нижний регистр). 

def is_password_good(password):
  if len(password) < 10:
    return False
  
  hasUpper = any(s.isupper() for s in password )
  hasLower = any(s.islower() for s in password )
  
  return hasLower and hasUpper

password = input("Введите пароль: ")
print('Пароль надежный!' if is_password_good(password) else 'Пароль ненадежный!' )