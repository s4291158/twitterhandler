from django.contrib import admin
from django.apps import apps

app = apps.get_app_config("api")

for model_name, model in app.models.items():
    exclude = []
    if model_name not in exclude:
        admin.site.register(model)
