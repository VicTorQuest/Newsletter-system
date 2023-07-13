
# Emailing Newsletter System with Django and Gmail SMTP

This project is a robust emailing newsletter system built using Django and integrated with Gmail SMTP for reliable email delivery. It provides a convenient way to manage and send newsletters to a large number of subscribers.



## Installation

1. Clone the repository:

```bash
  git clone https://github.com/VicTorQuest/Newsletter-system.git
```
2. Install the required dependencies
```bash
  pip install -r requirements.txt
```
3. Configure the Django **`settings.py`** file.
 - <b>Secret Key</b>: Create a **`.env`** file in the project root directory and generate a new secret key then add the following line:
```makeafile
  SECRET_KEY=your-secret-key-goes-here
```
Then, in **`settings.py`**, update the secret key assignment as follows:
```python
  import os
  SECRET_KEY = os.environ.get('SECRET_KEY')
```
 - **Django reCAPTCHA**: If you plan to use reCAPTCHA for spam protection, add the following lines to your **`.env`** file:
```python
  RECAPTCHA_SITE_KEY=your-recaptcha-site-key-goes-here
  RECAPTCHA_SECRET_KEY=your-recaptcha-secret-key-goes-here
```
In **`settings.py`**, update the reCAPTCHA settings as follows:
```python
  RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
  RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
  RECAPTCHA_REQUIRED_SCORE = 0.85
```
- Configure the Django **`settings.py`** file with your Gmail SMTP credentials.
```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
  EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
  APPLICATION_EMAIL = EMAIL_HOST_USER
  DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

4. Run database migrations: **`python manage.py migrate`**


5. Start the development server: **`python manage.py runserver`**

Ensure that you have the **`python-dotenv`** package installed (pip install python-dotenv) to enable loading environment variables from the **`.env`** file.

Please note that the secret key should be kept confidential and not shared publicly. Make sure to replace **'your-secret-key-goes-here'** with a secure and unique secret key.

If you decide to use Django reCAPTCHA for spam protection, obtain your reCAPTCHA site key and secret key from the reCAPTCHA website and replace **'your-recaptcha-site-key-goes-here'** and **'your-recaptcha-secret-key-goes-here'** respectively.

## Features

- **Subscriber Management**: Easily add, edit, and remove subscribers from the mailing list.
- **Subscription Management**: Allow subscribers to manage their preferences and unsubscribe if desired.
- **SPAM Protection**: Implemented measures to prevent newsletters from being marked as spam.
- **Integration with Gmail SMTP**: Utilize the reliable and secure Gmail SMTP service for email delivery.


## Usage
1. Access the admin panel at **`http://127.0.0.1:8000/admin`** and create an admin account
```bash
  python manage.py createsuperuser
```
2. Add subscribers to the mailing list.
<img src="https://iili.io/HLHINmF.png">
3. Create and schedule newsletters to be sent to the subscribers.
<img src="https://iili.io/HLHu96v.png">




## Contributing

Contributions are always welcome!

## Acknowledgements

 
Special thanks to the Django and Gmail teams for their excellent frameworks and services, which made this project possible.
## Contact

For any inquiries or feedback, please contact me at victorokolie001@gmail.com

Let's make email newsletters a breeze with Django and Gmail SMTP!
