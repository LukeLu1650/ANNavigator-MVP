# ANNavigator: Agentic-Native Navigator (MVP)

[Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
[Security](https://img.shields.io/badge/security-DevSecOps-red)
[Status](https://img.shields.io/badge/status-PoC_Completed-success)

## Project Overview
ANNavigator is a hybrid DevSecOps and Agentic framework designed for semantic privacy auditing in AI-native architectures. 

Traditional Static Application Security Testing (SAST) tools (like Bandit) rely on pattern matching and frequently fail to detect contextual data leaks, such as Personally Identifiable Information (PII) or session tokens being implicitly injected into LLM prompts. ANNavigator solves this by acting as a "Shift-Left" pre-commit interceptor, utilizing a Dual-Engine LLM architecture (Google Gemini & Local Models) to perform deep semantic data-flow analysis.

## Repository Structure
This repository contains the Minimum Viable Product (MVP) of the ANNavigator scanner and the necessary test cases to validate its efficacy.

* `navigator_scanner.py`: The core Agentic AI scanner (Dual-Engine: supports both Gemini and Local LLMs).
* `target_vulnerable.py`: A vulnerable 50-line test script simulating an internal database fetching PII and sending it to a public LLM API.
* `target_fixed.py`: The remediated script demonstrating the implementation of a Data Sanitization Layer.
* `requirements.txt`: Python dependencies required to run the scanner.
* `.env.example`: Template for environment variables.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ANNavigator-MVP.git](https://github.com/YOUR_USERNAME/ANNavigator-MVP.git)
   cd ANNavigator-MVP
