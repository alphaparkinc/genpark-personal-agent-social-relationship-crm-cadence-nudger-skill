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
