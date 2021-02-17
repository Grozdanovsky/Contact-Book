from contact_book import *


# da se napravi funkcija za pecatenje lista spored e-mail
# prima string pr "gmail" ili "yahoo" i treba da gi ispecati site mailovi koi se gmail yahoo itn
def get_emails(lista_knigi,email):
    for item in lista_knigi:
        if item.get_email().find(email) > 1:
            print(item.get_email())



b1 = Book("Viktor","Grozdanovski","grozdanovski.viktor@yahoo.com","072244114")
b2 = Book("Stefan","Cvetanovski","cvetanovskistefan72@gmail.com","070997977")
b3 = Book("Bojan","Stojanovski","b.stojanovski@gmail.com","071777111")
b4 = Book("Petra","Ivanovska","petraivanovska@gmail.com","076123321")
b5 = Book("Filip","Gicevski","filipgicevski@yahoo.com","075555222")

lista_knigi = [b1,b2,b3,b4,b5]



get_emails(lista_knigi,"gmail")
get_emails(lista_knigi,"yahoo")












