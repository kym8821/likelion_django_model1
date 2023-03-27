from django.contrib import admin
from .models import *
# .models에서 Blog를 가져옴. 차피 다 가져올거니까 Blog대신 * 써도 됨.

# Register your models here.
admin.site.register(Blog)
#admin에 Blog 등록하는듯!