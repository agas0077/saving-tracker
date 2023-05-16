from django import forms


from saving_tracker.models import (Project, LOCAL_FOCUS_NAME, BUDGET_NAME,
                                   PRIMARY_SHARE_NAME, SECONDARY_SHARE_NAME,
                                   WAREHOUSE_SHARE_NAME, APPROVED_NAME,
                                   PERSONAL_CARE_SHARE_NAME,
                                   HOME_CARE_SHARE_NAME, TEA_SHARE_NAME,
                                   FOOD_SHARE_NAME, IC_SHARE_NAME,
                                   SHARE_2020_NAME, SHARE_2021_NAME,
                                   SHARE_2022_NAME, SHARE_2023_NAME,
                                   SHARE_2024_NAME, SHARE_2025_NAME,
                                   SHARE_2026_NAME, SHARE_2027_NAME)


class ProjectForm(forms.ModelForm):
    '''
    Форма создания и редактирования проекта.
    '''
    local_focus = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input me-2'}),
        required=False,
        label=LOCAL_FOCUS_NAME,
        label_suffix='')

    budget_use = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input me-2'}),
        required=False,
        label=BUDGET_NAME,
        label_suffix='')

    approved = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input me-2'}),
        required=False,
        label=APPROVED_NAME,
        label_suffix='')

    class Meta:
        model = Project
        fields = ('__all__')

    def clean_initial_start_date(self):
        '''
        Проверяет поле initial_start_date на нахождение в нужном диапазоне.
        '''
        date = self.cleaned_data['initial_start_date']
        if date.year < 2020 or date.year > 2027:
            raise forms.ValidationError(
                'Год должен быть между 2020 и 2027')
        return date

    def clean_planned_start_date(self):
        '''
        Проверяет поле planned_start_date на нахождение в нужном диапазоне.
        '''
        date = self.cleaned_data['planned_start_date']
        if date.year < 2020 or date.year > 2027:
            raise forms.ValidationError(
                'Год должен быть между 2020 и 2027')
        return date

    def clean_project_end_date(self):
        '''
        Проверяет поле project_end_date на нахождение в нужном диапазоне.
        '''
        date = self.cleaned_data['project_end_date']
        if date.year < 2020 or date.year > 2027:
            raise forms.ValidationError(
                'Год должен быть между 2020 и 2027')
        return date

    def clean(self):
        '''
        Совершает следующие проверки:
        - сумма в полях primary, secondary, warehouse равна 1;
        - сумма в полях категорий равна 1;
        - сумма в полях годов равна 1;
        - нельзя перевести проект с экономией >= 40 kE в статус Done
        без согласования.
        '''
        cleaned_data = super().clean()
        set_1 = (
            (PRIMARY_SHARE_NAME, cleaned_data.get('primary_share', 0)),
            (SECONDARY_SHARE_NAME, cleaned_data.get('secondary_share', 0)),
            (WAREHOUSE_SHARE_NAME, cleaned_data.get('warehouse_share', 0)),
        )
        set_2 = (
            (PERSONAL_CARE_SHARE_NAME,
             cleaned_data.get('personal_care_share', 0)),
            (HOME_CARE_SHARE_NAME, cleaned_data.get('home_care_share', 0)),
            (TEA_SHARE_NAME, cleaned_data.get('tea_share', 0)),
            (FOOD_SHARE_NAME, cleaned_data.get('food_share', 0)),
            (IC_SHARE_NAME, cleaned_data.get('ic_share', 0)),
        )
        set_3 = (
            (SHARE_2020_NAME, cleaned_data.get('share_2020', 0)),
            (SHARE_2021_NAME, cleaned_data.get('share_2021', 0)),
            (SHARE_2022_NAME, cleaned_data.get('share_2022', 0)),
            (SHARE_2023_NAME, cleaned_data.get('share_2023', 0)),
            (SHARE_2024_NAME, cleaned_data.get('share_2024', 0)),
            (SHARE_2025_NAME, cleaned_data.get('share_2025', 0)),
            (SHARE_2026_NAME, cleaned_data.get('share_2026', 0)),
            (SHARE_2027_NAME, cleaned_data.get('share_2027', 0)),
        )
        sum_set_1 = sum([val for name, val in set_1]) == 1
        sum_set_2 = sum([val for name, val in set_2]) == 1
        sum_set_3 = sum([val for name, val in set_3]) == 1
        if not sum_set_1:
            fields = ', '.join([name for name, val in set_1])
            self.add_error(None, forms.ValidationError(
                f'Сумма в полях {fields} должна равняться едиинице.'))

        if not sum_set_2:
            fields = ', '.join([name for name, val in set_2])
            self.add_error(None, forms.ValidationError(
                f'Сумма в полях {fields} должна равняться едиинице.'))

        if not sum_set_3:
            fields = ', '.join([name for name, val in set_3])
            self.add_error(None, forms.ValidationError(
                f'Сумма в полях {fields} должна равняться едиинице.'))

        saving_flag = cleaned_data.get('saving_potential', 0) >= 40
        status = cleaned_data.get('high_level_status', None)
        status_flag = status.title == 'Done' if status else False
        approved_flag = not cleaned_data.get('approved', False)
        if all([saving_flag, status_flag, approved_flag]):
            self.add_error(None, forms.ValidationError(
                ('Проект с экономией больше 40 kE не может быть '
                 'переведен в статус Done без согласования.')))

        return cleaned_data
