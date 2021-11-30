from django.contrib import admin
from .models import Congestion_points_HJ, Congestion_points_SH, Questions, User_Account, turnover_points_HJ, turnover_points_SH

# Register your models here.

# @admin.register(User_Account)
# class user_admin(admin.ModelAdmin):
#     list_display = (
#         'email',
#         'username',
#         'date_signup',
#         'last_login',
#     )

#     list_display_links = (
#         'email',
#         'username',
#     )

admin.site.register(User_Account)

admin.site.register(Congestion_points_HJ)
admin.site.register(Congestion_points_SH)
admin.site.register(turnover_points_HJ)
admin.site.register(turnover_points_SH)

admin.site.register(Questions)
