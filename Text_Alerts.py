import os
from twilio.rest import Client
from datetime import datetime
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {"https": os.environ['https_proxy']}
account_sid ="ACf0169bad626e36d7404199ae55ecd308"
account_token="433c091ac6021500a24928d93b3df885"
#Info for twilio


current = datetime.now()
weekday = current.isoweekday()



message_s = ['remember to pay Kan his $325','Python meeting 5:30 wednesday', 'Java meeting Friday 6:30','FAM 100 meeting thursday 8pm','Aerospace expo  june 1 and 2', 'General motto May 26th 2021, 5:30 -6:30pm, venue not yet given']

if weekday == 3:
    message_to_send = message_s[1]
elif weekday ==4:
    message_to_send = message_s[3]
elif weekday ==5:
    message_to_send = message_s[2]


client = Client(account_sid,account_token, http_client = proxy_client)
message = client.messages \
    .create(
    body= message_to_send,
    from_ = '+16087290030',
    to = '+13136526912'


)

print(message.status)
