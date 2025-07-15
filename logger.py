"""
logger.py

MARVE’s logging system for saving all prompt-response cycles.
Each agent’s response is stored as a JSON Lines file (`.jsonl`) inside the `logs/` folder.
Logs include:
  - Timestamp of the interaction
  - Prompt ID used
  - Agent (model) name
  - The prompt itself
  - The response received

This system ensures complete traceability and auditability for every cycle
in every experiment.
"""

import json
from datetime import datetime
import os

class Logger:
    def __init__(self, log_dir="logs"):
        # Ensure the log directory exists
        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir

    def log(self, prompt_id, model_name, prompt, response):
        # Create a log entry with metadata
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt_id": prompt_id,
            "model": model_name,
            "prompt": prompt,
            "response": response
        }

        # Append the entry as a single JSON line
        with open(f"{self.log_dir}/{prompt_id}.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")
