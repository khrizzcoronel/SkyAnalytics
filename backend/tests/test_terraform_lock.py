from src.iac.terraform_lock import TerraformStateLock


def test_lock_acquire_and_release():
    lock = TerraformStateLock(ttl_seconds=60)
    info = lock.acquire("github-actions-1")
    assert info is not None
    assert lock.is_locked()
    assert lock.acquire("github-actions-2") is None
    assert lock.release("github-actions-1")
    assert not lock.is_locked()


def test_cannot_release_foreign_lock():
    lock = TerraformStateLock(ttl_seconds=60)
    lock.acquire("owner-a")
    assert not lock.release("owner-b")
    assert lock.is_locked()
