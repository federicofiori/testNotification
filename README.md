# Sample Push Notification

The call registerForRemoteNotificationTypes: tells the device wants to receive push notification.

When the app starts shows a message to inform the user that this app wishes to send push notification, if the user choose “OK”, then we should be all set.

If they choose “Don’t Allow” the app never receive push notification.

The user can reverse their decision in the phone’s settings under menu Notifications.

Know types of push notifications are enabled is possible through:

```UIRemoteNotificationType enabledTypes = [[UIApplication sharedApplication] enabledRemoteNotificationTypes];```

# Send Notification

Before you must create the correct certificate/provisioning profile and *.pem* file with Certificate and RSA PRIVATE KEY

For send notification use : *PyAPNs* (Python library for interacting with the Apple Push Notification Service).

Download https://pypi.python.org/pypi/pyapns/ or https://github.com/djacobs/PyAPNs

Code Example (*sendNotification.py*):

	import time
	from apns import APNs, Frame, Payload

	apns = APNs(use_sandbox=True, cert_file='ck.pem', key_file='ck.pem')
	# Send a notification
	# Insert target device token without brackets and white space
	token_hex = '6acbd1ee551dr15d034c150e4bd256e6b2730s89f9f13fcb2a0340aceb1fe7c3'
	payload = Payload(alert="Hello World", sound="default", badge=1)
	apns.gateway_server.send_notification(token_hex, payload)

Send the notification: ::

	$python sendNotification.py