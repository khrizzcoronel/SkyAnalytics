from src.devex.sdk_release import SDKReleasePlanner


def test_minor_bump_for_non_breaking_release():
    planner = SDKReleasePlanner()
    releases = planner.plan("v1.4.2", breaking_change=False)
    assert len(releases) == 3
    assert all(r.next_version == "v1.5.0" for r in releases)


def test_major_bump_for_breaking_release():
    planner = SDKReleasePlanner()
    releases = planner.plan("v1.4.2", breaking_change=True)
    assert all(r.next_version == "v2.0.0" for r in releases)
    assert any(r.language == "python" for r in releases)
    assert any(r.language == "javascript" for r in releases)
    assert any(r.language == "java" for r in releases)
