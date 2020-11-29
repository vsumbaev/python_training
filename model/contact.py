from sys import maxsize

class Contact:
    """Класс, описывающий атрибуты для метода create_contact"""
    def __init__(self, name=None, last_name=None, nick="python_training",
                 company="s-terra", mobile=None, homephone=None, workphone=None, all_phones_from_home_page=None,
                 mail="universal310@yandex.ru", b_day="8", b_mounth="May", b_year="1998", id=None):
        self.name = name,
        self.last_name = last_name,
#        self.nick = nick,
#        self.company = company,
        self.mobile = mobile,
        self.homephone = homephone,
        self.workphone = workphone,
#        self.mail = mail,
#        self.b_day = b_day,
#        self.b_mounth = b_mounth,
#        self.b_year = b_year
        self.id = id,
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def max_or_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize