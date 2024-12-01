import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)

class SMSHandler:
    sms = africastalking.SMS

    def send_message(self, recipients, message):
        try:
            response = self.sms.send(message, recipients) 
            print(response)
            return response
        except Exception as err:
            print(f"Error sending SMS: {err}")
            return None
