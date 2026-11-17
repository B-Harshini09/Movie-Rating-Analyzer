# Test Cases — Movie Rating Analyzer (PS No. 23)

This document outlines the functional, boundary, and error-handling test cases for the **Movie Rating Analyzer** application.

---

## Test Case 1: Normal Input (Overall Summary)
**Objective:** Verify that the application accurately computes the overall average rating, identifies the highest and lowest-rated movies, and renders the summary charts for a standard dataset.

* **Input Dataset (`movies.csv`):**
  ```csv
  Movie,Genre,Rating
  Inception,SciFi,8.8
  Titanic,Romance,7.9
  Interstellar,SciFi,8.6
  ```
* **Menu Selection:** `1` (Summary)
* **Expected Console Output:**
  ```text
  --- MOVIE SUMMARY ---
  Average rating: 8.43
  Top rated: Inception (8.8)
  Lowest: Titanic (7.9)
  ```
* **Expected Visual Output:**
  1. Bar chart titled **"Movie Ratings"** displaying bars for Inception (`8.8`), Titanic (`7.9`), and Interstellar (`8.6`).
  2. Histogram titled **"Movie Rating Histogram"** displaying the rating distribution.

---

## Test Case 2: Boundary / Minimum Input
**Objective:** Verify that the application handles the minimum valid dataset (a single record) without errors, returning the same movie for both top and lowest ratings.

* **Input Dataset (`movies.csv`):**
  ```csv
  Movie,Genre,Rating
  Sholay,Action,10
  ```
* **Menu Selection:** `1` (Summary)
* **Expected Console Output:**
  ```text
  --- MOVIE SUMMARY ---
  Average rating: 10.00
  Top rated: Sholay (10.0)
  Lowest: Sholay (10.0)
  ```
* **Expected Visual Output:**
  1. Bar chart titled **"Movie Ratings"** with a single bar at `10.0`.
  2. Histogram titled **"Movie Rating Histogram"**.

---

## Test Case 3: Invalid Input Handling
**Objective:** Verify that the data cleaning pipeline properly detects and filters out ratings outside the valid `0–10` range as well as non-numeric rating values.

* **Input Dataset (`movies.csv`):**
  ```csv
  Movie,Genre,Rating
  Inception,SciFi,8.8
  Titanic,Romance,11
  Dangal,Drama,abc
  ```
* **Menu Selection:** `1` (Summary)
* **Expected Behavior & Console Output:**
  * Row 3 (`Dangal,Drama,abc`) is coerced to `NaN` via `pd.to_numeric(..., errors="coerce")` and dropped automatically during missing-value cleanup.
  * Row 2 (`Titanic,Romance,11`) is flagged as out-of-bounds (`< 0` or `> 10`), triggering a warning message before being filtered out:
    ```text
    Row 2 skipped: Rating must be between 0 and 10.
    ```
  * Only **1 valid row** (`Inception,SciFi,8.8`) remains for analysis:
    ```text
    --- MOVIE SUMMARY ---
    Average rating: 8.80
    Top rated: Inception (8.8)
    Lowest: Inception (8.8)
    ```

---

## Test Case 4: Different Valid Scenario (Genre-Wise Average)
**Objective:** Verify that `groupby()` accurately calculates average ratings per genre, identifies the highest-rated genre, and displays the genre-wise bar chart.

* **Input Dataset (`movies.csv`):**
  ```csv
  Movie,Genre,Rating
  Inception,SciFi,8.8
  Titanic,Romance,7.9
  Interstellar,SciFi,8.6
  ```
* **Menu Selection:** `2` (Genre-wise Average)
* **Expected Console Output:**
  ```text
  --- GENRE-WISE AVERAGE ---
  Romance: 7.90
  SciFi: 8.70

  Best genre: SciFi
  ```
* **Expected Visual Output:**
  1. Bar chart titled **"Genre-wise Average Rating"** showing `Romance` (`7.90`) and `SciFi` (`8.70`).
  2. Histogram titled **"Movie Rating Histogram"** displaying the overall rating distribution.