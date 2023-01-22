# Rain Alert

Send a rain alert SMS if there is rain forcasted in the next 12 hours. 
Weather data is sourced from https://openweathermap.org/api.

Uses Twilio API for SMS (https://www.twilio.com/en-us/messaging/channels/sms)

Code is based on based on the code found in the Udemy course 
"100 Days of Code: The Complete Python Pro Bootcamp for 2023" 
by Dr. Angela Yu. (https://www.udemy.com/course/100-days-of-code/)

Requires following environment variables:

* FROM_NUMBER: Phone number to send SMS
* OWM_API_KEY: Open Weather Map API key
* TO_NUMBER: Phone number to receive the SMS
* TWILIO_AUTH_TOKEN: Twilio authorization token
* TIWILIO_ACCOUNT_SID: Twilio account SID
* LATITUDE: Latitude of your location (https://www.latlong.net/)
* LONGITUDE: Longitude of your location
* VERBOSE: Verbose (True or False)
