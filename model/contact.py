from sys import maxsize

class Contact:
    def __init__(self, name=None, last_name=None, nick=None, middlename=None, title=None, homepage=None,
                 company=None, mobile=None, homephone=None, workphone=None, all_phones_from_home_page=None,
                 b_day=None, address=None,  secondaryphone=None, notes=None, fax=None,
                 b_mounth=None, b_year=None, id=None, all_emails_from_home_page=None,
                 email=None, email2=None, email3=None, address2=None):
        self.address = address
        self.name = name
        self.last_name = last_name
        self.nick = nick
        self.company = company
        self.mobile = mobile
        self.homephone = homephone
        self.workphone = workphone
        self.email = email
        self.b_day = b_day
        self.b_mounth = b_mounth
        self.b_year = b_year
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.middlename = middlename
        self.title = title
        self.homepage = homepage
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.fax = fax
        self.address2 = address2

    def __repr__(self):
        return "%s, %s, %s, %s " % (self.id, self.name, self.last_name, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def max_or_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize