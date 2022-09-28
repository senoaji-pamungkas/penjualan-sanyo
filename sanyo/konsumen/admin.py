from django.contrib import admin
from konsumen.models import *
from django import forms

class KonsumenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'alamat', 'hp', 'produk_id')

admin.site.register(Konsumen, KonsumenAdmin)

class CustomModelChoiceField(forms.ModelChoiceField):
         def label_from_instance(self, obj):
             return "%s %s" % (obj.first_name, obj.last_name)

class MyProdukFormAdmin(forms.ModelForm):
    person = CustomModelChoiceField(queryset=Produk.objects.all()) 
    class Meta:
          model = Produk
          fields = '__all__'

class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id', 'jasa', 'harga')
    form: MyProdukFormAdmin

admin.site.register(Produk, ProdukAdmin)
