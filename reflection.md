# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? It was good and it took worked how it should.
- List at least two concrete bugs you noticed at the start  
  The range of the numbers was off the range and starting a new game was imposible without a whole page refresh.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior      | Actual Behavior   | Console Output / Error                             |
| ----- | ---------------------- | ----------------- | -------------------------------------------------- |
| 55    | lower or higher output | said to go higher | higher no error detected                           |
| 95    | lower or higher output | higher output     | out was higher no error detected                   |
| 100   | expected lower         | output was higher | The range was from 0-100 and this was not the case |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  There's no good reason for this. On every even-numbered attempt, the secret is converted to str.

2. check_guess then compares an int against a string — app.py:38-50

def check_guess(guess, secret):
if guess == secret: # 42 == "42" → always False
return "Win", "Correct!"
try:
if guess > secret: # 42 > "42" → TypeError in Python 3
...
except TypeError:
g = str(guess)
if g == secret: ...
if g > secret: # ← STRING comparison, lexicographic!
return "Too High", ...
return "Too Low", ...
When secret is a string:

guess == secret (42 == "42") is always False, so a correct guess on an even attempt is not recognized as a win.
guess > secret raises TypeError (can't compare int and str), so it falls into the except block and compares the numbers as text.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Here the AI gives us the wrong number to where the lines are located in the code , we do not see these on line 185-188:
  The culprit isn't the range itself — it's that the secret gets turned into a string on every other guess, which makes the "higher/lower" comparison lie to the user.

Here's the chain in app.py:

1. The secret is stringified on even attempts — app.py:185-188

if st.session_state.attempts % 2 == 0:
secret = str(st.session_state.secret) # ← secret becomes a string
else:
secret = st.session_state.secret

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
