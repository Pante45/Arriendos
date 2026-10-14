from django.contrib import admin

from .models import Arriendo, Equipo


def formato_clp(valor):
	return "$" + f"{valor:,}".replace(",", ".")


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ("nombre", "estado", "fecha_adquisicion", "valor_clp")
	list_filter = ("estado", "fecha_adquisicion")
	search_fields = ("nombre", "descripcion", "estado")
	ordering = ("nombre",)

	@admin.display(description="Valor de adquisición", ordering="valor_adquisicion")
	def valor_clp(self, obj):
		return formato_clp(obj.valor_adquisicion)


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
	list_display = ("equipo", "cliente", "fecha_inicio", "fecha_fin", "monto_clp")
	list_filter = ("equipo", "fecha_inicio", "fecha_fin")
	search_fields = ("equipo__nombre", "cliente")
	autocomplete_fields = ("equipo",)
	ordering = ("-fecha_inicio",)

	@admin.display(description="Monto", ordering="monto")
	def monto_clp(self, obj):
		return formato_clp(obj.monto)
