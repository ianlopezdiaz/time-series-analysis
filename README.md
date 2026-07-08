# Time Series Analysis with Python

> A comprehensive, hands-on guide to time series analysis, forecasting, and temporal machine learning using Python.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://www.python.org/)
[![Quarto](https://img.shields.io/badge/Quarto-Website-39729E?logo=quarto)](https://quarto.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

**Time Series Analysis with Python** is a long-term educational and portfolio project that aims to provide a complete introduction to time series analysis, from fundamental statistical concepts to modern machine learning and deep learning methods.

Rather than focusing exclusively on forecasting, this repository explores the broader field of temporal data analysis, emphasizing both the mathematical intuition behind the methods and their practical implementation in Python.

The project is designed to function simultaneously as:

- an interactive online textbook;
- a practical Python reference;
- a collection of reproducible case studies;
- a showcase of modern data science and software engineering practices.

The accompanying Quarto website presents the material as a structured course in which each chapter builds upon the previous ones.

---

## Goals

This project aims to:

- Teach time series analysis from first principles.
- Develop intuition alongside mathematical rigor.
- Cover the complete workflow of temporal data analysis.
- Demonstrate practical implementations using Python.
- Compare classical statistical methods with modern machine learning approaches.
- Build reusable utilities throughout the course.
- Present realistic end-to-end case studies.
- Maintain reproducible, well-documented code.
- Continuously expand as new topics are added.

---

## Topics Covered

The repository is organized into progressively more advanced sections.

### Part I - Foundations

- What is a time series?
- Time indexes
- Date and time handling
- Data cleaning
- Missing values
- Resampling
- Aggregation
- Rolling statistics
- Visualization

### Part II - Exploratory Analysis

- Trend
- Seasonality
- Cycles
- Noise
- Time series decomposition
- Smoothing techniques
- Moving averages
- Correlation over time

### Part III - Statistical Foundations

- White noise
- Random walks
- Stationarity
- Differencing
- Transformations
- Autocorrelation (ACF)
- Partial autocorrelation (PACF)
- Unit root tests

### Part IV - Classical Forecasting

- Naive forecasting
- Moving averages
- Exponential smoothing
- Holt
- Holt-Winters
- AR
- MA
- ARMA
- ARIMA
- SARIMA

### Part V - Feature Engineering

- Lag features
- Rolling window features
- Calendar features
- Fourier features
- Feature selection

### Part VI - Machine Learning

- Forecasting as supervised learning
- Linear models
- Decision Trees
- Random Forests
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

### Part VII - Deep Learning

- Sequence modeling
- Recurrent Neural Networks
- LSTM
- GRU
- Transformers
- Modern forecasting architectures

### Part VIII - Model Evaluation

- Time-aware train/test splits
- Walk-forward validation
- Backtesting
- Forecast accuracy metrics
- Prediction intervals

### Part IX - Case Studies

Complete end-to-end projects using real-world datasets, including topics such as:

- Retail sales forecasting
- Electricity demand
- Bike-sharing demand
- Household energy consumption
- Air quality
- Weather
- Traffic
- Financial markets
- Cryptocurrency
- Website traffic

---

## Repository Structure

```text
time-series-analysis/
│
├── README.md                                   # Project overview, objectives, installation instructions, and learning roadmap.
├── index.qmd                                   # Quarto website landing page.
├── _quarto.yml                                 # Quarto website configuration.
├── environment.yml                             # Conda environment specification.
├── requirements.txt                            # Pip dependencies.
├── LICENSE                                     # Project license.
├── CONTRIBUTING.md                             # Guidelines for contributors.
├── CHANGELOG.md                                # Project version history.
├── ROADMAP.md                                  # Planned features, chapters, and future milestones.
├── pyproject.toml                              # Project metadata and tooling configuration.
│
├── notebooks/
│   │
│   ├── 01_foundations/
│   │   ├── 01_what_is_a_time_series.ipynb
│   │   ├── 02_time_indexes.ipynb
│   │   ├── 03_datetime_with_pandas.ipynb
│   │   ├── 04_loading_and_cleaning_data.ipynb
│   │   ├── 05_resampling_and_aggregation.ipynb
│   │   ├── 06_missing_values.ipynb
│   │   ├── 07_rolling_statistics.ipynb
│   │   └── 08_visualization.ipynb
│   │
│   ├── 02_exploratory_analysis/
│   │   ├── 01_trend_seasonality_and_noise.ipynb
│   │   ├── 02_time_series_decomposition.ipynb
│   │   ├── 03_moving_averages.ipynb
│   │   ├── 04_exponential_smoothing.ipynb
│   │   └── 05_autocorrelation_visualization.ipynb
│   │
│   ├── 03_statistical_foundations/
│   │   ├── 01_white_noise_and_random_walks.ipynb
│   │   ├── 02_stationarity.ipynb
│   │   ├── 03_differencing.ipynb
│   │   ├── 04_acf_and_pacf.ipynb
│   │   ├── 05_unit_root_tests.ipynb
│   │   └── 06_transformations.ipynb
│   │
│   ├── 04_classical_forecasting/
│   │   ├── 01_baseline_models.ipynb
│   │   ├── 02_exponential_smoothing_models.ipynb
│   │   ├── 03_autoregressive_models.ipynb
│   │   ├── 04_arima.ipynb
│   │   ├── 05_sarima.ipynb
│   │   └── 06_model_selection.ipynb
│   │
│   ├── 05_feature_engineering/
│   │   ├── 01_lag_features.ipynb
│   │   ├── 02_rolling_window_features.ipynb
│   │   ├── 03_calendar_features.ipynb
│   │   ├── 04_fourier_features.ipynb
│   │   └── 05_feature_selection.ipynb
│   │
│   ├── 06_machine_learning/
│   │   ├── 01_forecasting_as_supervised_learning.ipynb
│   │   ├── 02_linear_models.ipynb
│   │   ├── 03_decision_trees.ipynb
│   │   ├── 04_random_forests.ipynb
│   │   ├── 05_gradient_boosting.ipynb
│   │   ├── 06_xgboost.ipynb
│   │   ├── 07_lightgbm.ipynb
│   │   └── 08_catboost.ipynb
│   │
│   ├── 07_deep_learning/
│   │   ├── 01_sequence_modeling.ipynb
│   │   ├── 02_recurrent_neural_networks.ipynb
│   │   ├── 03_lstm.ipynb
│   │   ├── 04_gru.ipynb
│   │   ├── 05_transformers.ipynb
│   │   └── 06_modern_forecasting_architectures.ipynb
│   │
│   ├── 08_model_evaluation/
│   │   ├── 01_train_test_splits.ipynb
│   │   ├── 02_walk_forward_validation.ipynb
│   │   ├── 03_backtesting.ipynb
│   │   ├── 04_forecasting_metrics.ipynb
│   │   └── 05_prediction_intervals.ipynb
│   │
│   ├── 09_case_studies/
│   │   ├── 01_bike_sharing_demand.ipynb
│   │   ├── 02_retail_sales_forecasting.ipynb
│   │   ├── 03_electricity_demand.ipynb
│   │   ├── 04_household_energy_consumption.ipynb
│   │   ├── 05_air_quality_prediction.ipynb
│   │   ├── 06_weather_forecasting.ipynb
│   │   ├── 07_traffic_prediction.ipynb
│   │   ├── 08_financial_time_series.ipynb
│   │   ├── 09_cryptocurrency_forecasting.ipynb
│   │   └── 10_website_traffic.ipynb
│   │
│   └── appendix/
│       ├── 01_probability_review.ipynb
│       ├── 02_linear_algebra_review.ipynb
│       ├── 03_statistical_tests.ipynb
│       └── 04_python_tips.ipynb
│
├── ts/                                         # Reusable Python package used throughout the notebooks.
│   ├── __init__.py
│   ├── datasets.py                             # Dataset loading and downloading utilities.
│   ├── preprocessing.py                        # Cleaning, interpolation, differencing, scaling, etc.
│   ├── features.py                             # Lag, rolling, calendar, and Fourier feature generation.
│   ├── plotting.py                             # Consistent visualization functions.
│   ├── decomposition.py                        # Time series decomposition utilities.
│   ├── forecasting.py                          # Baseline forecasting helper functions.
│   ├── evaluation.py                           # Backtesting and validation utilities.
│   ├── metrics.py                              # Forecast evaluation metrics.
│   ├── transforms.py                           # Mathematical transformations and inverse transforms.
│   └── utils.py                                # General-purpose helper functions.
│
├── data/
│   ├── raw/                                    # Original datasets.
│   ├── interim/                                # Intermediate datasets.
│   ├── processed/                              # Cleaned datasets ready for modeling.
│   └── external/                               # Large datasets downloaded automatically.
│
├── figures/                                    # Figures generated for documentation and website.
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_features.py
│   ├── test_metrics.py
│   ├── test_evaluation.py
│   └── test_transforms.py
│
├── scripts/
│   ├── download_data.py                        # Download public datasets.
│   ├── build_features.py                       # Generate reusable feature sets.
│   ├── build_environment_files.py              # Synchronize dependency files.
│   └── make_tree.py                            # Print the project directory tree.
│
├── references/
│   ├── bibliography.bib                        # BibTeX references for Quarto citations.
│   ├── datasets.md                             # Dataset catalog used throughout the project.
│   └── glossary.md                             # Glossary of common time series terminology.
│
├── assets/
│   ├── images/
│   ├── icons/
│   └── logo/
│
├── .github/
│   └── workflows/
│       ├── tests.yml                           # Run linting and unit tests.
│       ├── quarto-publish.yml                  # Build and deploy the Quarto website.
│       └── notebooks.yml                       # Execute selected notebooks to ensure reproducibility.
│
├── .gitignore                                  # Git ignore rules.
├── .pre-commit-config.yaml                     # Pre-commit hooks.
├── .editorconfig                               # Consistent editor settings across contributors.
│
└── _site/                                      # Generated Quarto website.
```

---

## Educational Philosophy

Each notebook follows a consistent structure to facilitate learning and encourage experimentation.

Typical chapters include:

1. Motivation
2. Theory
3. Visual intuition
4. Python implementation
5. Interpretation
6. Discussion
7. Exercises
8. Further reading

The emphasis is not only on *how* to apply each method, but also on *why* it works and *when* it should be used.

---

## Python Ecosystem

This project primarily uses the following libraries:

- NumPy
- pandas
- Matplotlib
- SciPy
- statsmodels
- scikit-learn
- XGBoost
- LightGBM
- CatBoost
- PyTorch

Additional libraries may be introduced as the project evolves.

---

## Software Engineering Practices

This repository emphasizes reproducibility and maintainability through:

- Modular code organization
- Reusable Python package
- Unit testing
- Type hints
- Automated documentation
- GitHub Actions
- Continuous deployment with Quarto
- Consistent coding style

---

## Quarto Website

All educational content is rendered as a Quarto website.

The website provides:

- Structured navigation
- Interactive notebooks
- Mathematical notation
- Figures and visualizations
- Cross-references
- Bibliography
- Search functionality

---

## Roadmap

The project will be developed incrementally.

- [ ] Foundations
- [ ] Exploratory analysis
- [ ] Statistical foundations
- [ ] Classical forecasting models
- [ ] Feature engineering
- [ ] Machine learning
- [ ] Deep learning
- [ ] Model evaluation
- [ ] End-to-end case studies
- [ ] Advanced forecasting topics

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ianlopezdiaz/time-series-analysis.git
cd time-series-analysis
```

Create the Conda environment:

```bash
conda env create -f environment.yml
conda activate time-series-analysis
```

or install using pip:

```bash
pip install -r requirements.txt
```

---

## Contributing

Suggestions, corrections, and improvements are welcome.

If you find an error or have an idea for expanding the project, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.