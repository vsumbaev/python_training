from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact())
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    app.contact.delete_contact()