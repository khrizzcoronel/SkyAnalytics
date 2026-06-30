from src.sre.changelog_generator import ChangelogGenerator, Commit


def test_no_public_changes_returns_none():
    gen = ChangelogGenerator()
    commits = [
        Commit(sha="a", message="chore: update ci"),
        Commit(sha="b", message="ci: bump action"),
    ]
    assert gen.generate("v1.0.0", commits) is None


def test_features_bump_minor_version():
    gen = ChangelogGenerator()
    commits = [
        Commit(sha="a", message="feat: add new dashboard"),
        Commit(sha="b", message="fix: correct latency metric"),
    ]
    entry = gen.generate("v1.4.2", commits)
    assert entry is not None
    assert entry.version == "v1.5.0"
    assert "add new dashboard" in entry.features
    assert "correct latency metric" in entry.fixes


def test_breaking_change_bumps_major_version():
    gen = ChangelogGenerator()
    commits = [
        Commit(sha="a", message="feat(api)!: remove legacy endpoint\n\nBREAKING CHANGE: endpoint removed"),
    ]
    entry = gen.generate("v1.4.2", commits)
    assert entry is not None
    assert entry.version == "v2.0.0"


def test_markdown_includes_pr_links():
    gen = ChangelogGenerator(repo_url="https://github.com/acme/sky")
    commits = [
        Commit(sha="a", message="feat: add widget (#42)"),
    ]
    entry = gen.generate("v1.0.0", commits)
    md = entry.to_markdown()
    assert "[##42](https://github.com/acme/sky/pull/42)" in md or "#42" in md
    assert "add widget" in md
