# genpark-personal-agent-social-relationship-crm-cadence-nudger-skill

[![GenPark AI](https://img.shields.io/badge/GenPark_AI-www.genpark.ai-blue.svg)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark_Company_92955550-0077B5.svg)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Dependencies](https://img.shields.io/badge/dependencies-0%20(Pure%20Stdlib)-brightgreen.svg)](requirements.txt)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-purple.svg)](mcp_server.py)

Proactive Personal Agent Social Relationship CRM & Dunbar Cadence Nudger. Models concentric Dunbar social circles (Inner Circle 5, Close 15, Key Network 50, Active 150), tracks interaction recency and tie-strength decay across WhatsApp, WeChat, and Email, and synthesizes personalized episodic reconnection nudges.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
"""Example usage for PersonalAgentSocialRelationshipCRMCadenceNudger."""
import sys
import json
from client import PersonalAgentSocialRelationshipCRMCadenceNudger

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== Today AI / Meta Muse Social Relationship CRM Cadence Nudger Demo ===")
    nudger = PersonalAgentSocialRelationshipCRMCadenceNudger()

    network = [
        {
            "name": "Dr. Aris Thorne",
            "dunbar_tier": "CLOSE_FRIENDS_15",
            "days_since_last_contact": 38,
            "last_topic_memory": "his robotics lab paper at ICRA",
            "preferred_channel": "WhatsApp"
        },
        {
            "name": "Sophia Lin",
            "dunbar_tier": "INNER_CIRCLE_5",
            "days_since_last_contact": 3,
            "last_topic_memory": "weekend hiking trip",
            "preferred_channel": "WeChat"
        }
    ]

    print("\n--- 1. Evaluating Dunbar Circle Tie-Strength Warmth ---")
    report = nudger.evaluate_relationship_cadence(network)
    for c in report["prioritized_contacts"]:
        print(f"  {c['name']} ({c['dunbar_tier']}) -> Warmth: {c['tie_warmth_score']}/100 | Overdue: {c['is_overdue']}")

    print("\n--- 2. Synthesizing Episodic Reconnection Nudges ---")
    nudges = nudger.synthesize_reconnection_nudges(network)
    for n in nudges:
        print(f"  [{n['channel']} -> {n['recipient']}]: {n['suggested_message_draft']}")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
