from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    # Too high means the player should guess lower next time
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    # Too low means the player should guess higher next time
    assert "HIGHER" in message

def test_hint_direction_matches_outcome():
    # Regression test for the swapped high/low hint bug.
    # The buggy version told players to "Go HIGHER!" when they were too high
    # and "Go LOWER!" when they were too low. The hint direction must always
    # point back toward the secret.
    too_high_outcome, too_high_message = check_guess(99, 50)
    assert too_high_outcome == "Too High"
    assert "LOWER" in too_high_message
    assert "HIGHER" not in too_high_message

    too_low_outcome, too_low_message = check_guess(1, 50)
    assert too_low_outcome == "Too Low"
    assert "HIGHER" in too_low_message
    assert "LOWER" not in too_low_message
