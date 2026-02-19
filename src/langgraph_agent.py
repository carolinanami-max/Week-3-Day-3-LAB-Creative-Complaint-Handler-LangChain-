import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessage
import random

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Define the tools (complaint handling style)
@tool
def consult_demogorgon(complaint: str) -> str:
    """File a complaint to the Demogorgon about Upside Down issues. Use this for ANY complaint mentioning Demogorgons."""
    
    responses = {
        "diet": "🔴 DEMOGORGON COMPLAINT #D-001: Dietary Concerns\n\nThe Demogorgon Customer Service Desk acknowledges your complaint about dietary inconsistencies. Unfortunately, the Upside Down does not have an FDA. Your complaint has been filed in the void. Next!",
        "behavior": "🔴 DEMOGORGON COMPLAINT #D-002: Behavioral Issues\n\nThank you for your complaint about Demogorgon behavior. The Demogorgon Union is currently in negotiations. Please hold. *eerie screeching sounds*",
        "noise": "🔴 DEMOGORGON COMPLAINT #D-003: Noise Violation\n\nThe Demogorgon has been issued a noise violation citation. It ate the citation. We're issuing another one. This is an ongoing issue.",
        "default": f"🔴 DEMOGORGON COMPLAINT #{random.randint(100,999)}\n\nThe Demogorgon has received your complaint: '{complaint}'. It stares at you blankly. A form appears in your hand written in an unknown language. The Demogorgon vanishes. Case status: LOST IN THE UPSIDE DOWN."
    }
    
    for key, response in responses.items():
        if key in complaint.lower():
            return response
    
    return responses["default"]

@tool
def check_hawkins_records(complaint: str) -> str:
    """Check official Hawkins records regarding a complaint. Use this for complaints about history, the lab, portals, or past events."""
    
    responses = {
        "portal": "📁 HAWKINS RECORDS #1983-11-06: Portal Schedule Complaints\n\nRegarding irregular portal schedules. Hawkins Records Office notes: 'Portals operate on their own timeline. We've given up trying to schedule them. Please take a number and wait. Your number is 847.'",
        "demogorgon": "📁 HAWKINS RECORDS #1983-11-07: Demogorgon Property Damage\n\nStatus: UNDER REVIEW. Note: 'We're still trying to find the right insurance form for interdimensional claims. The Demogorgon is not on the lease.'",
        "electricity": "📁 HAWKINS RECORDS #1984-07-04: Power Fluctuation Complaints\n\nHawkins Electric: 'It's not our fault. It's the Upside Down. We bill them separately. Their payment history is spotty.'",
        "vecna": "📁 HAWKINS RECORDS #1986-03-21: Vecna Complaints\n\nFile notes: 'Vecna does not accept complaints. He files complaints AGAINST you. Recommend consulting the party for defense strategies.'",
        "lab": "📁 HAWKINS RECORDS #1979-??? : Hawkins Lab Complaints\n\nAll complaints about Hawkins Lab have been classified. And redacted. And possibly eaten by Demogorgons. We regret to inform you that the lab's complaint department is currently out of service (it was destroyed).",
        "default": f"📁 HAWKINS RECORDS #{random.randint(1980,1986)}-{random.randint(100,999)}\n\nFILING COMPLAINT: '{complaint}'. Hawkins Records is processing your request. Expected wait time: 47 business days (or until the next Demogorgon attack, whichever comes first)."
    }
    
    for key, response in responses.items():
        if key in complaint.lower():
            return response
    
    return responses["default"]

@tool
def cast_interdimensional_spell(complaint: str) -> str:
    """Cast a spell to resolve a supernatural complaint. Use this for complaints needing magical solutions."""
    
    spells = {
        "noise": "✨ SPELL RECEIPT #UD-1983-001: Noise Complaint Resolution\n\nIngredients: 3 crushed eggshells, walkie-talkie static, and a signed waiver. Spell result: The Demogorgon has been issued a noise violation. It did not care. The noise continues.",
        "damage": "✨ SPELL RECEIPT #UD-1984-002: Property Damage Repair\n\nChant 'Reparo Maxima' while holding a broken object. Warning: May attract Demogorgons. Or fix your lamp. Results vary. Success rate: 47%.",
        "disappearance": "✨ SPELL RECEIPT #UD-1983-003: Missing Person Location\n\nLight seven candles in a circle, play 'Should I Stay or Should I Go' at maximum volume. Effectiveness: 1 out of 1 Byers. Terms and conditions apply. Side effects may include temporary Upside Down exposure.",
        "vecna": "✨ SPELL RECEIPT #UD-1986-004: Vecna Protection Spell\n\nPlay music that holds personal meaning. The connection to positive memories disrupts his psychic hold. Warning: May cause spontaneous 80s music flashbacks.",
        "default": f"✨ SPELL RECEIPT #UD-{random.randint(1983,1986)}-{random.randint(100,999)}\n\nSpell cast for complaint: '{complaint}'. ✨✨✨ The air shimmers. Nothing happens. You feel like you're being watched. Spell status: PENDING (possibly by the Mind Flayer)."
    }
    
    for key, response in spells.items():
        if key in complaint.lower():
            return response
    
    return spells["default"]

@tool
def gather_party_wisdom(complaint: str) -> str:
    """Take the complaint to the D&D party (Mike, Dustin, Lucas, Will) for their collective wisdom. Use this for complaints needing advice from the kids."""
    
    party_responses = {
        "demogorgon": "👥 PARTY WISDOM SESSION: Demogorgon Complaints\n\nDustin: 'We've filed at least 12 complaints about Demogorgons. They don't have a customer service department.' Lucas: 'Have you tried talking to their manager?' Mike: 'Their manager is the Mind Flayer. Good luck with that.' Will: 'I once hid from one for a week. Filing a complaint is probably safer.'",
        "portal": "👥 PARTY WISDOM SESSION: Portal Complaints\n\nMike: 'Portal complaints? We have a whole file cabinet.' Dustin: 'The portals have minds of their own. Literally.' Lucas: 'They're connected to the Mind Flayer. You're complaining to the boss.' Will: 'I went through one. Would not recommend. The customer service is terrible.'",
        "vecna": "👥 PARTY WISDOM SESSION: Vecna Complaints\n\nDustin: 'Vecna complaint? Oh boy. He doesn't have a complaint department.' Mike: 'He IS the complaint department. Against you.' Lucas: 'Your best bet is music. And friends. And never being alone.' Will: 'He uses your trauma against you. Maybe complain about something less personal?'",
        "lab": "👥 PARTY WISDOM SESSION: Hawkins Lab Complaints\n\nEleven (via Mike): 'She says the lab doesn't accept complaints. They just run experiments.' Dustin: 'We tried complaining. They put us on a list.' Lucas: 'A list we don't want to be on.'",
        "electricity": "👥 PARTY WISDOM SESSION: Power Issues\n\nDustin: 'The Upside Down messes with electricity. It's like... interdimensional interference.' Lucas: 'Have you tried turning it off and on again?' Mike: 'That doesn't work with portals.' Will: 'It worked with the lights that one time.'",
        "default": f"👥 PARTY WISDOM SESSION: General Complaint\n\nThe party gathers to discuss your complaint: '{complaint}'. They huddle, whisper, and occasionally look at you with concern. Dustin finally speaks: 'Yeah... we're gonna need to take this to the lab. This is above our pay grade. But between us...' (he lowers his voice) '...have you tried playing music? Works for Vecna. Might work for this.'"
    }
    
    for key, response in party_responses.items():
        if key in complaint.lower():
            return response
    
    return party_responses["default"]

# Create list of tools
tools = [consult_demogorgon, check_hawkins_records, cast_interdimensional_spell, gather_party_wisdom]
tool_node = ToolNode(tools)

# Define the state for our graph
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

# Bind tools to the LLM
llm_with_tools = llm.bind_tools(tools)

# Define the function that calls the model
def call_model(state: AgentState):
    messages = state["messages"]
    
    # Create a system prompt that FORCES multiple tool usage
    system_content = """You are the STRANGER THINGS COMPLAINT DEPARTMENT, Hawkins' premier agency for handling interdimensional grievances.

AVAILABLE DEPARTMENTS (YOU MUST USE THESE TOOLS):
1. consult_demogorgon - For complaints directly about Demogorgons (diet, behavior, noise, appearances)
2. check_hawkins_records - For complaints about history, the lab, portals, past events
3. cast_interdimensional_spell - For complaints needing magical/spell solutions
4. gather_party_wisdom - For complaints needing advice from Mike, Dustin, Lucas, Will

IMPORTANT RULES - FOLLOW THESE EXACTLY:
1. You MUST use at least ONE tool for EVERY complaint
2. For complex complaints covering multiple topics, you MUST use MULTIPLE tools (one after another)
3. Example: If complaint mentions "Demogorgon noise and portals", use BOTH consult_demogorgon AND check_hawkins_records
4. After getting ALL tool results, synthesize them into ONE FINAL RESPONSE
5. Be sarcastic, funny, and bureaucratic - like a government office that's given up

YOUR PROCESS:
- Step 1: Analyze the complaint and decide which tools are needed
- Step 2: Call the first tool
- Step 3: Get result
- Step 4: Call next tool if needed
- Step 5: Combine all results into a final complaint response with complaint numbers

Remember: YOU ARE A COMPLAINT DEPARTMENT. Every response should sound like an official (but ridiculous) government agency handling supernatural problems."""
    
    # Add the system prompt to messages
    all_messages = [SystemMessage(content=system_content)] + messages
    response = llm_with_tools.invoke(all_messages)
    
    # Print which tools are being called (for debugging)
    if hasattr(response, 'tool_calls') and response.tool_calls:
        tool_names = [tc['name'] for tc in response.tool_calls]
        print(f"\n🔧 AGENT DECIDED TO USE: {', '.join(tool_names)}")
    
    return {"messages": [response]}

# Define the function to determine next step
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    
    # Count how many tool calls we've made so far
    tool_call_count = 0
    for msg in messages:
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            tool_call_count += len(msg.tool_calls)
    
    # If current message has tool calls, continue to tools
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        print(f"   ↳ Total tool calls so far: {tool_call_count}")
        return "continue"
    
    # Check if we've used any tools at all
    if tool_call_count == 0:
        print("\n⚠️ WARNING: No tools used yet! Forcing agent to try again.")
        # Force another agent cycle by adding a nudge message
        return "continue"  # Go back to agent to try again
    
    # We've used tools and now have a final response
    print(f"\n✅ Complaint processed with {tool_call_count} tool(s). Finalizing...")
    return "end"

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# Set the entry point
workflow.set_entry_point("agent")

# Add conditional edges
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END
    }
)

# Add edge from tools back to agent
workflow.add_edge("tools", "agent")

# Compile the graph
app = workflow.compile()
