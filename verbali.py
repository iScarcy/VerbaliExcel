
verbali = {}

verbale = {
    "verbale_id":"255874444/V/2023",
    "cognome":"rossi",
    "nome":"mario",
    "dataNascita":"16/01/1969"
}


print(verbali)

print(type(verbali))

if verbale["verbale_id"] not in verbali.keys():
    verbali[verbale["verbale_id"]] = verbale
else:
    print("ok")

print(verbali)

print(type(verbali))


verbale = {
    "verbale_id":"345678945/V/2023",
    "cognome":"ASCELL",
    "nome":"DAVINIA",
    "dataNascita":"13/11/2001"
}

if verbale["verbale_id"] not in verbali.keys():
    verbali[verbale["verbale_id"]] = verbale
else:
    print("ok")

print(verbali)

print(type(verbali))

verbale = {
    "verbale_id":"255874444/V/2023",
    "cognome":"rossi",
    "nome":"mariooooooooo",
    "dataNascita":"22/08/1983"
}

if verbale["verbale_id"] not in verbali.keys():
    verbali[verbale["verbale_id"]] = verbale
else:
    verbali[verbale["verbale_id"]]["dataNascita"] = verbale["dataNascita"]

print(verbali)

print(type(verbali))    