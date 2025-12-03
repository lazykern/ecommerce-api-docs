# Webhook configuration overview
There are two ways to configure webhooks: you can configure on Partner Center or using the Event API.
# Requirements

* You're familiar with how [webhooks](tts-webhooks-overview) work.
* You're [authenticated](sign-your-api-request) with the TikTok Shop API
* You have the required permissions for the topics you're subscribing to.

# Webhook URL Requirements

* Employ the `https://` scheme
* Use TLS v1.2+
* Webhook URL can only be a domain name, not an IP address, and it cannot have a port
* Success returns 200, and authentication failure returns 401

# Method 1: Configure webhooks on Partner Center
## Step 1: Configure webhook URL on Partner Center

1. Add an HTTP Server URL in the '**Developing**' tab under '**Basic information**' to receive webhook notifications.

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/165377e00bad4228aac1251b778836ea~tplv-10qhjjqwgv-image.image" width="864px" /></div>

## Step 2: Decide what webhook topic to subscribe
TikTok Shop Partner Center automatically subscribes your app to default webhook notifications. You can manage webhook subscriptions in the '**Developing tab**' to choose specific events and actions you want to receive notifications for.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/80497a486d8042bc832558b76a4d519d~tplv-10qhjjqwgv-image.image" width="864px" /></div>

## Step 3: Receive the webhook
TikTok Shop sends an HTTP POST request to the URL specified every time that event occurs. The HTTP POST request's parameters contain the JSON data relevant to the event that triggered the request.
TikTok Shop verifies SSL certificates when delivering payloads to HTTPS webhook addresses. Make sure your server is correctly configured to support HTTPS with a valid SSL certificate.
To validate incoming webhook notifications, TikTok Shop includes a signature code in the 'Authorization' field of the HTTP request header. Developers should verify this signature, and instructions for generating it can be found [here](sign-your-api-request).
## Step 4: Respond to the webhook
To confirm successful receipt of a webhook notification, the HTTP server url is required to provide a proper response to declare having received the notification successfully.
Acceptable HTTP responses include the following below:
| Header | Body | Response Interval |
| --- | --- | --- |
| 200 | NULL / empty | within 3 seconds for each notification |
| 401 | NULL / empty | within 3 seconds for each notification |

Failure to do so will result in a webhook push notification re-try from TikTok Shop. No further attempt will be made after the 4th retry failure.
| Retry | Trigger |
| --- | --- |
| 1st Retry | 2 minutes after the initial push failure |
| 2nd Retry | 30 minutes after the 1st retry failure |
| 3rd Retry | 3 hours after the 2nd retry failure |
| 4th Retry | 12 hours after the 3rd retry failure |
# Method 2: Configure webhooks using Event API
Here are the Event APIs you can use to configure webhooks:

1. [Update Shop Webhook](update-shop-webhook): Use this API to create a special webhook for a shop for a certain event. This is equivalent to step 1 and 2 if you configure webhooks in Partner Center.
2. [Get Shop Webhooks](get-shop-webhooks): Use this API to get all shop webhooks configurations
3. [Delete Shop Webhook](delete-shop-webhook): Use this API to cancel the webhook for a shop for a certain event

# How to check webhook event history?
TikTok Shop Partner Center also offers a portal for monitoring all webhook push logs, allowing you to debug and confirm the successful receipt of webhooks by your recipient URL server. To access this feature, go to **Partner Console >> Development Kits >> Webhook Log.** From there, select the specific app you want to view webhook logs for.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/fb0e252e3552460a8edd0fc4b9a3883a~tplv-10qhjjqwgv-image.image" width="864px" /></div>