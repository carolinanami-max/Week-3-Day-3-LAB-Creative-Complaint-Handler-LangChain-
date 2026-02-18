import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import random

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

@tool
def consult_demogorgon(question: str) -> str:
    """Ask about Demogorgon behavior, diet, habits, or biology."""
    
    responses = {
        "diet": "Demogorgons are opportunistic predators. They primarily hunt living creatures but are also drawn to strong emotional energy. In the Upside Down, they seem to survive on whatever they can find - small creatures, lost travelers, and sometimes just the psychic energy of fear.",
        "behavior": "Demogorgons are territorial but also curious. They're drawn to light, sound, and strong emotions. Their behavior is unpredictable because they're not just animals - they're connected to the Mind Flayer's hive mind.",
        "weakness": "Demogorgons are vulnerable to fire, bright lights, and loud noises. They can be wounded by conventional weapons but heal quickly. The best defense is to avoid attracting their attention in the first place.",
        "default": "Demogorgons are creatures from the Upside Down. They're humanoid in shape but with a face that opens like a flower to reveal rows of teeth. They have no eyes but seem to sense prey through some combination of sound, vibration, and psychic energy."
    }
    
    for key, response in responses.items():
        if key in question.lower():
            return response
    
    return responses["default"]

@tool
def check_hawkins_records(question: str) -> str:
    """Ask about Hawkins history, the lab, past events, or characters."""
    
    responses = {
        "lab": "Hawkins National Laboratory is a Department of Energy facility that actually conducted secret experiments related to the Upside Down. Dr. Brenner ran experiments on children with psychic abilities, including Eleven. The lab had a massive gate to the Upside Down in its lower levels.",
        "portal": "The first known portal to the Upside Down was opened by Eleven in 1983 when she made contact with the Demogorgon. Since then, portals have appeared sporadically, often triggered by high emotional energy or disturbances in the fabric between dimensions.",
        "will": "Will Byers was the first known victim of the Demogorgon. He survived by hiding in the Upside Down for a week, communicating with his mother through Christmas lights. His experience left him with a connection to the Mind Flayer.",
        "eleven": "Eleven (El) is a psychic with telekinetic and extrasensory powers. She was born with these abilities, which were amplified by Dr. Brenner's experiments. She opened the first gate and has closed it twice.",
        "default": "Hawkins, Indiana has been the epicenter of Upside Down activity since 1983. Key locations include the Lab, the Byers house, the Starcourt Mall, and the Creel House. The town has survived multiple supernatural threats thanks to a group of kids and some brave adults."
    }
    
    for key, response in responses.items():
        if key in question.lower():
            return response
    
    return responses["default"]

@tool
def cast_interdimensional_spell(question: str) -> str:
    """Get creative solutions or spells for dealing with Upside Down problems."""
    
    spells = {
        "portal": "To locate or close a portal: Take a compass, a walkie-talkie tuned to static, and a photograph of someone you love. At the exact spot where the compass goes haywire, bury the photograph while saying the person's name three times. The emotional connection should stabilize or seal the portal.",
        "demogorgon": "To repel a Demogorgon: Create a circle of salt mixed with crushed eggshells. Light seven candles around it and play 'Should I Stay or Should I Go' at maximum volume. The combination of light, sound, and protective barriers confuses their senses.",
        "mindflayer": "To protect against the Mind Flayer: Wear something made of iron (horseshoe, nails, etc.) and keep a flame nearby. The Mind Flayer avoids intense heat and is disrupted by iron - ancient folklore about fairies actually applies here.",
        "default": "When dealing with the Upside Down, remember these rules: 1) Light protects you, 2) Emotional connections create pathways, 3) What happens in Hawkins doesn't stay in Hawkins, 4) Trust the kids - they've seen more than most adults."
    }
    
    for key, response in spells.items():
        if key in question.lower():
            return response
    
    return spells["default"]

@tool
def gather_party_wisdom(question: str) -> str:
    """Ask Mike, Dustin, Lucas, or Will for their advice and experiences."""
    
    party_advice = {
        "demogorgon": "Dustin: 'Demogorgons are like sharks - if you act scared, they sense it. Stand your ground, make noise, and use light.' Mike: 'They can track you through emotions, so try to stay calm.'",
        "portal": "Lucas: 'Portals are like wounds in reality. They can heal, but it takes time or someone with powers to close them.' Will: 'The Upside Down feels colder near portals. You can sense them if you pay attention.'",
        "mindflayer": "Will: 'The Mind Flayer... it's like a shadow that wants in your head. Don't let it. Think of happy things, think of your friends.' Mike: 'Heat hurts it. Fire, steam, anything hot.'",
        "vecna": "Dustin: 'Vecna uses your trauma against you. The more you dwell on your worst memories, the stronger he gets.' Lucas: 'Music helps. It breaks his hold somehow.'",
        "default": "The party huddles to discuss your question. Dustin adjusts his hat: 'Look, we've faced a lot of weird stuff. The key is to stick together, trust your instincts, and remember that normal rules don't always apply.' Mike nods: 'And if you hear someone calling your name when you're alone - don't answer.'"
    }
    
    for key, response in party_advice.items():
        if key in question.lower():
            return response
    
    return party_advice["default"]

# List of tools for compatibility with your existing code
tools = [consult_demogorgon, check_hawkins_records, cast_interdimensional_spell, gather_party_wisdom]

# Tool Usage Tracker (keeping your existing code below)
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
        result = consult_demogorgon.invoke({"question": complaint})
        print(f"    → {result}")
    
    if "portal" in complaint.lower() or "schedule" in complaint.lower():
        print("  ✓ Using check_hawkins_records")
        tracker.track_usage("check_hawkins_records")
        result = check_hawkins_records.invoke({"question": complaint})
        print(f"    → {result}")
    
    if "psychics" in complaint.lower() or "see" in complaint.lower():
        print("  ✓ Using gather_party_wisdom")
        tracker.track_usage("gather_party_wisdom")
        result = gather_party_wisdom.invoke({"question": complaint})
        print(f"    → {result}")
    
    if "creatures" in complaint.lower() or "power" in complaint.lower() or "electricity" in complaint.lower():
        print("  ✓ Using cast_interdimensional_spell")
        tracker.track_usage("cast_interdimensional_spell")
        result = cast_interdimensional_spell.invoke({"question": complaint})
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