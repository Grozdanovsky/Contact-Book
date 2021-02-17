
class Book:
    def __init__(self,ime,prezime,e_mail,tel_broj):
        self.__ime = ime
        self.__prezime = prezime
        self.__e_mail = e_mail
        self.__tel_broj = tel_broj




    def get_broj(self):
        return self.__tel_broj

    def get_user(self):
        print(f"Ime: {self.__ime}\nPrezime: {self.__prezime}\nE-mail: {self.__e_mail}\nTelefonski Broj: {self.__tel_broj}\n\n")

