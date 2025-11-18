IAM: set Maximum Session Duration = 43,200 seconds.

Issuance: mint credentials for the full 12 hours.

Cache policy: return cached credentials for normal operation.

Refresh trigger: refresh only when remaining_time ≤ 300 seconds plus randomized jitter.

Jitter: choose jitter uniformly in [0, 300] seconds to spread refreshes across a 5- to 10-minute window.

Failure handling: on refresh failure use exponential backoff with jitter and circuit breaking to avoid retry storms.

Monitoring: alert on elevated refresh rates or control-plane error rates.

Security note: document revocation and compromise procedures since long sessions reduce immediate revocability.
