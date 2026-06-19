# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
      The purpose of the game is to bring fun and have the user guess a certain number to users.
- [x] Detail which bugs you found.
      I found that whenever the user input a number it was misleading the output. This because the string was the input instead of an integer.
- [x] Explain what fixes you applied.
      I changed it from being a string to an integer this gave the user the correct output and did not mislead them.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. First run the app with python3 -m streamlit run app.py. Depending on the python version you have you can run it with or without the 3.
2. A window will pop up with the site Game glitch investigator
3. In the middle of the page there is a text box that you input a guess in. After the input has taken place then you run the guess.
4. After the guess has been processed then the output of your guess can be to go lower or higher.
5. If the correct number was guessed then you will be rewarded with celebratory balloons.

**Screenshot** _(optional)_:

## 🧪 Test Results

```
tests/test_game_logic.py::test_winning_guess PASSED                                                               [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                              [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                               [ 75%]
tests/test_game_logic.py::test_hint_direction_matches_outcome PASSED                                              [100%]

=================================================== 4 passed in 0.09s ===================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
