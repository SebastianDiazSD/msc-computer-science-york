# Canvas Lab Posts – Week 6
**Advanced Programming | Sebastian Diaz**

---

## Activity 1 – Data Wrangling
**Label: `Activity 1 - Data wrangling`**

Hi everyone,

Both datasets come with some interesting data quality issues baked in — different grade orderings (F,P,M,D in Dataset 1 vs P,M,D,F in Dataset 2), typos in college and subject names, and different period labelling (Year 1/Year 2 vs academic years 16-17/17-18). Documenting these assumptions before writing any code made the merge process much cleaner.

**Exercise 1 — Reshaping:**

The two target formats required grouping at different levels of the MultiIndex. For format (a) — subjects as columns — I aggregated across colleges using `groupby(level='Subject', axis=1).sum()`. For format (b) — colleges as columns, gender as rows — I summed across subjects and periods to collapse down to just College × Gender × Grade.

**Exercise 2 — Merge and analysis:**

Merged the two datasets using `pd.concat([df1_year, df2], axis=1)` after normalising spelling and treating "Evening" rows as a separate cohort (excluded from Year 1 / Year 2 comparison).

Key results:
1. **Mathematics, English, Technology year comparison**: Year 2 consistently shows a lower fail rate than Year 1 across all three subjects — students who make it to Year 2 are a self-selected group that has already passed Year 1 screening.
2. **Fail rate by gender per subject**: Males have a higher fail rate than females in most subjects, most notably in Engineering and Technology disciplines.
3. **Female outperformance**: Females achieve a higher Merit+Distinction rate in Psychology, Chemistry, and Art — subjects where communication and analytical writing are assessed more heavily than purely mathematical problem-solving.

One assumption I want to flag: I treated F,P,M,D values as correctly labelled in both files — the files use different grade ordering in the header rows, but the grade labels themselves are correct. If anyone reads this differently in their file, I'd be curious to hear.

---

## Activity 2 – Data Representation
**Label: This activity posts to Padlet, not Canvas. See `Activity_2_Padlet_Response.md` for the prepared post content.**

---

## Activity 3 – Data Visualisation
**Label: `Activity 3 - Data visualisation`**

Hi everyone,

**Exercise 1 — Matplotlib + Tkinter framework:**

I built a `ChartFrame` class that embeds a `FigureCanvasTkAgg` in a tkinter window. A row of buttons calls `swap_chart(kind)`, which clears the axes and redraws with the new chart type — without recreating the window or the canvas. This pattern is straightforward to extend: adding a new chart type just means adding a new `elif` branch and a new button. The `NavigationToolbar2Tk` is included by default, giving zoom, pan, and save functionality for free.

**Exercise 2 — College grades analysis:**

For Q1 (success rate per subject in Year 2), I used a **stacked bar chart** with four colour-coded grade bands. Choosing the stacked form over grouped made sense here because the primary question is about the proportion of passes vs fails — the stack directly shows that proportion.

Key findings:
- Engineering has the highest fail rate in Year 2 across the combined dataset
- Psychology and Art have the highest combined Merit+Distinction rate
- Technology has the most even spread across all four grades

For Q2 (Year 1 vs Year 2 per college), I used **grouped bar charts**, one panel per college. Year 2 consistently shows fewer fails than Year 1, and more Distinctions in most colleges — consistent with progression effects.

**Exercise 3 — Visualisation justification (in notebook):** Stacked bar for composition/proportion; grouped bar for direct category comparison. Key limitation of stacked bar: non-baseline segments (M, D) are hard to compare exactly across subjects.

**Exercise 4 — tkinter GUI:** The `launch_gui()` function creates a window with an `OptionMenu` dropdown to select the college and a `FigureCanvasTkAgg` that updates dynamically when the dropdown changes.

---

## Activity 4 – Data Analysis
**Label: `Activity 4 - Data analysis`**

Hi everyone,

Both exercises here use the McKinney textbook datasets (Baby Names and USDA). If you are using Google Colab, you can download and mount them directly.

**Exercise 1 — Baby Names:**

For the random 5M/5F name comparison, I used `np.random.seed(42)` to make the selection reproducible. The line chart over 1880–2010 immediately reveals the cultural cycles in name popularity — some names spike for a decade and then almost disappear, while others show slow, steady decline.

For the birth totals chart (male vs female), the post-WWII baby boom is visible clearly — a sharp peak around 1955–1960, followed by a gradual drop into the 1970s, and a second smaller peak in the 1980s. Male and female births track almost perfectly together, which makes sense given natural sex ratios at birth.

For the popularity hypothesis, I selected **Linda** — one of the most remarkable name spikes in US data, peaking ~1947-1952. My 200-word plan in the notebook proposes correlating the song "Linda" (1947) chart positions with birth data using a conception-lag-adjusted regression. I'd be interested whether anyone chose a more recent name and found social media or film correlations instead.

**Exercise 2 — USDA:**

For cheese nutrients: protein, fat, and sodium are the dominant nutrients by mean value. Standard deviations are high relative to the means, reflecting the wide variety of cheese types.

For potassium sources: I excluded Spices and Herbs from the ranking — technically high per 100g but consumed in gram quantities, so not meaningful 'sources'. The top practical sources are dried legumes, nuts, and some fish. I drew the threshold at 400mg/100g, which is above the median potassium content across the whole database.

---

## Activity 5 – Special Data Types
**Label: `Activity 5 - Special data types`**

Hi everyone,

**Exercise 1 — Data type identification in Chapter 14 datasets:**

- **Time data (timezone):** The MovieLens `timestamp` column is Unix epoch — always UTC. Converting to meaningful local time requires a timezone conversion. The data represents US users, so US/Eastern or US/Pacific would be the relevant choices.
- **Continuous numerical data:** The USDA `value` field (nutrient quantities per 100g) is genuinely continuous — any positive real value is valid, and arithmetic operations (mean, std, correlation) are meaningful.
- **Nominal data:** Zip codes in MovieLens `users.dat` are nominal labels — the numbers carry no mathematical meaning and should never be averaged or sorted as if they did.
- **Coded categorical data:** `Occupation` and `Age` in MovieLens are stored as integers but are category codes. Age code `56` means "56+ years old", not the number 56. Averaging these directly would produce nonsense.

**Exercise 2 — MovieLens information need:**

My question: "Do male and female users rate films differently within the same genre?"

Key findings: The largest rating gaps between genders appear in Horror (men rate higher) and Romance/Drama (women rate higher). The overall mean gap is small (<0.2 stars) but consistent across a large sample size (1M ratings), suggesting genuine preference differences that a naive recommendation algorithm trained on aggregate ratings would miss.

The most important data handling decision was using `explode()` on the genres column — each film has multiple genres, and without exploding, genre-level analysis would be impossible. Treating `Age` as coded ordinal (not numeric) and converting timestamps to UTC were the other key type-awareness decisions.

---
