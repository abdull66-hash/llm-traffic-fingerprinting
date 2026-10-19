# Fingerprinting AI Chatbot Traffic: Platform and Task-Type Inference from Encrypted Metadata

**Status: in progress.** Data collection is under way. No results are reported yet.

## Research question
Using only packet size, direction and timing metadata, can a classifier identify which AI platform a user is on and which type of task they are performing (short Q&A, long-form generation, code generation, image generation), and does this generalize across platforms?

## Literature gap
Prior work shows that encrypted traffic leaks identity through metadata. Recent papers extend this to LLMs: identifying which model is in use, and which agent is running. Fine-grained task-type inference compared across competing platforms is less explored, and that is the gap this project targets. This is an extension of established ideas, not a new phenomenon.

## Related work
- Liberatore & Levine (2006) showed that encrypted HTTP traffic reveals the visited site from packet-length profiles alone, the foundation of this technique family.
- Panchenko et al. (2016) introduced the CUMUL features and evaluated website fingerprinting at large scale in an open-world setting.
- Al-Naami et al. (2016) addressed concept drift in traffic fingerprinting with an adaptive model, which is relevant because chatbot interfaces change often.
- Alhazbi et al. (2025) fingerprinted LLMs from inter-token timing, identifying which model is in use but not what task is being performed.
- Zhang et al. (2025, arXiv preprint) showed that LLM agents leave distinguishable traffic fingerprints, at the level of which agent or tool is used rather than fine-grained task type.

Full notes are in `notes.md`, and citations are in `references.md`.

## Approach
1. Capture my own encrypted sessions (Wireshark/TShark) on two platforms across four task types, using a fixed prompt bank.
2. Extract metadata-only features (sizes, direction, inter-arrival times, bursts).
3. Train baseline classifiers (Random Forest, SVM) for platform and task type.
4. Test cross-platform generalization.

Methodology and prompts are documented in `scripts/capture_guide.md`, and sessions are logged in `data/processed/session_log.md`.

## Ethics
Defensive, awareness-focused research. Only my own traffic is captured. Only metadata is analyzed, with no payload inspection. This is not a surveillance tool.

## Limitations (so far)
Small self-collected dataset, a single machine, and captures from a small number of network conditions.

## Setup
```
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```
Requires Wireshark/TShark with Npcap installed.