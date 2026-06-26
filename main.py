from kivy.app import App
from kivy.utils import platform
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Запуск фонового сервиса для Android
        if platform == 'android':
            from android.kivy_service import start_service
            start_service('myservice', 'Сервис запущен', 'Кликните для управления')
        
        return Label(text="Сервис инициализирован. Приложение можно закрыть.")

if __name__ == '__main__':
    MainApp().run()
