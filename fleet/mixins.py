# fleet/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin

class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Sprawdza czy użytkownik jest superuserem lub jest w grupie Managers
        return self.request.user.is_staff or self.request.user.groups.filter(name='Managers').exists()

class DriverRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Drivers').exists()