from django.contrib import admin

from .models import CategoryItem, City, FoodBasket, Item, Comment, Kindsgardens, MedPrices, OpeningHours, ParksIvents, SchollRate, SpecialDays, UniversityRate


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):


    def save_model(self, request, obj, form, change):
        if not change: # Проверяем что запись только создаётся
            obj.author = request.user # Присваеваем полю автор пользователя
    
        super(ItemAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )


admin.site.register(CategoryItem)
admin.site.register(City)
admin.site.register(Comment)
admin.site.register(OpeningHours)
admin.site.register(SpecialDays)
admin.site.register(FoodBasket)
admin.site.register(MedPrices)
admin.site.register(ParksIvents)
admin.site.register(Kindsgardens)
admin.site.register(SchollRate)
admin.site.register(UniversityRate)
