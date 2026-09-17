## [Paper Title]
- Authors / Year / Venue:
- Core claim/method (paper's own words, paraphrased):
- Dataset/domain used:
- Relation to my project:
- My interpretation (separate from the paper's claim):

## [Website Fingerprinting at Internet Scale]

- Andriy Panchenko, Fabian Lanze, Andreas Zinnen, Martin Henze, Jan Pennekamp, Klaus Wehrle, and Thomas Engel / 2016 / San Diego, CA, USA 

- They claim that they're presenting "a novel website fingerprinting
attack. Based on a simple and comprehensible idea, our approach
outperforms all state-of-the-art methods in terms of classification
accuracy while being computationally dramatically more efficient."

- "In order to evaluate the severity of the website fingerprinting
attack in reality, we collected the most representative dataset that
has ever been built, where we avoid simplified assumptions made
in the related work regarding selection and type of webpages and
the size of the universe".... 
Dataset A is called ALEXA10 
Dataset B is called RND-WWW

-This is related to my project in a way that, I also classifies encrypted traffic using meta-data

- Notes: This paper really does well and will be very usefull because it clearly mentions all what we're looking for in the abstract ("The website fingerprinting attack aims to identify
the content (i.e., a webpage accessed by a client) of encrypted
and anonymized connections by observing patterns of data flows
such as packet size and direction. This attack can be performed
by a local passive eavesdropper – one of the weakest adversaries
in the attacker model of anonymization networks such as Tor")
They clearly state "for the first time we show that no existing method – including our own scales when applied in realistic settings."


## [Website Fingerprinting and Identification Using Ordered Feature Sequences]

- Liming Lu, Ee-Chien Chang & Mun Choon Chan / 2010 / National University of Singapore

- They claim that they're pointing out that packet ordering information, though noisy, can be utilized to enhance website fingerprinting. In addition, traces of the ordering information remain even under traffic morphing and they can be extracted for identification
They use passive traffic analysis to fingerprint websites.

-Datasets: They said they prepared 3 datasets on OpenVPN namely, static50, dynamic150, and OpenVPN1000. (We'll need to look at the explanations or contents of each dataset) AND
OpenSSH2000


**************************************************
## LLMs Have Rhythm: Fingerprinting Large Language Models Using Inter-Token Times and Network Traffic Analysis
- Authors / Year / Venue: Alhazbi, Hussain, Oligeri, Papadimitratos (2025), IEEE Open Journal of the Communications Society
- Core claim/method: Autoregressive LLMs produce a distinctive timing "rhythm" in Inter-Token Times (ITTs) that survives network transmission even encrypted. A deep learning pipeline trained on ITT + packet timing features identifies which of 16 SLMs or 10 proprietary LLMs is being used, staying accurate across GPU/CPU, LAN, remote, and VPN conditions.
- Dataset/domain used: Self-collected traces from 16 open-source SLMs (via Ollama) and 10 proprietary LLMs (OpenAI, Claude, Mistral), across multiple network/hardware conditions.
- Relation to my project: Overlaps with the "which AI app" half of Project 1, but stops at model/app identity — doesn't classify what task is being performed. This is the gap my project extends into.
- My interpretation: Their signal depends entirely on streaming (ITTs only exist because tokens arrive one at a time). This means the method — and any task-type extension of it — likely breaks against providers that disable streaming or batch tokens before sending, which the paper itself acknowledges as a limitation.

## Exposing LLM User Privacy via Traffic Fingerprint Analysis: A Study of Privacy Risks in LLM Agent Interactions
- Authors / Year / Venue: Zhang, Deng, Gu, Chen, Xu, Li, Wu (2025), arXiv preprint (venue not yet confirmed as peer-reviewed)
- Core claim/method: LLM agents that plan, call tools, and produce multimodal output leave distinctive traffic fingerprints beyond plain text chat. Their AgentPrint framework identifies which agent is in use (F1 = 0.866) and infers user attributes like occupation from aggregated agent usage (up to 73.9% top-3 accuracy).
- Dataset/domain used: ~50 monitored custom-GPT agents (7.3k traces) plus 166 unmonitored agents, covering tool-invocation behaviors (web search, code interpreter, image generation).
- Relation to my project: Shows agent-level *behavior* classification works, but their granularity is behavior-category (which tool ran), not fine-grained prompt-task type (e.g. code-gen vs. long-form writing within one platform) — and it's confined to one agent ecosystem rather than compared across competing platforms.
- My interpretation: The 73.9% top-3 occupation-inference figure is their most striking claim, but the gap between simulated (73.9%) and real-user (69.1%) accuracy suggests the technique is less reliable outside a lab setting than the headline number implies — worth citing that gap, not just the top-line number, if I reference this in my README.

## Inferring the Source of Encrypted HTTP Connections
- Authors / Year / Venue: Liberatore, M. & Levine, B.N. (2006), ACM CCS
- Core claim/method: One of the earliest demonstrations that encrypted HTTP/SSL traffic leaks the identity of the visited site purely from packet-length profiles — no payload needed. Used a Naive Bayes classifier and Jaccard-coefficient similarity over packet-length sets, tested on ~2,000 websites.
- Dataset/domain used: Self-collected traces of 2,000 websites over encrypted (SSL) HTTP connections.
- Relation to my project: This is the founding proof-of-concept for the entire technique family my project sits in — "encrypted traffic leaks identity via size/timing metadata alone." Everything from CUMUL to ITT fingerprinting descends from this idea.
- My interpretation: The classifier is simple by modern standards (no deep learning, no timing features — just size sets), which is useful context: it shows the core privacy leak isn't about sophisticated ML, it's inherent to how encrypted traffic behaves. Worth citing to frame my project's problem statement, not its method.

## Website Fingerprinting at Internet Scale
- Authors / Year / Venue: Panchenko, A. et al. (2016), NDSS
- Core claim/method: Introduced CUMUL, a cumulative packet-length feature representation, paired with an SVM classifier, and showed website fingerprinting works in an open-world setting (i.e., the attacker doesn't know the full universe of possible sites) at a much larger scale than prior work — 300,000+ web pages.
- Dataset/domain used: Tor traffic traces across 300,000+ pages, open-world and closed-world evaluation splits.
- Relation to my project: The open-world vs. closed-world distinction matters directly for me — a real "which AI app / which task" classifier also needs to handle traffic it's never seen (e.g., non-AI background browsing), not just distinguish among known classes.
- My interpretation: CUMUL is a strong, still-cited baseline feature representation almost a decade later, which suggests my project's feature engineering step should benchmark against something CUMUL-like before reaching for deep learning.

## Adaptive Encrypted Traffic Fingerprinting With Bi-Directional Dependence
- Authors / Year / Venue: Al-Naami, K. et al. (2016), ACM ACSAC
- Core claim/method: Introduced BIND (bi-directional burst dependencies in packet size and timing) as a feature set, and ADABIND, an adaptive model that retrains to handle concept drift — the fact that traffic patterns for the same site/app change over time (browser updates, CDN changes, etc.).
- Dataset/domain used: Website fingerprinting (WFIN) and mobile app fingerprinting (AFIN) traces over HTTPS and Tor.
- Relation to my project: Directly relevant to a limitation I'll likely hit — AI chatbot UIs and APIs change frequently (model updates, UI redesigns), so a classifier trained today may degrade in weeks. ADABIND's adaptive retraining approach is a candidate mitigation to mention in my own limitations/future-work section.
- My interpretation: This paper predates LLM-specific fingerprinting entirely, so it's evidence that "concept drift" is a known, general problem in this field — not something unique to AI traffic — which strengthens my Related Work framing rather than being a direct method I'll reuse.