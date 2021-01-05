from rest_framework import routers
from form.viewsets import FormViewSet

router = routers.DefaultRouter()

router.register(r'form', FormViewSet)
