from twilio.rest import Client
account_sid = 'AC767eabb6d6c8c301f48b789085911414'
auth_token = 'eb27fd108a53c29769c8403ac4aa4875'


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919717067624", 
    from_="+12342318363",
    body="Hello from Python AGAIN!")

#myTwilioNumber = '+12342342318363'
#myCellPhone = '+919717067624'
#message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
