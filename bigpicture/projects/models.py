from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        "Імейл",
        unique=True,
        error_messages={"unique": "Користувач з таким імейлом вже існує"},
    )
    username = models.CharField("Юзернейм", max_length=150, blank=True)

    first_name = models.CharField("Ім'я", max_length=30)
    last_name = models.CharField("Прізвище", max_length=150, blank=True)
    phone = models.CharField("Телефон", max_length=30, default="", blank=True)
    avatar = models.ImageField(max_length=200, blank=True)

    @property
    def full_name(self):
        res = f"{self.first_name} {self.last_name}"
        if not res.strip():
            res = f"{self.username} <{self.email}>"

        return res

    def __str__(self):
        return self.full_name

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"

    class Meta():
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class Department(models.Model):
    name = models.CharField("Назва департаменту", max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField("Картинка", max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменти"


class System(models.Model):
    name = models.CharField("Назва системи", max_length=200)
    description = models.TextField("Опис", blank=True)
    slug = models.SlugField(max_length=200)
    departments = models.ManyToManyField(Department, verbose_name="Департаменти")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Система"
        verbose_name_plural = "Системи"


class Project(models.Model):
    KINDS = {"it": "IT-проект", "legislative": "Підзаконні акти"}

    system = models.ForeignKey(System, verbose_name="Система", on_delete=models.CASCADE)
    name = models.CharField("Назва проєкту", max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField("Опис проєкту", blank=True)
    kind = models.CharField("Тип проєкту", max_length=20, choices=KINDS.items())
    responsible_persons = models.ManyToManyField(User, verbose_name="Відповідальні")
    departments = models.ManyToManyField(Department, verbose_name="Департаменти")
    image = models.ImageField("Картинка", max_length=200, blank=True)
    deadline = models.DateField("Дедлайн", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Проєкт"
        verbose_name_plural = "Проєкти"
