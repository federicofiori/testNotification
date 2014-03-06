import time
from apns import APNs, Frame, Payload

apns = APNs(use_sandbox=True, cert_file='ck.pem', key_file='ck.pem')
# Send a notification
# Insert target device token without brackets and white space
token_hex = '6acbd1ee551dr15d034c150e4bd256e6b2730s89f9f13fcb2a0340aceb1fe7c3'
payload = Payload(alert="Hello World", sound="default", badge=1)
apns.gateway_server.send_notification(token_hex, payload)
