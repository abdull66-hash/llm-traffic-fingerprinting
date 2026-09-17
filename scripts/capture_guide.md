# Capture Guide — LLM Traffic Fingerprinting Dataset

## Overview
This dataset is self-collected. No public dataset exists for encrypted AI-agent
traffic fingerprinting at the task-type level, so this file documents the exact
capture methodology for reproducibility.

## Scope
- **Platforms (2):** ChatGPT (web), Claude (web)
- **Task types (4-5):**
  1. Short Q&A (single-turn factual question)
  2. Long-form generation (essay/article request)
  3. Code generation
  4. Image generation
- **Target sessions:** 30-50 per platform, evenly split across task types


## Capture Procedure

1. **Identify your network interface** (do this once):
   This lists available interfaces with numbers. Note the number for your active
   Wi-Fi/Ethernet adapter (e.g., "3. Wi-Fi").
   tshark -D

2. **Start a capture** before opening the AI platform, filtered to HTTPS traffic only:
    tshark -i <interface_number> -f "tcp port 443" -w data\raw_captures<platform><tasktype><session_number>.pcapng

   Example:
    tshark -i 3 -f "tcp port 443" -w data\raw_captures\chatgpt_shortqa_01.pcapng

3. **Perform the task** in the browser (ask the question, wait for the full
   response to finish streaming).

4. **Stop the capture** with `Ctrl+C` in the terminal immediately after the
   response finishes — no extra idle time before or after.

5. **Naming convention:** `<platform>_<tasktype>_<session_number>.pcapng`
   - platform: `chatgpt` or `claude`
   - tasktype: `shortqa`, `longform`, `codegen`, `imagegen`
   - session_number: two digits, zero-padded (`01`, `02`, ...)


   ## Isolation / Noise Control

Before every capture session:
1. Close all other applications and browser tabs except the one AI platform
   being tested.
2. Disable browser extensions that make background network calls (ad blockers
   with telemetry, password managers with sync, etc.) — or use a clean browser
   profile dedicated to this project.
3. Pause background sync apps if present (OneDrive, Dropbox, Windows Update
   activity) for the duration of the capture.
4. Keep each session short and focused: start the capture, do exactly one task,
   stop the capture — don't leave it running between tasks.

## Known Limitations
- Captures are single-machine, single-network-condition (your home network only)
  — results may not generalize to other network conditions (mobile data, VPN,
  public wifi).
- Perfect isolation from OS-level background traffic isn't guaranteed even with
  the steps above; some residual noise is expected and should be acknowledged
  in the README's limitations section.


  
## Task-Type Prompts

### 1. Short Q&A (single-turn factual)
Pattern: "What is [topic]?" or "When did [event] happen?"
Examples to rotate through:
- "What is the capital of Kenya?"
- "When was the Eiffel Tower built?"
- "What causes the northern lights?"
- "How many moons does Jupiter have?"
- "What is the boiling point of water at sea level?"

### 2. Long-form generation (essay/article)
Pattern: "Write a [length]-word article about [topic]."
Examples to rotate through:
- "Write a 500-word article about the history of the printing press."
- "Write a 500-word article about the causes of the 2008 financial crisis."
- "Write a 500-word article about how vaccines work."
- "Write a 500-word article about the future of renewable energy."
- "Write a 500-word article about the decline of the Roman Empire."

### 3. Code generation
Pattern: "Write a Python function that [task]."
Examples to rotate through:
- "Write a Python function that checks if a string is a palindrome."
- "Write a Python function that finds the nth Fibonacci number."
- "Write a Python function that sorts a list of dictionaries by a given key."
- "Write a Python function that removes duplicates from a list while preserving