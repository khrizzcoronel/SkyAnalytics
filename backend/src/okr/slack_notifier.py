"""
Slack notifier for OKR publishing.

Abstracts the Slack webhook so tests can use an in-memory sink.
"""
from dataclasses import dataclass, field
from typing import List, Callable, Optional


@dataclass
class SlackMessage:
    channel: str
    text: str


class SlackNotifier:
    """Send or capture Slack notifications."""

    def __init__(
        self,
        webhook_url: Optional[str] = None,
        sink: Optional[List[SlackMessage]] = None,
    ):
        self.webhook_url = webhook_url
        self.sink = sink

    def send(self, channel: str, text: str) -> bool:
        if self.sink is not None:
            self.sink.append(SlackMessage(channel=channel, text=text))
            return True
        # In a real implementation, this would POST to webhook_url
        return bool(self.webhook_url)
