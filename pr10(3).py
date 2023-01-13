print("Enter date in format DD/MM/YYYY")
date=input("Enter date:")
date=date.split("/")
print("Date in formet MM-DD-YYYY: %s-%s-%s" % (date[1], date[0], date[2]))