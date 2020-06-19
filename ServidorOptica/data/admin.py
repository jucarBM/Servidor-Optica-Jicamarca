from django.contrib import admin

# Models
from django.contrib.auth.models import User
from data.models import Station, Instrument, Experiment, InstrumentModel, InstrumentCharacteristic, Product, Setting

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    pass

@admin.register(InstrumentModel)
class InstrumentModelAdmin(admin.ModelAdmin):
    pass

@admin.register(InstrumentCharacteristic)
class InstrumentCharacteristicAdmin(admin.ModelAdmin):

    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    pass

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    pass