from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group

class RBACNegativeTests(APITestCase):
    def setUp(self):
        # Create Engineer user
        self.engineer_user = User.objects.create_user(username='engineer1', password='password123')
        eng_group = Group.objects.create(name='Engineer')
        self.engineer_user.groups.add(eng_group)
        
        self.url = reverse('supervisor-review-endpoint', kwargs={'result_id': 1})

    def test_engineer_cannot_access_supervisor_review(self):
        self.client.force_authenticate(user=self.engineer_user)
        response = self.client.post(self.url, {'confirmed': True})
        # Verify strict negative test constraint
        self.assertEqual(response.status_code, 403)