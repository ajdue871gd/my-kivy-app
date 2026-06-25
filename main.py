from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


class PeriodicApp(App):

    def build(self):
        # Главный контейнер
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Информационный текст
        self.label = Label(
            text="Приложение запущено.\nОжидание таймера...",
            font_size="20sp",
            halign="center",
        )
        self.layout.add_widget(self.label)

        # Виджет для отображения GIF (изначально пустой и скрытый)
        self.gif_widget = Image(keep_ratio=True, allow_stretch=True)

        # Кнопка для ручного теста / запуска
        self.btn = Button(
            text="Запустить цикл (каждые 30 сек)",
            size_hint=(1, 0.2),
            on_press=self.start_timer,
        )
        self.layout.add_widget(self.btn)

        # Переменные для звука и состояния
        self.sound = SoundLoader.load("audio.mp3")
        self.is_playing = False

        return self.layout

    def start_timer(self, instance):
        self.btn.disabled = True
        self.label.text = "Цикл активирован.\nПервый запуск через 30 секунд."
        # Запуск периодического таймера (30 секунд). Измените значение при необходимости.
        Clock.schedule_interval(self.trigger_media, 30)

    def trigger_media(self, dt):
        if not self.is_playing:
            self.is_playing = True
            self.label.text = "Воспроизведение медиа!"

            # Показываем GIF
            self.gif_widget.source = "animation.gif"
            # Перезапускаем анимацию GIF
            self.gif_widget.anim_delay = 0.10
            if self.gif_widget not in self.layout.children:
                # Вставляем GIF над кнопкой
                self.layout.add_widget(self.gif_widget, index=1)

            # Включаем звук
            if self.sound:
                self.sound.play()

            # Выключаем медиа через 10 секунд (длительность показа)
            Clock.schedule_once(self.stop_media, 10)

    def stop_media(self, dt):
        # Останавливаем звук
        if self.sound:
            self.sound.stop()

        # Прячем GIF
        if self.gif_widget in self.layout.children:
            self.layout.remove_widget(self.gif_widget)

        self.label.text = "Ожидание следующего запуска..."
        self.is_playing = False


if __name__ == "__main__":
    PeriodicApp().run()