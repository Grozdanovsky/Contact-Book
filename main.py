from contact_book import *

b1 = Book("Viktor", "Grozdanovski", "grozdanovski.viktor@yahoo.com", "072244114")

b2 = Book("Stefan", "Cvetanovski", "cvetanovskistefan72@gmail.com", "070997977")

b3 = Book("Bojan", "Stojanovski", "b.stojanovski@gmail.com", "071707111")

b4 = Book("Petra", "Ivanovska", "petraivanovska@gmail.com", "076123321")

b5 = Book("Filip", "Gicevski", "filipgicevski@yahoo.com", "075555222")

lista_knigi = [b1, b2, b3, b4, b5]


def get_emails(lista_knigi, email):
    if email.lower() == "yahoo":
        for item in lista_knigi:
            if item.get_email().find(email) > 1:
                item.get_user()

    elif email.lower() == "gmail":
        for item in lista_knigi:
            if item.get_email().find(email) > 1:
                item.get_user()


def listanje_po_broevi(lista_broevi, operator):
    for item in lista_broevi:
        if operator.lower() == "telekom":

            if item.get_broj()[0:3] == "070" or item.get_broj()[0:3] == "071" or item.get_broj()[0:3] == "072":
                item.get_user()

        elif operator.lower() == "one":
            if item.get_broj()[0:3] == "075" or item.get_broj()[0:3] == "076" or item.get_broj()[0:3] == "077":
                item.get_user()


# MAIN

odluka = input("Sakata da pregledate preku email ili telefonski broj: ")

if (odluka == "email"):
    emailType = input("koi mejlovi gi sakate")
    get_emails(lista_knigi, emailType)

if (odluka == "broj"):
    operatorType = input("koj operator go sakate")
    listanje_po_broevi(lista_knigi, operatorType)
