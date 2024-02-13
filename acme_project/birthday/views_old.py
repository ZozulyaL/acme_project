from django.shortcuts import get_object_or_404, redirect, render
# Импортируем класс пагинатора.
#from django.core.paginator import Paginator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy


# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
# Импортируем модель дней рождения.
from .models import Birthday
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown


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
# def birthday(request, pk=None):
#     instance = get_object_or_404(Birthday, pk=pk)  
#     form = BirthdayForm(request.POST or None, instance=instance)
#     # Создаём словарь контекста сразу после инициализации формы.
#     context = {'form': form}
#     # Если форма валидна...
#     if form.is_valid():
#         form.save()
#         # ...вызовем функцию подсчёта дней:
#         birthday_countdown = calculate_birthday_countdown(
#             # ...и передаём в неё дату из словаря cleaned_data.
#             form.cleaned_data['birthday']
#         )
#         # Обновляем словарь контекста: добавляем в него новый элемент.
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context) 


# Добавим опциональный параметр pk.
# def birthday(request, pk=None):
#     # Если в запросе указан pk (если получен запрос на редактирование объекта):
#     if pk is not None:
#         # Получаем объект модели или выбрасываем 404 ошибку.
#         instance = get_object_or_404(Birthday, pk=pk)
#     # Если в запросе не указан pk
#     # (если получен запрос к странице создания записи):
#     else:
#         # Связывать форму с объектом не нужно, установим значение None.
#         instance = None
#     # Передаём в форму либо данные из запроса, либо None. 
#     # В случае редактирования прикрепляем объект модели.
#     form = BirthdayForm(request.POST or None,
#                         files=request.FILES or None,
#                         instance=instance)
#     # Остальной код без изменений.
#     context = {'form': form}
#     # Сохраняем данные, полученные из формы, и отправляем ответ:
#     if form.is_valid():
#         form.save()
#         birthday_countdown = calculate_birthday_countdown(
#             form.cleaned_data['birthday']
#         )
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context) 

#это код создания с классом

class BirthdayCreateView(CreateView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Этот класс сам может создать форму на основе модели!
    # Нет необходимости отдельно создавать форму через ModelForm.
    # Указываем поля, которые должны быть в форме:
    #fields = '__all__'
    # Указываем имя формы:
    form_class = BirthdayForm
    # Явным образом указываем шаблон:
    template_name = 'birthday/birthday.html'
    # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # после создания объекта:
    success_url = reverse_lazy('birthday:list') 

    #класс по обновление
class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list') 


# это код до пагинации
# def birthday_list(request):
#     # Получаем все объекты модели Birthday из БД.
#     birthdays = Birthday.objects.all()
#     # Передаём их в контекст шаблона.
#     context = {'birthdays': birthdays}
#     return render(request, 'birthday/birthday_list.html', context) 

#это код с пагинацией
# def birthday_list(request):
#     # Получаем список всех объектов с сортировкой по id.
#     birthdays = Birthday.objects.order_by('id')
#     # Создаём объект пагинатора с количеством 10 записей на страницу.
#     paginator = Paginator(birthdays, 5)

#     # Получаем из запроса значение параметра page.
#     page_number = request.GET.get('page')
#     # Получаем запрошенную страницу пагинатора. 
#     # Если параметра page нет в запросе или его значение не приводится к числу,
#     # вернётся первая страница.
#     page_obj = paginator.get_page(page_number)
#     # Вместо полного списка объектов передаём в контекст 
#     # объект страницы пагинатора
#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html', context) 

#это код с классом  CBV
# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 4

# def delete_birthday(request, pk):
#     # Получаем объект модели или выбрасываем 404 ошибку.
#     instance = get_object_or_404(Birthday, pk=pk)
#     # В форму передаём только объект модели;
#     # передавать в форму параметры запроса не нужно.
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     # Если был получен POST-запрос...
#     if request.method == 'POST':
#         # ...удаляем объект:
#         instance.delete()
#         # ...и переадресовываем пользователя на страницу со списком записей.
#         return redirect('birthday:list')
#     # Если был получен GET-запрос — отображаем форму.
#     return render(request, 'birthday/birthday.html', context)

class BirthdayDeleteView(DeleteView):
    model = Birthday
    #template_name = 'birthday/birthday.html' так как создали страницу удаления
    success_url = reverse_lazy('birthday:list') 


class BirthdayDetailView(DetailView):
    model = Birthday
    
    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context 