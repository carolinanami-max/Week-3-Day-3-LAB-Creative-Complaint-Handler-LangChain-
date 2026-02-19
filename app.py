import gradio as gr
from src.langgraph_agent import app
from langchain_core.messages import HumanMessage, AIMessage

def handle_complaint(complaint):
    if not complaint.strip():
        return "Please enter a complaint."
    
    inputs = {"messages": [HumanMessage(content=complaint)]}
    result = app.invoke(inputs)
    messages = result["messages"]
    
    tools_used = []
    for msg in messages:
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            for tc in msg.tool_calls:
                tools_used.append(tc['name'])
    
    final_response = None
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and not msg.tool_calls:
            final_response = msg.content
            break
    
    if final_response:
        if tools_used:
            tool_list = ", ".join(set(tools_used))
            return f"🔧 Tools used: {tool_list}\n\n{final_response}"
        return final_response
    return "⚠️ Error processing complaint."

custom_css = """
body { background-color: #0b0c10; }
.gradio-container { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border: 2px solid #e94560; border-radius: 15px; padding: 20px; }
h1 { color: #e94560 !important; font-family: 'Courier New', monospace; text-align: center; }
label { color: #e94560 !important; font-family: 'Courier New', monospace; }
input, textarea { background-color: #0f3460 !important; border: 1px solid #e94560 !important; color: #ffffff !important; }
button { background: linear-gradient(45deg, #e94560, #0f3460) !important; color: white !important; width: 100% !important; }
.output-text { background-color: #0f3460 !important; border: 2px solid #e94560 !important; color: #ffffff !important; }
"""

with gr.Blocks(title="Stranger Things Complaint Department", css=custom_css) as demo:
    gr.Markdown("# STRANGER THINGS COMPLAINT DEPARTMENT")
    complaint_input = gr.Textbox(label="FILE YOUR COMPLAINT", lines=4)
    submit_btn = gr.Button("SUBMIT")
    output = gr.Textbox(label="RESPONSE", lines=10, elem_classes="output-text")
    submit_btn.click(fn=handle_complaint, inputs=[complaint_input], outputs=output)

if __name__ == "__main__":
    demo.launch(share=True)