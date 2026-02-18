import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import List, Dict
import random

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

@tool
def consult_demogorgon(complaint: str) -> str:
    """Get the Demogorgon's perspective on a complaint about the Upside Down."""
    responses = [
        f"The Demogorgon tilts its head. It seems confused by '{complaint}'. Perhaps the issue is that you're thinking in three dimensions?",
        f"The Demogorgon makes a sound that might be agreement. It suggests that the problem might be temporal - things work differently in the Upside Down's time.",
        f"The Demogorgon appears to be eating something. It doesn't seem to understand the concept of '{complaint}' - maybe consistency isn't a priority there?"
    ]
    return random.choice(responses)

@tool
def check_hawkins_records(query: str) -> str:
    """Search Hawkins historical records for information."""
    records = {
        "portal": "Records show portals have opened on various dates with no clear pattern. Weather, electromagnetic activity, and unknown factors seem involved.",
        "monsters": "Historical records indicate creatures from the Upside Down behave differently based on environmental factors, time of day, and proximity to certain individuals.",
        "psychics": "Records show that psychic abilities vary greatly. Some individuals can move objects but not see the future, others can see visions but not move things.",
        "electricity": "Hawkins has a history of electrical anomalies. Records suggest a connection between the Upside Down and electromagnetic fields."
    }
    for key, value in records.items():
        if key in query.lower():
            return value
    return f"Records don't contain specific information about '{query}', but they note that many unexplained events have occurred in Hawkins over the years."

@tool
def cast_interdimensional_spell(problem: str, creativity_level: str = "medium") -> str:
    """Suggest a creative interdimensional spell to fix a problem."""
    spells = [
        f"Try chanting 'Beema Beema Beema' three times while holding a Walkman. This might recalibrate the interdimensional frequencies related to: {problem}",
        f"Create a salt circle and place a compass in the center. The magnetic anomalies might help stabilize: {problem}",
        f"Play 'Running Up That Hill' backwards at the exact location of the issue. The temporal resonance could fix: {problem}",
        f"Gather three items: a lighter, a compass, and something personal. Arrange them in a triangle while thinking about: {problem}. The emotional connection might help."
    ]
    return random.choice(spells)

@tool
def gather_party_wisdom(question: str) -> str:
    """Ask the D&D party (Mike, Dustin, Lucas, Will) for their collective wisdom."""
    party_responses = {
        "portal": "Mike: 'Portals are unpredictable, but they usually open near strong emotional events or electromagnetic disturbances.' Dustin: 'Also, they seem to follow some kind of pattern related to the Mind Flayer's activity.'",
        "monsters": "Lucas: 'Demogorgons are territorial but also opportunistic.' Will: 'They can sense fear and strong emotions. Maybe that's why they act differently sometimes.'",
        "psychics": "Mike: 'El's powers seem connected to her emotional state.' Dustin: 'And they're limited by her physical and mental energy. That's probably why she can't do everything.'",
        "electricity": "Lucas: 'The Upside Down seems to interfere with electrical systems.' Dustin: 'But it also creates strange connections. It's like a feedback loop.'"
    }
    for key, response in party_responses.items():
        if key in question.lower():
            return response
    return "The party huddles together. Mike: 'This is a tough one.' Dustin: 'We need more information.' Lucas: 'Let's think about what we know.' Will: 'Maybe we should consult other sources?'"

# Create list of tools
tools = [consult_demogorgon, check_hawkins_records, cast_interdimensional_spell, gather_party_wisdom]

# Tool Usage Tracker (from Step 5)
class ToolUsageTracker:
    def __init__(self):
        self.usage_count = {tool.name: 0 for tool in tools}
        self.tool_sequences = []
    
    def track_usage(self, tool_name: str):
        if tool_name in self.usage_count:
            self.usage_count[tool_name] += 1
        self.tool_sequences.append(tool_name)
    
    def get_statistics(self):
        return {
            "total_tool_calls": sum(self.usage_count.values()),
            "tool_counts": self.usage_count,
            "most_used": max(self.usage_count.items(), key=lambda x: x[1])[0] if self.usage_count else None,
            "tool_sequences": self.tool_sequences
        }

# Sample complaints
complaints = [
    "Why do demogorgons sometimes eat people and sometimes don't?",
    "The portal opens on different days—is there a schedule?",
    "Why can some psychics see the Upside Down and others can't?",
    "Why do creatures and power lines react so strangely together?"
]

print(f"\n{'='*60}")
print("STEP 5: ANALYZING TOOL USAGE")
print(f"{'='*60}\n")

# Initialize tracker
tracker = ToolUsageTracker()

# Test each complaint manually to track tool usage
print("Testing each complaint with relevant tools:\n")

for i, complaint in enumerate(complaints, 1):
    print(f"Complaint {i}: {complaint}")
    print("-" * 40)
    
    # Determine which tools might be relevant
    if "demogorgon" in complaint.lower() or "eat" in complaint.lower():
        print("  ✓ Using consult_demogorgon")
        tracker.track_usage("consult_demogorgon")
        result = consult_demogorgon.invoke({"complaint": complaint})
        print(f"    → {result}")
    
    if "portal" in complaint.lower() or "schedule" in complaint.lower():
        print("  ✓ Using check_hawkins_records")
        tracker.track_usage("check_hawkins_records")
        result = check_hawkins_records.invoke({"query": complaint})
        print(f"    → {result}")
    
    if "psychics" in complaint.lower() or "see" in complaint.lower():
        print("  ✓ Using gather_party_wisdom")
        tracker.track_usage("gather_party_wisdom")
        result = gather_party_wisdom.invoke({"question": complaint})
        print(f"    → {result}")
    
    if "creatures" in complaint.lower() or "power" in complaint.lower() or "electricity" in complaint.lower():
        print("  ✓ Using cast_interdimensional_spell")
        tracker.track_usage("cast_interdimensional_spell")
        result = cast_interdimensional_spell.invoke({"problem": complaint})
        print(f"    → {result}")
    
    print()

# Show analysis
print(f"\n{'='*60}")
print("TOOL USAGE ANALYSIS RESULTS")
print(f"{'='*60}")
stats = tracker.get_statistics()
print(f"\n📊 Total tool calls: {stats['total_tool_calls']}")
print(f"\n📈 Tool usage counts:")
for tool_name, count in stats['tool_counts'].items():
    print(f"   - {tool_name}: {count} times")
print(f"\n⭐ Most used tool: {stats['most_used']}")
print(f"\n📝 Tool sequence (in order used):")
for i, tool in enumerate(stats['tool_sequences'], 1):
    print(f"   {i}. {tool}")

print(f"\n{'='*60}")
print("ANALYSIS SUMMARY")
print(f"{'='*60}")
print("""
Key Observations:
1. The agent (in this case us) chooses tools based on keywords in the complaint
2. Multiple tools can be used for a single complaint
3. Different complaints trigger different tool combinations
4. This shows how a LangChain agent could chain tools together

Comparison with Structured Approaches (LangGraph):
- Freeform (current): Flexible, creative, can use any tool in any order
- Structured (tomorrow's lab): Fixed workflows, predictable, better for repeatable tasks

Pitfalls Experienced:
- Version conflicts with LangChain packages
- Different import paths across versions
- Need to check available functions before coding
""")