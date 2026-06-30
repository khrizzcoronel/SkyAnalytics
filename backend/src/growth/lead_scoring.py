"""
Growth hacking lead scoring and CAC calculator.

Scores leads based on corporate email domains and calculates campaign CAC.
"""
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Lead:
    email: str
    utm_campaign: str
    converted: bool = False
    score: int = 0


@dataclass
class Campaign:
    campaign_id: str
    budget_usd: float
    leads: List[Lead] = field(default_factory=list)


class LeadScorer:
    """Score leads and compute campaign-level CAC."""

    HIGH_VALUE_DOMAINS = {"airlines", "cargo", "logistics"}
    BASE_SCORE = 10
    MULTIPLIER = 2

    def score(self, lead: Lead) -> int:
        domain = lead.email.split("@")[-1].lower()
        if any(keyword in domain for keyword in self.HIGH_VALUE_DOMAINS):
            lead.score = self.BASE_SCORE * self.MULTIPLIER
        else:
            lead.score = self.BASE_SCORE
        return lead.score


class CampaignAnalyzer:
    """Analyze campaign performance and CAC."""

    def __init__(self, scorer: LeadScorer):
        self.scorer = scorer

    def process(self, campaign: Campaign) -> Dict:
        converted = [lead for lead in campaign.leads if lead.converted]
        for lead in campaign.leads:
            self.scorer.score(lead)
        cac = campaign.budget_usd / len(converted) if converted else float("inf")
        return {
            "campaign_id": campaign.campaign_id,
            "budget_usd": campaign.budget_usd,
            "total_leads": len(campaign.leads),
            "converted": len(converted),
            "conversion_rate": (len(converted) / len(campaign.leads) * 100)
            if campaign.leads
            else 0.0,
            "cac": cac,
            "total_score": sum(lead.score for lead in campaign.leads),
        }
