import datetime


subsequent_date = datetime.date.today() + datetime.timedelta(days=365*3)  # +3 Years from today yyyy-mm-dd format

print(subsequent_date.strftime("%Y.%m.%d"))  # Change format to yyyy.mm.dd = <class ' str>
