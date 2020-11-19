class Contact:
    """Класс, описывающий атрибуты для метода create_contact"""
    def __init__(self, name="valery", last_name="sumbaev", nick="python_training",
                 company="s-terra", mobile="+79999999999", mail="universal310@yandex.ru",
                 b_day="8", b_mounth="May", b_year="1998", id=None):
        self.name = name,
        self.last_name = last_name,
        self.nick = nick,
        self.company = company,
        self.mobile = mobile,
        self.mail = mail,
        self.b_day = b_day,
        self.b_mounth = b_mounth,
        self.b_year = b_year
        self.id = id