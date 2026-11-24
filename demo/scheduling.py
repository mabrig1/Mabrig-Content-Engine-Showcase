"""Independent synthetic content scheduling example; no external actions."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class Post:
    title: str
    approved: bool
    scheduled_at: datetime

def status(post: Post, now: datetime) -> str:
    if not post.title.strip():
        raise ValueError("Post title required")
    if post.scheduled_at.utcoffset() is None or now.utcoffset() is None:
        raise ValueError("Timezone-aware timestamps required")
    if post.approved is not True:
        return "awaiting review"
    return "eligible for simulated queue" if post.scheduled_at <= now else "scheduled"

if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    print(status(Post("Fictional announcement", True, now), now))
