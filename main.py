from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label

class NovaFillApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="NovaFill: Driver Wait Form Generator"))

        self.font_spinner = Spinner(
            text="Select Font",
            values=["LiebeHeide", "Viktorie", "Roboto"],
            size_hint=(1, None), height=44
        )
        layout.add_widget(self.font_spinner)

        generate_btn = Button(text="📝 Generate Wait Form PDF")
        generate_btn.bind(on_press=self.generate_pdf)
        layout.add_widget(generate_btn)

        return layout

    def generate_pdf(self, instance):
        from utils.ocr_extractor import extract_data
        from utils import pdf_filler

        data = extract_data("assets/screenshot.jpg")
        pdf_filler.fill_pdf(data, self.font_spinner.text)

if __name__ == "__main__":
    NovaFillApp().run()
