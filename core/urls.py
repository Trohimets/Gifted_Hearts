from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings

import feedback.views as feedback
import company.views as company
import event.views as event
import news.views as news
import documents.views as documents
import projects.views as projects
import command.views as command
import friends.views as friends
import help_translation.views as help_translation
from recaptcha.views import VerifyCaptcha
from forms_api.urls import router as router_form

admin.site.site_header = "Администрирование сайта"
admin.site.site_title = "Администрирование сайта"
admin.site.index_title = "Добро пожаловать!"

router = DefaultRouter()

router.register('feedback', feedback.FeedbackView)
router.register('company', company.CompanyView)
router.register('event', event.EventView)
router.register('news', news.NewsModelViewSet)
router.register('documents', documents.DocumentViewSet)
router.register('projects', projects.ProjectViewSet)
router.register('command', command.CommandViewSet)
router.register('friends', friends.FriendsView)
router.register('help_translation', help_translation.HelpTranlationView)
router.register('autopay_delete', help_translation.AutoPayView)

schema_view = get_schema_view(
    openapi.Info(
        title='',
        default_version='v1',
        description='',
        contact=openapi.Contact(email=''),
        license=openapi.License(name='MIT')
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # Recaptcha
    path('api/recaptcha/', VerifyCaptcha.as_view()),
    # Docs
    path('docs/', schema_view.with_ui('swagger')),
    path('docs<str:format>', schema_view.without_ui()),
    path('swagger.json', schema_view.without_ui(), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('forms_api/', include(router_form.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
