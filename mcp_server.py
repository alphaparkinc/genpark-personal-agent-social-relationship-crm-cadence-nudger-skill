"""MCP Server for Personal Agent Social Relationship CRM Cadence Nudger."""
import sys
import json
import time
from client import PersonalAgentSocialRelationshipCRMCadenceNudger

nudger = PersonalAgentSocialRelationshipCRMCadenceNudger()

def handle_call_tool(params):
    name = params.get("name")
    args = params.get("arguments", {})
    if name != "manage_personal_relationship_cadence":
        raise ValueError(f"Unknown tool: {name}")

    action = args.get("action", "synthesize_reconnection_nudges")
    contacts = args.get("contacts", [])

    if action == "evaluate_relationship_cadence":
        return nudger.evaluate_relationship_cadence(contacts)
    elif action == "synthesize_reconnection_nudges":
        return {"nudges": nudger.synthesize_reconnection_nudges(contacts)}
    else:
        raise ValueError(f"Invalid action: {action}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Running self-test...")
        contacts = [
            {"name": "Elena Vance", "dunbar_tier": "CLOSE_FRIENDS_15", "days_since_last_contact": 45, "last_topic_memory": "her Tokyo marathon prep", "preferred_channel": "WhatsApp"},
            {"name": "Marcus Chen", "dunbar_tier": "KEY_NETWORK_50", "days_since_last_contact": 12, "last_topic_memory": "Series B fundraising", "preferred_channel": "WeChat"}
        ]
        nudges = nudger.synthesize_reconnection_nudges(contacts)
        assert len(nudges) == 1
        assert nudges[0]["recipient"] == "Elena Vance"
        assert "Tokyo marathon prep" in nudges[0]["suggested_message_draft"]
        print("Self-test PASSED!")
        sys.exit(0)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            msg_id = req.get("id")
            method = req.get("method")
            if method == "initialize":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "serverInfo": {"name": "PersonalAgentSocialRelationshipCRMCadenceNudger", "version": "1.0.0"},
                        "capabilities": {"tools": {}}
                    }
                }
            elif method == "tools/list":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "tools": [{
                            "name": "manage_personal_relationship_cadence",
                            "description": "Evaluate Dunbar tier tie-strength decay, identify overdue relationships, and synthesize personalized reconnection messages.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "action": {"type": "string", "enum": ["evaluate_relationship_cadence", "synthesize_reconnection_nudges"]},
                                    "contacts": {"type": "array"}
                                },
                                "required": ["action"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                res = handle_call_tool(req.get("params", {}))
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
                }
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
            print(json.dumps(resp), flush=True)
        except Exception as e:
            err_resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err_resp), flush=True)

if __name__ == "__main__":
    main()
