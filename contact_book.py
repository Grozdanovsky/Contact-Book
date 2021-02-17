
class Book:
    def __init__(self,ime,prezime,e_mail,tel_broj):
        self.__ime = ime
        self.__prezime = prezime
        self.__e_mail = e_mail
        self.__tel_broj = tel_broj

    def get_email(self):
        return self.__e_mail;




