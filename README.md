# 🚀 Automation Testing Framework – AutomationExercise.com

This is a Python-based Selenium automation framework built using Pytest and Page Object Model (POM). It covers major test scenarios from https://automationexercise.com.

## ✅ Tools Used

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Git
- Jenkins (optional for CI)
- POM Design Pattern

## 📁 Folder Structure

- `My_Testcases/` – All test_*.py files (tagged: smoke, sanity, regression)
- `POM/` – Page object files
- `conftest.py` – Driver fixture + Screenshot on failure logic
- `requirements.txt` – Dependencies
- `reports/` – HTML test result reports
- `screenshots/` – Captures of failed tests

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2.Run all tests:
pytest My_Testcases/ --html=reports/report.html --self-contained-html -v

3.Run tests by tag:
pytest -m smoke
pytest -m regression
pytest -m sanity