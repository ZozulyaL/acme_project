from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
# Импортируем модель дней рождения.
from .models import Birthday

# def birthday(request):
#      # Создаём экземпляр класса формы.
#     # Если есть GET-параметры — передаём их в форму:
#     form = BirthdayForm(request.GET or None)
#      # Форму с переданным в неё объектом request.GET 
#     # записываем в словарь контекста...
#     if form.is_valid():
#         pass
#     # Добавляем его в словарь контекста под ключом form:
#     context = {'form': form}
#     # Указываем нужный шаблон и передаём в него словарь контекста.
#     return render(request, 'birthday/birthday.html', context=context)
#тема обработка данных из веб формы
def birthday(request):
    form = BirthdayForm(request.POST or None)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если форма валидна...
    if form.is_valid():
        form.save()
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context) 

def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context) 
    