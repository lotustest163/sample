# Tested from django shell.

from sample import settings
# from django.conf import settings
from django.core.mail import send_mail

send_mail(
	'test',
	'sending from sample via sendgrid',
	'test@sample.com',
	['zhouyou.xy@gmail.com']
)