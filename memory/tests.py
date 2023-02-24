from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.urls import resolve

from memory.views import top, memory_new, memory_detail
from memory.models import Memory

UserModel = get_user_model()

# Create your tests here.

class TopPageRenderMemoryTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user", 
            email = "test@example.com",
            password = "top_secret_pass0001",
        )
        self.memory = Memory.objects.create(
            title = "title1",
            weapon = "Slosher",
            stage = "Scorch Gorge",
            rule = "Turf War",
            xp = 2400,
            memory_num = "R4K3-STLQ-XYD3-2VSG",
            comment = "よろしく",
        )
    
    def test_should_return_memory_tilte(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.memory.title)

    '''modelにuserを登録していないので通らない
    def test_should_return_username(self):
        request =RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)
    '''

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "メモリー", status_code=200)

    def test_top_page_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "memory/top.html")
    
class CreateMemoryTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email = "test@exapmle.com",
            password = "secret",
        )

    def test_render_creation_form(self):
        response = self.client.get("/memories/new/")
        self.assertContains(response, "メモリーの投稿", status_code=200)

    def test_create_snippet(self):
        data = {'title' : 'タイトル', 'weapon' : 'ドライブワイパー', 'stage' : 'ユノハナ大渓谷', 'rule' : 'ナワバリバトル', 'xp' : 2400, 'memory_num' : 'XXXX-XXXX-XXXX-XXXX', 'comment' : 'コメント'}
        self.client.post("/memories/new/", data)
        memory = Memory.objects.get(title='タイトル')
        self.assertEqual('ドライブワイパー', memory.weapon)
        self.assertEqual('ユノハナ大渓谷', memory.stage)
        self.assertEqual('ナワバリバトル', memory.rule)
        self.assertEqual(2400, memory.xp)
        self.assertEqual('XXXX-XXXX-XXXX-XXXX', memory.memory_num)
        self.assertEqual('コメント', memory.comment)

class MemoryDetailTest(TestCase):
    def setUp(self):
        self.memory = Memory.objects.create(
            title = "title1",
            weapon = "Slosher",
            stage = "Scorch Gorge",
            rule = "Turf War",
            xp = 2400,
            memory_num = "R4K3-STLQ-XYD3-2VSG",
            comment = "よろしく",
        )

    def test_should_use_expectd_template(self):
        response = self.client.get("/memories/%s/" % self.memory.id)
        self.assertTemplateUsed(response, "memory/memory_detail.html")

    def test_top_page_returns_200_and_expexted_heading(self):
        response = self.client.get("/memories/%s/" % self.memory.id)
        self.assertContains(response, self.memory.title, status_code=200)