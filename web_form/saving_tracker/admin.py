from django.contrib import admin

import saving_tracker.models as stm


class SupportFunctionAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    SupportFunctionAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class SavingTypeAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    SavingTypeAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class HighLevelStatusAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    HighLevelStatusAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class LowLevelStatusAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    LowLevelStatusAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    GroupAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class RiskAdjustmentAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    RiskAdjustmentAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class LossesForAttackAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    LossesForAttackAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class BusinessAreaAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    BusinessAreaAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class StreamAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    StreamAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class ApprovalAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    ApprovalAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


class ProjectAdmin(admin.ModelAdmin):
    '''
    Устанавливает параметры отображения модели
    ProjectAdmin в админке.
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


admin.site.register(stm.SupportFunction, SupportFunctionAdmin)
admin.site.register(stm.SavingType, SavingTypeAdmin)
admin.site.register(stm.HighLevelStatus, HighLevelStatusAdmin)
admin.site.register(stm.LowLevelStatus, LowLevelStatusAdmin)
admin.site.register(stm.Group, GroupAdmin)
admin.site.register(stm.RiskAdjustment, RiskAdjustmentAdmin)
admin.site.register(stm.LossesForAttack, LossesForAttackAdmin)
admin.site.register(stm.BusinessArea, BusinessAreaAdmin)
admin.site.register(stm.Stream, StreamAdmin)
admin.site.register(stm.Approval, ApprovalAdmin)
admin.site.register(stm.Project, ProjectAdmin)
