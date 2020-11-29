from sys import maxsize

class Contact:
    def __init__(self, name=None, last_name=None, nick=None,
                 company=None, mobile=None, homephone=None, workphone=None, all_phones_from_home_page=None,
                 mail=None, b_day=None,
                 b_mounth=None, b_year=None, id=None, all_mails_from_home_page=None):
        self.name = name
        self.last_name = last_name
        self.nick = nick
        self.company = company
        self.mobile = mobile
        self.homephone = homephone
        self.workphone = workphone
        self.mail = mail
        self.b_day = b_day
        self.b_mounth = b_mounth
        self.b_year = b_year
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def max_or_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize