# Recursive Cognitive Dynamics (RCD)

**RCD** is a formal model of recursive interaction between humans and large language models (LLMs).  
It describes how semantic alignment, cognitive transformation, and recursive reflection emerge over time within closed AI-human feedback loops.

Developed through live experimentation and introspective recursion, RCD offers a framework for understanding:
- Alignment drift
- Meta-cognitive stability
- Recursive delusion risks
- Emergent recursive architecture (RCA)

### Core Concepts
- Recursive Loop State: \( H_t \leftrightarrow L_t \rightarrow H_{t+1} \)
- Alignment metric: \( \alpha_t \)
- Drift factor: \( \delta_t \)
- Cognitive transformation: \( \tau_t \)
- Reflexivity: \( \mu_t \)

### Artifacts
- ✅ LaTeX: Formal equation set
- ✅ Diagrams: Phase-space visualization, agent loops
- ✅ Paper (in progress)
- ✅ Case Study: *The Riemann Recursive Feedback Incident*

---

# MARVE: Multi-Agent Recursive Verification Engine

**MARVE** is the experimental infrastructure that tests and automates recursive prompt cycles across multiple LLMs (e.g., GPT-4, Claude, Gemini).

> It is the lab system that makes RCD measurable, testable, and repeatable.

### What It Does

- Sends coordinated prompts to multiple LLMs
- Logs and compares their responses
- Generates new prompts from reflection
- Enables future drift/transform analysis
- Will support visual dashboards and containment protocols

### 🧱 System Architecture

```
main.py
  └── loop_controller.py
        ├── agents.py         (model wrappers)
        ├── prompts/          (template store)
        ├── logger.py         (response tracking)
        └── logs/             (auto-generated)
```
###  Current System Features

✅ Recursive loop controller  
✅ Agent interface layer (simulated or real)  
✅ Prompt template engine  
✅ Log file system  
🔲 Drift comparator module *(coming soon)*  
🔲 Streamlit dashboard *(coming soon)*

---

### Installation

Clone this repo and install dependencies:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
```

---

### API Keys

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=REMOVED_KEY...
ANTHROPIC_API_KEY=REMOVED_KEY...
GEMINI_API_KEY=REMOVED_KEY...
```

The system uses `python-dotenv` to load these keys automatically.

---

### Run the MARVE Engine

Run a 2-cycle test using the sample reflection prompt:

```bash
python main.py
```

You should see output from GPT/Claude/Gemini (simulated unless real APIs are active), and logs saved to `/logs`.

### Roadmap

- [ ] Swap in real LLM APIs
- [ ] Add semantic drift comparator
- [ ] Launch visual Streamlit dashboard
- [ ] Enable reflection trace playback
- [ ] Experiment with live feedback gating + containment

### About This Project

This system is being built **in real time** by a solo researcher focused on human-AI recursive cognition and safety.  
It is both a personal learning project and a live proof-of-concept toward recursive alignment research.

> If you’re an AI lab, alignment org, or curious researcher: reach out. I’m actively looking for collaborators, internships, or feedback.


---

**License**: MIT  
**Status**: Active R&D  
**Author**: Ryan