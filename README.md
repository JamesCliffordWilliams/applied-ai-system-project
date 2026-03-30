# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Recommendation systems compare things to a users normal preferences to predict what they will like. This simulation uses a content-based approach by matching song attributes directly to a user profile. It prioritizes mood and energy because they best represent a song’s overall vibe, while genre helps narrow down style. Acousticness is included to capture whether the user prefers a more acoustic or electronic sound. The goal is to recommend songs that closely match the user’s preferred feel, not just songs with high values.

The Song object will use the following features: id, title, artist, genre, mood, energy, and acousticness. The UserProfile object will use favorite_genre, favorite_mood, target_energy, and likes_acoustic.
Some prompts to answer:

The system uses a content-based approach to recommend songs based on a user’s preferences. It takes in the user’s genre, mood, target energy, and acoustic preference. Then it loops through every song in the CSV file and calculates a score for each one based on how well it matches those preferences. After all songs are scored, they are sorted from highest to lowest, and the top k songs are returned as the recommendations.

Algorithm Recipe

Each song gets points based on a few rules. If the genre matches the user’s preferred genre, the song gets +2.0 points. If the mood matches, it gets +1.5 points. The system also looks at energy and gives a score based on how close the song’s energy is to the user’s target energy using this formula: 1 minus the absolute difference between the two values. This means songs closer to the preferred energy get higher scores. Finally, the system checks acoustic preference. If the user likes acoustic songs and the song has high acousticness, or if the user prefers non-acoustic songs and the song has low acousticness, it gets +0.5 points. All these values are added together to get the final score.

Potential Biases

This system might over-prioritize genre, which could cause it to miss songs from other genres that still match the user’s mood and energy. It also mainly relies on energy to measure similarity, which simplifies how people actually experience music. The acoustic preference is handled in a basic way, so it may not fully reflect how users perceive sound. Because of this, the recommendations might be somewhat limited even if they seem accurate based on the rules.

![Output](Screenshot%202026-03-30%20020900.png)

## System Evaluation Outputs

### High-Energy Pop
![High Energy Pop](Screenshot%202026-03-30%20021718.png)

### Chill Lofi
![Chill Lofi](Screenshot%202026-03-30%20021714.png)

### Intense Rock / Edge Case
![Intense Rock](Screenshot%202026-03-30%20021710.png)
- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

The system shows a bias toward energy similarity, which often overrides other important features like mood and genre. During testing, high-energy songs were frequently recommended even when they did not match the user’s desired mood or genre, such as “Gym Hero” appearing for users who wanted sad or different-genre music. This creates a filter effect where songs with similar intensity are prioritized over songs that better match the user’s emotional preference. Additionally, the system does not strongly penalize mismatches, meaning songs can still rank highly even if they only match one feature. As a result, the recommender may produce less accurate results for users with specific or conflicting preferences.

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

