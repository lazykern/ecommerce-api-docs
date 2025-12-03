# Why do we have API rate limits?
Rate limits are a common practice for APIs, and they are put in place to ensure our platform remains stable and fair for everyone. We ask developers to use industry standard techniques for limiting calls, caching results, and re-trying requests responsibly.
# API Rate Limit Policy
## Quota

* Each app is automatically set with a default rate limit of 50 QPS (Queries Per Second) for each API.

## Limit method

* TikTok Shop API rate limits are based on the combination of the app and shop. This means that calls from one app don't affect the rate limits of another app, even when both apps are making requests for the same shop. Similarly, calls to one shop don't affect the rate limits of another shop, even when making requests from the same app.
* Apps can make the maximum number of requests per second. In our case, it would be 50 queries per second. Each request counts equally, regardless of how much or how little data is returned.
* All requests that are made after rate limits have been exceeded are throttled and an HTTP 429 error is returned.

# API Rate Limited Behavior and Responses
If you exceed the rate limits for API requests, the system will apply throttling and return specific HTTP status codes to inform you of the situation. Here are the relevant HTTP status codes and their descriptions:
| **HTTP Status Code** | **Description** |
| --- | --- |
| 429 | The HTTP status code 429 indicates "Too Many Requests." When a certain API service receives an excessive number of requests, it triggers rate limiting logic and returns this status code. This typically occurs when the client sends an excessive number of requests, exceeding the predefined processing capacity or request rate limit of the API service. |
| 503 | The HTTP status code 503 indicates "Service Unavailable," which means that the service is not available. When a server is unable to provide the requested service, it returns this status code. This can occur due to server overload, maintenance, temporary failures, or other reasons. The difference between HTTP status code 429 and 503 is that 429 is a platform-controlled rate limiting measure, while 503 is a non-platform-controlled protective measure to prevent server overload.' |
# Avoiding rate limit errors
Designing your app with best practices in mind is the best way to avoid throttling errors. For example, you can stagger API requests in a queue and do other processing tasks while waiting for the next queued job to run. Consider the following best practices when designing your app:

* Optimize your code to only get the data that your app requires.
* Use caching for data that your app uses often.
* Regulate the rate of your requests for smoother distribution.
* Include code that catches errors. If you ignore these errors and keep trying to make requests, then your app won't be able to gracefully recover.
* Automatically retry requests with a random exponential backoff. Retrying with exponential backoff means performing a short sleep when a rate limit error is hit, then retrying the unsuccessful request.