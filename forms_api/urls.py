from rest_framework.routers import DefaultRouter

from forms_api.views import (FeedBackSuggestion,
                             ApplicationsForVolunteering,
                             RegistrationForEvents, )

__all__ = [
    'router',
]

router = DefaultRouter()
router.register('feedback', FeedBackSuggestion)
router.register('volunteering', ApplicationsForVolunteering)
router.register('registration_for_events', RegistrationForEvents)
