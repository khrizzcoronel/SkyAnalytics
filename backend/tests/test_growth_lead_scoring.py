from src.growth.lead_scoring import LeadScorer, CampaignAnalyzer, Lead, Campaign


def test_high_value_domain_gets_double_score():
    scorer = LeadScorer()
    lead = Lead(email="contact@fastairlines.com", utm_campaign="beta")
    assert scorer.score(lead) == 20


def test_regular_domain_gets_base_score():
    scorer = LeadScorer()
    lead = Lead(email="user@gmail.com", utm_campaign="beta")
    assert scorer.score(lead) == 10


def test_cac_calculation():
    scorer = LeadScorer()
    analyzer = CampaignAnalyzer(scorer)
    campaign = Campaign(
        campaign_id="beta_launch_europe",
        budget_usd=5_000,
        leads=[
            Lead(email="a@airlines.com", utm_campaign="beta_launch_europe", converted=True),
            Lead(email="b@gmail.com", utm_campaign="beta_launch_europe", converted=False),
            Lead(email="c@logistics.com", utm_campaign="beta_launch_europe", converted=True),
        ],
    )
    report = analyzer.process(campaign)
    assert report["total_leads"] == 3
    assert report["converted"] == 2
    assert report["cac"] == 2_500
