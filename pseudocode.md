MAX_SESSION = 43200  // seconds
BASE_THRESHOLD = 300 // seconds
JITTER = random_between(0, 300) // seconds

if token.remaining_seconds() <= BASE_THRESHOLD + JITTER:
    attempt_refresh_with_exponential_backoff_and_jitter()

