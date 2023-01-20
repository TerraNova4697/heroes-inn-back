import io
from io import BytesIO
from unittest import mock

from PIL import Image
from PIL.ImageFile import ImageFile
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Hero
from .models import Weapon


# url: 'heroes:'
class APITestCaseWithCredentials(APITestCase):

    @staticmethod
    def get_tokens_for_user(curr_user=None):
        refresh = RefreshToken.for_user(curr_user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def set_up_credentials(self):
        user = User.objects.get(pk=1)
        token = self.get_tokens_for_user(curr_user=user)['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    # Создается фейковое изображение
    @staticmethod
    def generate_test_image(image_name='test.jpeg', color=(155, 0, 0)):
        file = io.BytesIO()
        image = Image.new('RGB', size=(300, 300), color=color)
        image.save(file, 'jpeg')
        file.name = image_name
        return file


# url: 'heroes:heroes_list'
class HeroesTests(APITestCaseWithCredentials):

    def setUp(self) -> None:
        user = User.objects.create_user(username='Nikita', email='nikita@test.com', password='9bb7bfe4')
        user2 = User.objects.create_user(username='Olga', email='olga@test.com', password='9bb7bfe4')

        Hero.objects.create(name='Руди', owner=user, heroes_class='Варвар')
        Hero.objects.create(name='Инга', owner=user2, heroes_class='Жрец')
        Hero.objects.create(name='Феликс', owner=user, heroes_class='Колдун')
        Hero.objects.create(name='Ричмонд', owner=user2, heroes_class='Следопыт')
        Hero.objects.create(name='Ева', owner=user, heroes_class='Следопыт')

    def test_get_heroes(self):
        self.set_up_credentials()
        response = self.client.get(reverse('heroes:heroes_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_heroes_fail_401(self):
        response = self.client.get(reverse('heroes:heroes_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# url: 'heroes:weapons'
class WeaponTests(APITestCase):

    def setUp(self) -> None:
        weapon1 = Weapon.objects.create(name='Длинный меч', price='20зм', damage='1к6', type_of_damage='Рубящий')
        weapon2 = Weapon.objects.create(name='Дубинка', price='1см', damage='1к6', type_of_damage='Дробящий')
        weapon3 = Weapon.objects.create(name='Булава', price='2зм', damage='1к6', type_of_damage='Дробящий')
        weapon4 = Weapon.objects.create(name='Копье', price='2зм', damage='1к6', type_of_damage='Колющий')
        weapon5 = Weapon.objects.create(name='Арбалет', price='50зм', damage='1к6', type_of_damage='Колющий')

    def test_get_weapon(self):
        response = self.client.get(reverse('heroes:weapons'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)


# url: 'heroes:create_hero'
class CreateHeroTests(APITestCaseWithCredentials):

    def setUp(self) -> None:
        user = User.objects.create_user(username='Nikita', email='nikita@test.com', password='9bb7bfe4')

    def test_create_hero(self):
        self.set_up_credentials()
        url = reverse('heroes:create_hero')
        data = {'name': 'Руди', 'owner': 1, 'heroes_class': 'Варвар'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hero.objects.count(), 1)
        self.assertEqual(Hero.objects.get().name, 'Руди')

    def test_create_hero_fail_401(self):
        url = reverse('heroes:create_hero')
        data = {'name': 'Феликс', 'owner': 1, 'heroes_class': 'Варвар'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# url: 'heroes:get_hero'
class GetHeroTests(APITestCaseWithCredentials):

    def setUp(self) -> None:
        user = User.objects.create_user(username='Nikita', email='nikita@test.com', password='9bb7bfe4')
        user2 = User.objects.create_user(username='Olga', email='olga@test.com', password='9bb7bfe4')

        Hero.objects.create(name='Руди', owner=user, heroes_class='Варвар')
        Hero.objects.create(name='Инга', owner=user2, heroes_class='Жрец')
        Hero.objects.create(name='Феликс', owner=user, heroes_class='Колдун')
        Hero.objects.create(name='Ричмонд', owner=user2, heroes_class='Следопыт')
        Hero.objects.create(name='Ева', owner=user, heroes_class='Следопыт')

    def test_get_hero(self):
        self.set_up_credentials()
        url = reverse('heroes:get_hero', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Руди')

    def test_get_hero_fail_403(self):
        self.set_up_credentials()
        url = reverse('heroes:get_hero', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_hero_fail_401(self):
        url = reverse('heroes:get_hero', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# url: 'heroes:image_upload'
class ImageLoadTests(APITestCaseWithCredentials):

    # Создаем тестовое изображение. Оно нужно для передачи в качестве "старого изображения, которое будет удалено
    def setUp(self) -> None:
        file = self.generate_test_image()
        default_storage.save(file.name, file)

    # Создаем изображение и отправляем его на бекенд в качестве нового. Также отправляем путь к станому изображению,
    # которое уже было создано в setUP()
    def test_load_image(self):
        file = self.generate_test_image()
        data = { 'image': file, 'old_image': '/test.jpeg' }
        response = self.client.post(reverse('heroes:image_upload'), data)
        image_name = response.data['imageURL'].split('/')[-1]
        self.assertEqual(default_storage.exists(image_name), True)
        self.assertEqual(default_storage.exists('test.jpeg'), False)
        default_storage.delete(image_name)


# url: 'heroes:delete_hero'
class DeleteHeroTests(APITestCaseWithCredentials):

    def setUp(self) -> None:
        user = User.objects.create_user(username='Nikita', email='nikita@test.com', password='9bb7bfe4')
        user2 = User.objects.create_user(username='Olga', email='olga@test.com', password='9bb7bfe4')

        if not default_storage.exists('test.jpeg'):
            file = self.generate_test_image()
            default_storage.save(file.name, file)

        Hero.objects.create(name='Руди', owner=user, heroes_class='Варвар')
        Hero.objects.create(name='Инга', owner=user2, heroes_class='Жрец')
        Hero.objects.create(name='Феликс', owner=user, heroes_class='Колдун', hero_img='/default-hero-img.jpg')
        Hero.objects.create(name='Ричмонд', owner=user2, heroes_class='Следопыт')
        Hero.objects.create(name='Ева', owner=user, heroes_class='Следопыт', hero_img='/test.jpeg')

    def test_delete_hero_no_image(self):
        self.set_up_credentials()
        url = reverse('heroes:delete_hero', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_hero_with_default_image(self):
        self.set_up_credentials()
        url = reverse('heroes:delete_hero', kwargs={'pk': 3})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_hero_with_image(self):
        self.set_up_credentials()
        url = reverse('heroes:delete_hero', kwargs={'pk': 5})
        response = self.client.delete(url)
        self.assertEqual(default_storage.exists(r'test*' + '.jpeg'), False)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_hero_fail_403(self):
        self.set_up_credentials()
        url = reverse('heroes:delete_hero', kwargs={'pk': 2})
        response = self.client.delete(url)
        hero = Hero.objects.filter(pk=2).get()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(hero.name, 'Инга')

    def test_delete_hero_fail_401(self):
        url = reverse('heroes:delete_hero', kwargs={'pk': 2})
        response = self.client.delete(url)
        hero = Hero.objects.filter(pk=2).get()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(hero.name, 'Инга')


# url: 'heroes:update_hero'
class UpdateHeroTest(APITestCaseWithCredentials):

    def setUp(self) -> None:
        user = User.objects.create_user(username='Nikita', email='nikita@test.com', password='9bb7bfe4')
        user2 = User.objects.create_user(username='Olga', email='olga@test.com', password='9bb7bfe4')

        if not default_storage.exists('test.jpeg'):
            file = self.generate_test_image()
            default_storage.save(file.name, file)

        Hero.objects.create(name='Руди', owner=user, heroes_class='Варвар')
        Hero.objects.create(name='Инга', owner=user2, heroes_class='Жрец')
        Hero.objects.create(name='Феликс', owner=user, heroes_class='Колдун', hero_img='/default-hero-img.jpg')
        Hero.objects.create(name='Ричмонд', owner=user2, heroes_class='Следопыт')
        Hero.objects.create(name='Ева', owner=user, heroes_class='Следопыт', hero_img='/test.jpeg')

    def test_update_heroes_background(self):
        self.set_up_credentials()
        data = {'background': 'Отшельник'}
        url = reverse('heroes:update_hero', kwargs={'pk': 1})
        response = self.client.patch(url, data=data)
        hero = Hero.objects.filter(pk=1).get()
        self.assertEqual(hero.background, 'Отшельник')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        default_storage.delete('test.jpeg')

    def test_update_heroes_image(self):
        self.set_up_credentials()

        # Создаем изображение, которым будем обновлять старое. В этом же тесте удалим его
        file = self.generate_test_image('new_test.jpeg', (0, 155, 0))
        default_storage.save(file.name, file)

        data = {'hero_img': '/new_test.jpeg'}
        url = reverse('heroes:update_hero', kwargs={'pk': 1})
        response = self.client.patch(url, data=data)
        hero = Hero.objects.filter(pk=1).get()

        # Удаляем изображение созданное для теста
        default_storage.delete('new_test.jpeg')
        default_storage.delete('test.jpeg')

        self.assertEqual(hero.hero_img, '/new_test.jpeg')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_heroes_background_fail_403(self):
        self.set_up_credentials()
        data = {'background': 'Отшельник'}
        url = reverse('heroes:update_hero', kwargs={'pk': 2})
        response = self.client.patch(url, data=data)
        hero = Hero.objects.filter(pk=2).get()
        self.assertNotEqual(hero.background, 'Отшельник')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        default_storage.delete('test.jpeg')

    def test_update_heroes_background_fail_402(self):
        data = {'background': 'Отшельник'}
        url = reverse('heroes:update_hero', kwargs={'pk': 2})
        response = self.client.patch(url, data=data)
        hero = Hero.objects.filter(pk=2).get()
        self.assertNotEqual(hero.background, 'Отшельник')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        default_storage.delete('test.jpeg')

