from django.contrib import admin

import saving_tracker.models as stm


class BaseAdmin(admin.ModelAdmin):
    '''
    Устанавливает базовые параметры отображения админки
    '''
    list_display = ('title', 'pk')
    empty_value_display = '-пусто-'


admin.site.register(stm.SupportFunction, BaseAdmin)
admin.site.register(stm.SavingType, BaseAdmin)
admin.site.register(stm.HighLevelStatus, BaseAdmin)
admin.site.register(stm.LowLevelStatus, BaseAdmin)
admin.site.register(stm.Group, BaseAdmin)
admin.site.register(stm.RiskAdjustment, BaseAdmin)
admin.site.register(stm.LossesForAttack, BaseAdmin)
admin.site.register(stm.BusinessArea, BaseAdmin)
admin.site.register(stm.Stream, BaseAdmin)
admin.site.register(stm.Approval, BaseAdmin)
admin.site.register(stm.Project, BaseAdmin)
