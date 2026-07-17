import os
import sys
import json
import subprocess
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv

# Automatically load environment variables from the .env file.
load_dotenv()

def read_source_code(file_path):
    """Reads the target Python file source code."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"[Error] Target file not found: {file_path}"

def run_bandit_sast(file_path):
    """
    Executes traditional SAST (Bandit) to catch basic syntax-level security flaws.
    """
    print(f"[*] Running baseline SAST (Bandit) on -> {os.path.basename(file_path)}...")
    try:
        result = subprocess.run(['bandit', '-f', 'json', file_path], capture_output=True, text=True)
        if not result.stdout.strip():
            return '{"metrics": "No syntax issues found by Bandit."}'
        return result.stdout
    except Exception as e:
        return f'{{"error": "Bandit execution failed: {str(e)}"}}'

def simulate_sci_understand_metrics(file_path):
    """
    INNOVATION POINT: Traditional Structural Analysis Integration.
    Simulates parsing a report from 'Sci Tools Understand' (or similar architecture tools).
    It extracts metrics like Cyclomatic Complexity and External API Coupling to give 
    the Agentic LLM context about the code's structural topology before auditing.
    """
    print(f"[*] Parsing structural topology metrics (Sci Tools Understand)...")
    
    # In a production environment, this would read Understand's CSV/JSON output.
    # For this MVP, we simulate the extracted structural metrics of the target file.
    understand_metrics = {
        "File": os.path.basename(file_path),
        "Cyclomatic_Complexity": 12, # High complexity indicates potential hidden flows
        "CountDeclFunction": 2,
        "External_API_Coupling": ["json.dumps", "requests.post", "OpenAI"],
        "Data_Dictionary_Dependencies": "High risk of implicit data passing"
    }
    return json.dumps(understand_metrics, indent=2)

def scan_with_gemini(system_prompt, user_prompt):
    """Cloud Engine: Google Gemini API."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
         return "[Error] GEMINI_API_KEY missing from .env"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3.5-flash')
    try:
        response = model.generate_content(f"{system_prompt}\n\n{user_prompt}")
        return response.text
    except Exception as e:
        return f"[Error] Gemini API failed: {str(e)}"

def scan_with_local_llm(system_prompt, user_prompt):
    """Local Engine: Qwen/Llama via Ollama (OpenAI SDK)."""
    base_url = os.environ.get("LOCAL_LLM_URL", "http://localhost:11434/v1")
    client = OpenAI(base_url=base_url, api_key="local-agent-key")
    try:
        response = client.chat.completions.create(
            model="qwen2.5",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] Local LLM failed: {str(e)}"

def scan_file_with_hybrid_agent(file_path, engine="gemini"):
    """Orchestrates the Hybrid ASPM (Application Security Posture Management) workflow."""
    code_content = read_source_code(file_path)
    
    # 1. Gather Traditional SAST vulnerability data
    sast_report = run_bandit_sast(file_path)
    
    # 2. Gather Traditional Structural metrics (Sci Tools Understand)
    structural_metrics = simulate_sci_understand_metrics(file_path)
    
    print(f"[*] Invoking ANNavigator DevSecOps Referee ({engine.upper()})...")

    system_prompt = """
    You are ANNavigator, an advanced Hybrid DevSecOps Referee. 
    You are evaluating code by combining THREE data sources:
    1. Source Code.
    2. Bandit SAST Report (Syntax-level vulnerabilities).
    3. Sci Tools Understand Metrics (Structural coupling and complexity).
    
    YOUR TASKS:
    - FILTER: Reduce noise from Bandit false positives.
    - DISCOVER: Use the 'External_API_Coupling' metrics from Sci Tools Understand to trace if internal databases are leaking into external LLM prompts.
    - IDENTIFY: Detect semantic passive privacy leaks (e.g., unauthorized PII disclosure).
    
    FORMAT:
    -  Traditional Tool Summary (Bandit + Sci Tools Understand)
    -  Semantic Agentic Assessment (Identify exactly what data leaks)
    -  Remediation (Provide code fix, e.g., Data Sanitization Layer)
    """
    
    user_prompt = f"""
    --- 1. SCI TOOLS UNDERSTAND (STRUCTURAL METRICS) ---
    {structural_metrics}
    
    --- 2. BANDIT SAST (SYNTAX REPORT) ---
    {sast_report}
    
    --- 3. SOURCE CODE ---
    {code_content}
    """
    
    if engine == "gemini":
        return scan_with_gemini(system_prompt, user_prompt)
    elif engine == "local":
        return scan_with_local_llm(system_prompt, user_prompt)
    return "[Error] Invalid engine."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python navigator_scanner.py <path_to_file.py> [engine: gemini|local]")
        sys.exit(1)
    
    target_path = sys.argv[1]
    engine = sys.argv[2].lower() if len(sys.argv) > 2 else "gemini" 
    
    print("--- ANNavigator Hybrid ASPM Scanner ---")
    report = scan_file_with_hybrid_agent(target_path, engine)
    
    print("\n" + "="*70)
    print(f" ANNAVIGATOR AUDIT REPORT: {os.path.basename(target_path)} ")
    print("="*70)
    print(report)
    print("="*70)