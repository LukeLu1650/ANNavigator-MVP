# ANNavigator: Agentic-Native Navigator (MVP)

[Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
[Security](https://img.shields.io/badge/security-DevSecOps-red)
[Status](https://img.shields.io/badge/status-PoC_Completed-success)

## Project Overview
ANNavigator is an advanced Hybrid DevSecOps framework designed for semantic privacy auditing within AI-native software architectures. 

Building upon the concept of **"CyberDevOps"** (an extreme shifting-left architecture), ANNavigator pioneers an AI-native Application Security Posture Management (ASPM) approach. Traditional SAST tools lack the semantic awareness to trace data from internal databases to external AI prompts. To solve this, ANNavigator ingests output from structural tools (**Sci Tools Understand**) and SAST scanners (**Bandit**), leveraging a **Dual-Engine LLM** (Cloud/Local) to act as a "Referee" and perform deep semantic data-flow analysis.

## Repository Structure
This repository contains the Minimum Viable Product (MVP) of the ANNavigator scanner and the necessary test cases to validate its efficacy.

* `navigator_scanner.py`: The core Agentic AI scanner (Dual-Engine: supports both Gemini and Local LLMs). It simulates the ingestion of Sci Tools Understand metrics and orchestrates Bandit SAST.
* `requirements.txt`: Python dependencies required to run the scanner.
* `.env.example`: Template for environment variables.
## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/LukeLu1650/ANNavigator-MVP.git](https://github.com/LukeLu1650/ANNavigator-MVP.git)
   cd ANNavigator-MVP
