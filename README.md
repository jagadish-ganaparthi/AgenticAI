
# AgenticAI Documentation

## Project Overview
AgenticAI is a cutting-edge framework designed to empower multi-tool cybersecurity agents capable of automating a range of security tasks. The project aims to enhance digital security by utilizing advanced tools to analyze and mitigate potential threats.

## Installation Instructions
To set up the AgenticAI project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jagadish-ganaparthi/AgenticAI.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd AgenticAI
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

## Architecture Description
The AgenticAI architecture is centered around a multi-tool cybersecurity agent that integrates several specialized tools to ensure comprehensive threat detection and response.

### Tools Overview
1. **URL Checker**: This tool verifies the safety of URLs by checking against a myriad of threat intelligence sources.

2. **Phishing Detector**: Utilizes machine learning algorithms to assess the likelihood that a given URL is part of a phishing attempt.

3. **Malware Detector**: Scans files and URLs for known malware signatures to prevent infections.

4. **Threat Score Calculator**: Evaluates potential threats based on various factors, providing an aggregate risk score for URLs and files.

## Usage Examples
- **Check a URL**:
   ```python
   result = url_checker.check("https://example.com")
   print(result)
   ```

- **Detect Phishing**:
   ```python
   phishing_result = phishing_detector.detect("https://phishing-example.com")
   print(phishing_result)
   ```

- **Scan for Malware**:
   ```python
   malware_result = malware_detector.scan(file_path)
   print(malware_result)
   ```

- **Calculate Threat Score**:
   ```python
   threat_score = threat_score_calculator.calculate("https://suspicious-site.com")
   print(threat_score)
   ```

## Agent Usage of the ADK Framework with Gemini 2.5 Flash Model
The AgenticAI leverages the ADK framework to facilitate interaction with the Gemini 2.5 Flash model, enabling robust and efficient threat detection and response capabilities. Through this integration, the agent can dynamically access advanced analysis tools and algorithms, ensuring optimal performance in identifying and mitigating threats.

#How ADK web works
<img width="1855" height="991" alt="image" src="https://github.com/user-attachments/assets/435646b0-ccc8-42d7-9448-659673061525" />

Event level tracing
<img width="1852" height="949" alt="image" src="https://github.com/user-attachments/assets/b32cf6be-8c78-4a20-99aa-91032aaf6a9f" />

