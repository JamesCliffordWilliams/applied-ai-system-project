# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

This recommender suggests songs based on a user’s preferred genre, mood, and energy level. It assumes the user already knows the type of vibe they want, such as “happy pop” or “chill lofi.” This system is designed for classroom exploration, not for real-world use.

---

## 3. How the Model Works  

The model uses features like genre, mood, energy, and acousticness. It compares each song to the user’s preferences and assigns points. It gives more points for matching genre and mood, and it adds points based on how close the energy level is. It also adds a small bonus if the acoustic level matches the user’s preference. Songs with the highest total scores are recommended.

---

## 4. Data  

The dataset contains about 20 songs. It includes genres like pop, lofi, rock, hip-hop, and ambient. Each song has features such as energy, tempo, valence, and acousticness. Some genres, like pop and hip-hop, appear more often than others. The dataset is small and does not represent all types of music or user preferences.

---

## 5. Strengths  

The system works well when the user’s preferences are clear and consistent. For example, it correctly recommends low-energy, acoustic songs for a chill lofi profile. It also does a good job matching songs based on energy levels. In many cases, the top results match the expected vibe.

---

## 6. Limitations and Bias 

The system shows a bias toward energy similarity, which often overrides other features like mood and genre. High-energy songs are frequently recommended even when they do not match the user’s desired mood. For example, “Gym Hero” appears for users who want different moods because it has a high energy score. The system also does not strongly penalize mismatches, so songs can still rank highly even if they only match one feature.

---

## 7. Evaluation  

I tested the system using several different user profiles, including a “Chill Lofi” listener, an “Intense Rock” listener, and an edge case with high energy but a sad mood. For the Chill Lofi profile, the system performed well and returned songs like “Library Rain” and “Midnight Coding,” which clearly match both the low energy and acoustic vibe. This shows that when preferences are consistent, the recommender behaves as expected.

For the Intense Rock profile, the top result was correct (“Storm Runner”), but the system quickly started recommending songs from completely different genres like hip-hop and pop. This happened because those songs had similar energy levels, even though they did not match the genre. It shows that energy has a strong influence and can override genre preferences.

The most surprising results came from the edge case (high energy + sad). While “drivers license” appeared correctly because it matched both genre and mood, songs like “Gym Hero” and “Sunroof” also showed up. These songs are not sad, but they have high energy, so they still scored well. This shows that the system does not strongly penalize mood mismatches and tends to favor energy similarity.

Overall, the system works well for clear and consistent preferences, but it can produce unexpected results when preferences conflict or when songs share similar energy but differ in mood or genre.

---

## 8. Future Work  

I would add more features like tempo, valence, or lyrics to better capture a song’s full vibe. I would also improve the scoring system so it penalizes mismatches more strongly, especially for mood. Another improvement would be increasing diversity so the system does not always recommend songs from the same genre.

---

## 9. Personal Reflection  

My biggest learning moment during this project was realizing how small changes in scoring can completely change the recommendations. For example, giving energy too much importance caused songs like “Gym Hero” to show up even when they didn’t match the mood. It showed me how sensitive recommender systems are to design choices.

Using AI tools helped me move faster and understand how to structure my functions and logic. However, I still had to double-check the results because sometimes the code worked but didn’t produce the right behavior. I learned that just because something runs correctly doesn’t mean it is logically correct.

What surprised me most is how a simple algorithm can still feel like real recommendations. Even with just a few features like genre, mood, and energy, the system was able to produce results that made sense most of the time. At the same time, it also showed how easy it is for the system to make mistakes.

If I extended this project, I would improve how the system handles conflicts between preferences, like high energy and sad mood. I would also add more features like lyrics or user history and try to make the recommendations more diverse instead of repeating similar types of songs.