from django.contrib import admin

from.models import Pergunta
admin.site.register(Pergunta)

from.models import Resposta
admin.site.register(Resposta)

from.models import Categoria
admin.site.register(Categoria)

from.models import Usuario
admin.site.register(Usuario)