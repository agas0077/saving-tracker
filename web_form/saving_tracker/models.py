# Third Party Library
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()

DATE_FIELDS = (
    "initial_start_date",
    "planned_start_date",
    "project_end_date",
)

PROJECT_NAME = "Проект"
PROJECT_OWNER_NAME = "Владелец"
PROJECT_COORDINATOR_NAME = "Координатор"
SUPPORT_FUNCTION_NAME = "Функция"
SAVING_TYPE_NAME = "Тип экономии"
HIGH_LEVEL_STATUS_NAME = "Статус высокого уровня"
LOW_LEVEL_STATUS_NAME = "Статус низкого уровня"
GROUP_NAME = "Группа"
RISK_ADJUSTMENT_NAME = "Уровень риска"
LOSSES_FOR_ATTACK_NAME = "Тип потери"
BUSINESS_AREA_NAME = "Бизнес сегмент"
STREAM_NAME = "Направление"
APPROVAL_NAME = "Согласующий"
INITIAL_START_DATE_NAME = "Начало"
PLANNED_STARRT_DATE_NAME = "Плановое начало"
PROJECT_END_DATE_NAME = "Окончание"
SAVING_POTENTIAL_NAME = "Экономия, kE"
BUDGET_NAME = "Бюджет"
APPROVED_NAME = "Согласовано"
LOCAL_FOCUS_NAME = "Фокусный проект"
FOLDER_URL_NAME = "Ссылка на проект"
SRS_NUMBER_NAME = "SRS"
PRIMARY_SHARE_NAME = "Primary, %"
SECONDARY_SHARE_NAME = "Secondary, %"
WAREHOUSE_SHARE_NAME = "Warehouse, %"
PERSONAL_CARE_SHARE_NAME = "Personal Care, %"
HOME_CARE_SHARE_NAME = "Home Care, %"
TEA_SHARE_NAME = "Tea, %"
FOOD_SHARE_NAME = "Food, %"
IC_SHARE_NAME = "IC, %"
SHARE_2020_NAME = "2020, kE"
SHARE_2021_NAME = "2021, kE"
SHARE_2022_NAME = "2022, kE"
SHARE_2023_NAME = "2023, kE"
SHARE_2024_NAME = "2024, kE"
SHARE_2025_NAME = "2025, kE"
SHARE_2026_NAME = "2026, kE"
SHARE_2027_NAME = "2027, kE"


class SupportFunction(models.Model):
    """Модель-список бизнес функций."""

    title = models.CharField(
        SUPPORT_FUNCTION_NAME, max_length=100, unique=True
    )

    def __str__(self):
        return self.title


class SavingType(models.Model):
    """Модель-список типов экономии."""

    title = models.CharField(SAVING_TYPE_NAME, max_length=100, unique=True)

    def __str__(self):
        return self.title


class HighLevelStatus(models.Model):
    """Модель-список статусов высокого уровня."""

    title = models.CharField(
        HIGH_LEVEL_STATUS_NAME, max_length=100, unique=True
    )

    def __str__(self):
        return self.title


class LowLevelStatus(models.Model):
    """Модель-список статусов низкого уровня."""

    title = models.CharField(
        LOW_LEVEL_STATUS_NAME, max_length=100, unique=True
    )

    def __str__(self):
        return self.title


class Group(models.Model):
    """Модель-список групп."""

    title = models.CharField(GROUP_NAME, max_length=100, unique=True)

    def __str__(self):
        return self.title


class RiskAdjustment(models.Model):
    """Модель-список уровней риска."""

    title = models.CharField(RISK_ADJUSTMENT_NAME, max_length=20, unique=True)

    def __str__(self):
        return self.title


class LossesForAttack(models.Model):
    """Модель-список типов потерь."""

    title = models.CharField(
        LOSSES_FOR_ATTACK_NAME, max_length=100, unique=True
    )

    def __str__(self):
        return self.title


class BusinessArea(models.Model):
    """Модель-список бизнес сегментов."""

    title = models.CharField(BUSINESS_AREA_NAME, max_length=20, unique=True)

    def __str__(self):
        return self.title


class Stream(models.Model):
    """Модель-список направлений."""

    title = models.CharField(STREAM_NAME, max_length=20, unique=True)

    def __str__(self):
        return self.title


class Approval(models.Model):
    """Модель-список пока непонятно чего"""  # TODO: заполнить в readme

    title = models.CharField(APPROVAL_NAME, max_length=20, unique=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    """Основная модель приложения. Хранит информацию о каждом проекте."""

    title = models.CharField(PROJECT_NAME, max_length=200)
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="project_owner",
        verbose_name=PROJECT_OWNER_NAME,
    )
    support_function = models.ForeignKey(
        SupportFunction,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=SUPPORT_FUNCTION_NAME,
    )

    initial_start_date = models.DateField(INITIAL_START_DATE_NAME)
    planned_start_date = models.DateField(PLANNED_STARRT_DATE_NAME)
    project_end_date = models.DateField(PROJECT_END_DATE_NAME)
    saving_potential = models.FloatField(SAVING_POTENTIAL_NAME)

    saving_type = models.ForeignKey(
        SavingType,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=SAVING_TYPE_NAME,
    )
    high_level_status = models.ForeignKey(
        HighLevelStatus,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=HIGH_LEVEL_STATUS_NAME,
    )
    low_level_status = models.ForeignKey(
        LowLevelStatus,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=LOW_LEVEL_STATUS_NAME,
    )
    comment = models.TextField("Комментарий", blank=True, null=True)
    coordinator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="project_coordinator",
        verbose_name=PROJECT_COORDINATOR_NAME,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=GROUP_NAME,
    )
    risk_adjustment = models.ForeignKey(
        RiskAdjustment,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=RISK_ADJUSTMENT_NAME,
    )
    budget_use = models.BooleanField(BUDGET_NAME)
    approved = models.BooleanField(APPROVED_NAME)
    losses_for_attack = models.ForeignKey(
        LossesForAttack,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=LOSSES_FOR_ATTACK_NAME,
    )
    business_area = models.ForeignKey(
        BusinessArea,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=BUSINESS_AREA_NAME,
    )
    stream = models.ForeignKey(
        Stream,
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=STREAM_NAME,
    )
    local_focus = models.BooleanField(LOCAL_FOCUS_NAME)
    srs_number = models.CharField(
        SRS_NUMBER_NAME, max_length=20, blank=True, null=True
    )
    # TODO: approvers
    folder_url = models.URLField(FOLDER_URL_NAME, blank=True, null=True)

    primary_share = models.FloatField(
        PRIMARY_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=1,
    )

    secondary_share = models.FloatField(
        SECONDARY_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    warehouse_share = models.FloatField(
        WAREHOUSE_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    personal_care_share = models.FloatField(
        PERSONAL_CARE_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=1,
    )

    home_care_share = models.FloatField(
        HOME_CARE_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    tea_share = models.FloatField(
        TEA_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    food_share = models.FloatField(
        FOOD_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    ic_share = models.FloatField(
        IC_SHARE_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    share_2020 = models.FloatField(
        SHARE_2020_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    share_2021 = models.FloatField(
        SHARE_2021_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )
    share_2022 = models.FloatField(
        SHARE_2022_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )
    share_2023 = models.FloatField(
        SHARE_2023_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=1,
    )
    share_2024 = models.FloatField(
        SHARE_2024_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )
    share_2025 = models.FloatField(
        SHARE_2025_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )
    share_2026 = models.FloatField(
        SHARE_2026_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )
    share_2027 = models.FloatField(
        SHARE_2027_NAME,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0,
    )

    def __str__(self):
        return self.title
