# Sample Push Notification

The call registerForRemoteNotificationTypes: tells the device wants to receive push notification.
When the app starts shows a message to inform the user that this app wishes to send push notification, if the user choose “OK”, then we should be all set.
If they choose “Don’t Allow” the app never receive push notification.
The user can reverse their decision in the phone’s settings under menu Notifications.

Know types of push notifications are enabled is possible through:
```UIRemoteNotificationType enabledTypes = [[UIApplication sharedApplication] enabledRemoteNotificationTypes];```