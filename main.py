from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from random import choice

# مشاهد اللعبة بصيغة مبسطة
SCENES = {
    'start': {
        'text': 'تفتح عينيك في غرفة مظلمة. هناك باب واحد أمامك ونور خافت من فتحة تحت الباب.',
        'choices': [('اقترب من الباب', 'door'), ('ابحث في الغرفة', 'search')]
    },
    'search': {
        'text': 'تلمس الطاولة القديمة وتجد مذكرات ممزقة. تسمع صوت خطوات بعيدة... هل تستمر؟',
        'choices': [('اجلس وأقرأ المذكرات', 'read'), ('تختبئ', 'hide')]
    },
    'door': {
        'text': 'اليد على المقبض ببطء. الباب مغلق بالقفل. تسمع نفس الهمهمة من الخارج.',
        'choices': [('أدق الباب بقوة', 'knock'), ('تعود للغرفة', 'start')]
    },
    'read': {
        'text': 'المذكرات تحكي عن ضيف لم يغادر. فجأة ينطفئ الضوء. شعرت بنسمة باردة... النهاية؟',
        'choices': [('أعد تشغيل اللعبة', 'start')]
    },
    'hide': {
        'text': 'تختبئ تحت السرير. تمر خطوة واحدة بجانب السرير... ثم تذهب. نجوت... مؤقتًا.',
        'choices': [('تخرج ببطء', 'door'), ('تنتهي اللعبة هنا', 'end')]
    },
    'knock': {
        'text': 'بعد طرقك، صمت طويل ثم همسة "لا تغادر". الباب يفتح من تلقاء نفسه... النهاية؟',
        'choices': [('ادخل', 'end'), ('تهرب', 'start')]
    },
    'end': {
        'text': 'انتهت التجربة. شكراً للعب — يمكنك إعادة التشغيل للبحث عن نهايات أخرى.',
        'choices': [('إعادة التشغيل', 'start')]
    }
}

class HorrorGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.label = Label(text='', font_size='20sp', halign='right', valign='middle')
        self.label.bind(size=self._update_text_size)
        self.add_widget(self.label)

        self.buttons_box = BoxLayout(size_hint_y=None, height='120dp', spacing=10)
        self.add_widget(self.buttons_box)

        self.sound = None
        self.play_ambient()

        self.current = 'start'
        Clock.schedule_once(lambda dt: self.show_scene(self.current), 0.1)

    def _update_text_size(self, *args):
        self.label.text_size = (self.label.width, None)

    def play_ambient(self):
        try:
            self.sound = SoundLoader.load('sounds/ambient.ogg')
            if self.sound:
                self.sound.loop = True
                self.sound.play()
        except Exception:
            pass

    def show_scene(self, scene_id):
        scene = SCENES.get(scene_id)
        if not scene:
            return
        self.current = scene_id
        self.label.text = '\n' + scene['text']
        self.buttons_box.clear_widgets()
        for (text, target) in scene['choices']:
            b = Button(text=text, font_size='18sp')
            b.bind(on_release=lambda btn, t=target: self.on_choice(t))
            self.buttons_box.add_widget(b)

    def on_choice(self, target):
        # تأثير صوتي عند الاختيار إن وُجد
        try:
            s = SoundLoader.load('sounds/creak.ogg')
            if s:
                s.play()
        except Exception:
            pass
        Clock.schedule_once(lambda dt: self.show_scene(target), 0.2)

class HorrorApp(App):
    def build(self):
        self.title = 'لعبة الرعب'
        return HorrorGame()

if __name__ == '__main__':
    HorrorApp().run()
