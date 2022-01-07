from django.contrib import admin

from polls.models import Choice, Question

# Register your models here.

# class ChoiceInline(admin.StackedInline):  #Question 및 Choice 한 화면에서 변경하기
class ChoiceInline(admin.TabularInline):    # Question 및 Choice 테이블 형식으로 보여주기
    model = Choice
    extra = 2 # 추가 개 수 지정

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] -> 필드 순서 변경
    fieldsets = [                                                                   # 각 필드 분리해서 보여주기
        (None, {'fields': ['question_text']}), 
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),    # 'classes': ['collapse'] 숨김/확장
    ]
    inlines = [ChoiceInline]    # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')    # 레코드 리스트 컬러 항목 지정
    list_filter = ['pub_date']         # 필터 사이드바 추가
    search_fields = ['question_text']  # 검색 박스 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)