# 🚢 Titanic Survival Analysis (EDA)

## 📌 Project Overview

In this project, I explored the Titanic dataset from Kaggle to understand what factors influenced passenger survival. The goal was to go beyond surface-level patterns and carefully analyze how different features relate to survival outcomes.

I focused on variables such as gender, age, passenger class, fare, and family size. Instead of just looking at individual features, I also tried to understand how these variables interact with each other and how reliable the observed patterns are.

---

## 🔍 Key Findings

* **Gender turned out to be the most important factor**, with females having much higher survival rates than males, especially among adults.
* **Children had relatively higher survival rates**, which likely reflects evacuation priorities at the time.
* **Passenger class played a major role**, with first-class passengers having significantly better chances of survival compared to lower classes.
* **Fare showed a positive relationship with survival**, but this is largely because it is closely tied to passenger class (higher fare → higher class).
* **Family size showed a non-linear pattern** — passengers traveling in small families (1–3 members) had the highest survival rates.
* **Passengers traveling alone or in large families had lower survival rates**, possibly due to lack of support or coordination challenges.
* Some extreme results (like very large families having zero survival) were based on very small sample sizes, so they were interpreted cautiously.

---

## 🛠️ What I Practiced / Learned

* Cleaning real-world data and handling missing values
* Creating new features (age groups, fare categories, family size)
* Analyzing relationships between variables instead of looking at them in isolation
* Understanding that not all patterns are linear
* Being careful with conclusions when sample sizes are small
* Writing clear insights instead of just showing numbers

---

## 🧰 Tools Used

* Python
* Pandas
* Matplotlib, Seaborn(used minimally for basic visualization checks)

---

## 🚀 Final Thoughts

This project helped me understand how important it is to not just find patterns in data, but also to question them. Some relationships were very clear (like gender), while others required more careful interpretation (like family size and fare).

Overall, this was a great exercise in building intuition around data and learning how to communicate insights clearly.
