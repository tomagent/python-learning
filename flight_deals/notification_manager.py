from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, origin_city, origin_airport, destination_city, destination_airport, leave_date, return_date, airline, price):
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.leave_date = leave_date
        self.return_date = return_date
        self.airline = airline
        self.price = price
        self.phone_number = "+14582305585"
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.send_text_msg()

    def send_text_msg(self):
        body = f"Low price alert! Only £{self.price} from {self.origin_city}-{self.origin_airport} to {self.destination_city}" \
                    f"-{self.destination_airport}, from {self.leave_date} to {self.return_date} via {self.airline}"
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=body,
            from_=self.phone_number,
            to='+525514233587'
        )

        print(message.status)