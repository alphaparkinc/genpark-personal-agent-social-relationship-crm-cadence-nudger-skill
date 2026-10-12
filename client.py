"""
Personal Agent Social Relationship CRM & Dunbar Cadence Nudger (Zero External Dependencies)
Tracks Dunbar social circle cadence thresholds and generates episodic reconnection prompts.
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
import time
import math
import hashlib
import json
from typing import Dict, Any, List, Optional

DUNBAR_CADENCE_DAYS = {
    "INNER_CIRCLE_5": 7,
    "CLOSE_FRIENDS_15": 21,
    "KEY_NETWORK_50": 60,
    "ACTIVE_NETWORK_150": 120
}

class PersonalAgentSocialRelationshipCRMCadenceNudger:
    def __init__(self):
        pass

    def evaluate_relationship_cadence(self, contacts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculates tie-strength health and identifies overdue contacts across Dunbar tiers."""
        evaluated = []
        overdue_count = 0

        for c in contacts:
            name = c.get("name", "Contact")
            tier = str(c.get("dunbar_tier", "KEY_NETWORK_50")).upper()
            days_elapsed = int(c.get("days_since_last_contact", 30))
            target_cadence = DUNBAR_CADENCE_DAYS.get(tier, 60)

            # Exponential tie warmth score [0..100]
            warmth_score = round(100.0 * math.exp(-0.693147 * (days_elapsed / max(1.0, float(target_cadence)))), 1)
            is_overdue = days_elapsed > target_cadence
            if is_overdue:
                overdue_count += 1

            evaluated.append({
                "name": name,
                "dunbar_tier": tier,
                "target_cadence_days": target_cadence,
                "days_since_last_contact": days_elapsed,
                "tie_warmth_score": warmth_score,
                "is_overdue": is_overdue,
                "overdue_ratio": round(days_elapsed / max(1.0, float(target_cadence)), 2),
                "last_topic_memory": c.get("last_topic_memory", "recent projects"),
                "preferred_channel": c.get("preferred_channel", "WeChat / WhatsApp")
            })

        evaluated.sort(key=lambda x: (x["is_overdue"], x["overdue_ratio"]), reverse=True)
        return {
            "total_contacts": len(contacts),
            "overdue_relationships_count": overdue_count,
            "prioritized_contacts": evaluated
        }

    def synthesize_reconnection_nudges(self, contacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generates context-grounded outreach drafts for overdue contacts."""
        analysis = self.evaluate_relationship_cadence(contacts)
        nudges = []

        for item in analysis["prioritized_contacts"]:
            if not item["is_overdue"]:
                continue
            topic = item["last_topic_memory"]
            draft = (
                f"Hey {item['name']}! Been thinking about our last chat regarding {topic}. "
                f"Hope things have been going smoothly—would love to catch up over a quick call or coffee soon!"
            )
            nudges.append({
                "recipient": item["name"],
                "dunbar_tier": item["dunbar_tier"],
                "channel": item["preferred_channel"],
                "days_overdue": item["days_since_last_contact"] - item["target_cadence_days"],
                "tie_warmth_score": item["tie_warmth_score"],
                "suggested_message_draft": draft
            })

        return nudges
