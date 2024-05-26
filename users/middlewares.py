from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ExpClubMiddleWare(MiddlewareMixin):
    def progress_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            exp = int(request.POST.get('experience'))
            age = int(request.POST.get('age'))
            if age < 5:
                return HttpResponseBadRequest('Ваш возраст слишком мал для регистрации!!!')
            elif exp < 1:
                request.club = 'Новичок'
            elif 1 <= exp <= 2:
                request.club = 'не Новичок'
            elif 2 <= exp <= 3:
                request.club = 'Старейшина'
            elif 3 <= exp <= 5:
                request.club = 'Профи'
            elif exp > 5:
                request.club = 'Книжный гуру'
            else:
                return HttpResponseBadRequest('Извините вы не подходите для регистрации')

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'клуб не определен')