from django.contrib import admin
from .models import Department, System, Project, User
from django.contrib.auth.admin import UserAdmin as UserAdminDefault


@admin.register(User)
class UserAdmin(UserAdminDefault):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "username")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("email", "first_name", "last_name")
    prepopulated_fields = {"username": ("first_name", "last_name")}

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def departments_readable(self, obj):
        return ", ".join(dep.name for dep in obj.departments.all())

    departments_readable.short_description = "Департаменти"

    def responsible_readable(self, obj):
        return ", ".join(user.full_name for user in obj.responsible_persons.all())

    responsible_readable.short_description = "Відповідальні особи"

    list_display = ("name", "system", "kind", "deadline", "departments_readable", "responsible_readable")
    list_filter = ("departments", "responsible_persons", "system")