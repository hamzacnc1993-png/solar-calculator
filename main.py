from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SolarCalculatorApp(App):
 
  def build(self):
    self.title = "حاسبة أداء الطاقة الشمسية"
    layout = BoxLayout(
        orientation="vertical", padding=30, spacing=15, pos_hint={"center_x": 0.5}
    )

    # عنوان التطبيق
    title_label = Label(
        text="حاسبة معامل الأداء (PR)",
        font_size=22,
        color=(0.1, 0.5, 0.8, 1),
        size_hint_y=None,
        height=40,
    )

    # حقول الإدخال
    self.cap_input = TextInput(
        hint_text="القدرة الاسمية (MW)",
        multiline=False,
        input_type="number",
        size_hint_y=None,
        height=50,
    )
    self.energy_input = TextInput(
        hint_text="الطاقة المنتجة (MWh)",
        multiline=False,
        input_type="number",
        size_hint_y=None,
        height=50,
    )
    self.irr_input = TextInput(
        hint_text="الإشعاع الشمسي (MJ/m²)",
        multiline=False,
        input_type="number",
        size_hint_y=None,
        height=50,
    )

    # زر الحساب
    calc_btn = Button(
        text="حساب النتيجة",
        background_color=(0.1, 0.6, 0.9, 1),
        font_size=18,
        size_hint_y=None,
        height=50,
    )
    calc_btn.bind(on_press=self.calculate)

    # حقل عرض النتيجة
    self.result_label = Label(
        text="أدخل البيانات واضغط حساب",
        font_size=16,
        color=(0.2, 0.2, 0.2, 1),
        size_hint_y=None,
        height=80,
    )

    # إضافة العناصر للشاشة
    layout.add_widget(title_label)
    layout.add_widget(self.cap_input)
    layout.add_widget(self.energy_input)
    layout.add_widget(self.irr_input)
    layout.add_widget(calc_btn)
    layout.add_widget(self.result_label)

    return layout

  def calculate(self, instance):
    try:
      p_nom = float(self.cap_input.text)
      energy = float(self.energy_input.text)
      irr_mj = float(self.irr_input.text)

      if p_nom <= 0 or energy < 0 or irr_mj < 0:
        self.result_label.text = "خطأ: القيم يجب ألا تكون سالبة أو صفراً للقدرة!"
        return

      # التحويلات والحسابات
      p_nom_kw = p_nom * 1000
      energy_kwh = energy * 1000
      irr_kwh = irr_mj / 3.6

      yf = energy_kwh / p_nom_kw
      yr = irr_kwh / 1.0

      if yr == 0:
        self.result_label.text = "خطأ: الإشعاع لا يمكن أن يكون صفراً!"
        return

      pr = (yf / yr) * 100
      self.result_label.text = (
          f"الإشعاع بعد التحويل: {irr_kwh:,.2f} kWh/m²\nمعامل الأداء الكلي (PR):"
          f" {pr:.2f}%"
      )

    except ValueError:
      self.result_label.text = "الرجاء إدخال أرقام صحيحة في جميع الحقول!"


if __name__ == "__main__":
  SolarCalculatorApp().run()
