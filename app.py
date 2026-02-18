import gradio as gr
from src.normalobjects_langchain import (
    consult_demogorgon, 
    check_hawkins_records, 
    cast_interdimensional_spell, 
    gather_party_wisdom
)

def handle_complaint(complaint, tool_choice):
    if tool_choice == "👹 Consult Demogorgon":
        result = consult_demogorgon.invoke({"question": complaint})
    elif tool_choice == "📚 Check Hawkins Records":
        result = check_hawkins_records.invoke({"question": complaint})
    elif tool_choice == "✨ Cast Interdimensional Spell":
        result = cast_interdimensional_spell.invoke({"question": complaint})
    elif tool_choice == "👥 Gather Party Wisdom":
        result = gather_party_wisdom.invoke({"question": complaint})
    else:
        result = "Please select a tool"
    
    return result

# Custom CSS with Stranger Things theme and Christmas lights effect
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Creepster&family=Special+Elite&display=swap');

:root {
    --stranger-red: #e50914;
    --stranger-dark: #0a0f0f;
    --stranger-blue: #1e80ff;
    --upside-down-green: #00ff9d;
}

body {
    background: linear-gradient(135deg, #000000 0%, #1a1a2e 100%);
    margin: 0;
    padding: 0;
}

.gradio-container {
    background: transparent !important;
    max-width: 1200px !important;
    margin: 0 auto !important;
    padding: 20px !important;
    position: relative;
}

/* Christmas lights effect */
.christmas-lights {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 50px;
    background: repeating-linear-gradient(
        90deg,
        transparent,
        transparent 50px,
        rgba(255, 0, 0, 0.1) 50px,
        rgba(255, 0, 0, 0.1) 55px,
        transparent 55px,
        transparent 105px,
        rgba(0, 255, 0, 0.1) 105px,
        rgba(0, 255, 0, 0.1) 110px,
        transparent 110px,
        transparent 160px,
        rgba(0, 0, 255, 0.1) 160px,
        rgba(0, 0, 255, 0.1) 165px
    );
    pointer-events: none;
    z-index: 1000;
    animation: flicker 2s infinite;
}

@keyframes flicker {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
}

@keyframes glow {
    0% { text-shadow: 0 0 10px var(--stranger-red); }
    50% { text-shadow: 0 0 20px var(--stranger-red), 0 0 30px #ff0; }
    100% { text-shadow: 0 0 10px var(--stranger-red); }
}

@keyframes demogorgon-breath {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

/* Header styling */
h1 {
    font-family: 'Creepster', cursive !important;
    font-size: 4em !important;
    background: linear-gradient(45deg, #e50914, #ff6b6b, #ffd700, #e50914);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-size: 300% 300%;
    animation: gradient-shift 5s ease infinite;
    text-align: center !important;
    letter-spacing: 4px !important;
    border: none !important;
    padding: 20px !important;
    position: relative;
}

@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1::before, h1::after {
    content: "⚡";
    color: #ffd700;
    font-size: 1.5em;
    margin: 0 20px;
    animation: glow 1.5s infinite;
}

h3 {
    font-family: 'Special Elite', cursive !important;
    color: #a8dadc !important;
    text-align: center !important;
    border-bottom: 2px dashed #e50914 !important;
    padding-bottom: 10px !important;
}

/* Input areas */
label {
    font-family: 'Special Elite', cursive !important;
    color: #ffd700 !important;
    font-size: 1.3em !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 5px rgba(229, 9, 20, 0.5) !important;
}

input, textarea, select {
    background: rgba(10, 15, 15, 0.9) !important;
    border: 2px solid #e50914 !important;
    border-radius: 8px !important;
    color: #00ff9d !important;
    font-family: 'Courier New', monospace !important;
    font-size: 1.1em !important;
    padding: 12px !important;
    box-shadow: 0 0 15px rgba(229, 9, 20, 0.3) !important;
    transition: all 0.3s !important;
}

input:focus, textarea:focus, select:focus {
    border-color: #00ff9d !important;
    box-shadow: 0 0 25px rgba(0, 255, 157, 0.5) !important;
    outline: none !important;
    transform: translateY(-2px);
}

/* Dropdown specific */
select {
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23e50914' stroke-width='2'><polyline points='6 9 12 15 18 9'/></svg>");
    background-repeat: no-repeat;
    background-position: right 10px center;
    padding-right: 40px !important;
}

/* Button styling */
button {
    background: linear-gradient(45deg, #e50914, #6a040f) !important;
    border: none !important;
    border-radius: 50px !important;
    color: white !important;
    font-family: 'Creepster', cursive !important;
    font-size: 1.8em !important;
    padding: 20px 40px !important;
    text-transform: uppercase !important;
    letter-spacing: 4px !important;
    box-shadow: 0 0 30px rgba(229, 9, 20, 0.5) !important;
    transition: all 0.3s !important;
    width: 100% !important;
    margin: 20px 0 !important;
    animation: demogorgon-breath 3s infinite;
}

button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 50px rgba(255, 215, 0, 0.8) !important;
    background: linear-gradient(45deg, #6a040f, #e50914) !important;
}

/* Output area */
.output-text {
    background: rgba(10, 15, 15, 0.95) !important;
    border: 3px solid #e50914 !important;
    border-radius: 15px !important;
    color: #00ff9d !important;
    font-family: 'Special Elite', cursive !important;
    font-size: 1.2em !important;
    padding: 25px !important;
    box-shadow: 0 0 30px rgba(229, 9, 20, 0.3), inset 0 0 30px rgba(0, 0, 0, 0.8) !important;
    line-height: 1.6 !important;
    min-height: 150px !important;
}

/* Radio/Checkbox styling */
.gr-box {
    border: 1px solid #e50914 !important;
    background: rgba(0, 0, 0, 0.7) !important;
}

/* Progress/loading bar */
.progress-bar {
    background: linear-gradient(90deg, #e50914, #ffd700, #00ff9d) !important;
}

/* Tool selection area */
.gr-form {
    background: rgba(0, 0, 0, 0.5) !important;
    border-radius: 15px !important;
    padding: 20px !important;
    backdrop-filter: blur(5px) !important;
    border: 1px solid rgba(229, 9, 20, 0.3) !important;
}

/* Add some floating demogorgon faces */
.floating-demogorgon {
    position: fixed;
    bottom: 20px;
    right: 20px;
    font-size: 4em;
    opacity: 0.2;
    animation: demogorgon-breath 4s infinite;
    pointer-events: none;
    z-index: 999;
}

.floating-demogorgon::after {
    content: "👹";
}

/* 80s grid background */
.grid-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(229, 9, 20, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(229, 9, 20, 0.05) 1px, transparent 1px);
    background-size: 50px 50px;
    pointer-events: none;
    z-index: -1;
}

/* Responsive design */
@media (max-width: 768px) {
    h1 {
        font-size: 2.5em !important;
    }
    
    button {
        font-size: 1.2em !important;
        padding: 15px 20px !important;
    }
}
"""

# HTML elements to add
html_elements = """
<div class="christmas-lights"></div>
<div class="grid-background"></div>
<div class="floating-demogorgon"></div>
"""

with gr.Blocks(title="Stranger Things Complaint Department", theme=gr.themes.Base()) as demo:
    gr.HTML(html_elements)
    
    gr.Markdown("# STRANGER THINGS COMPLAINT DEPARTMENT")
    gr.Markdown("### *\"When you're lost in the darkness, look for the lights\"*")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            <div style="text-align: center; margin: 20px 0;">
                <span style="font-size: 3em; filter: drop-shadow(0 0 20px #e50914);">⚡</span>
            </div>
            """)
    
    with gr.Row():
        with gr.Column(scale=2):
            complaint_input = gr.Textbox(
                label="🔮 YOUR QUESTION", 
                placeholder="Ask about Demogorgons, the Mind Flayer, Eleven, portals, or any Hawkins mystery...",
                lines=4
            )
        with gr.Column(scale=1):
            tool_dropdown = gr.Dropdown(
                choices=[
                    "👹 Consult Demogorgon", 
                    "📚 Check Hawkins Records", 
                    "✨ Cast Interdimensional Spell", 
                    "👥 Gather Party Wisdom"
                ],
                label="🛠️ CHOOSE YOUR TOOL",
                value="👹 Consult Demogorgon"
            )
    
    with gr.Row():
        submit_btn = gr.Button("🌋 ENTER THE UPSIDE DOWN 🌋")
    
    with gr.Row():
        output = gr.Textbox(
            label="📜 MESSAGE FROM THE DARKNESS", 
            lines=8,
            elem_classes="output-text"
        )
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            <div style="display: flex; justify-content: space-around; margin: 30px 0; color: #666; font-family: 'Special Elite', cursive;">
                <span>🔥 1983</span>
                <span>👾 HAWKINS LAB</span>
                <span>🌌 THE UPSIDE DOWN</span>
                <span>⚡ 1984</span>
            </div>
            """)
    
    gr.Markdown("---")
    gr.Markdown("""
    <div style="text-align: center; font-family: 'Special Elite', cursive; color: #a8dadc; padding: 20px;">
        <p><i>"Friends don't lie... but the Upside Down does."</i></p>
        <p style="font-size: 0.9em; margin-top: 10px;">⚡ Select a tool, ask your question, and uncover the mysteries of Hawkins... if you dare. ⚡</p>
    </div>
    """)
    
    # Add some interactive JavaScript for extra effects
    gr.HTML("""
    <script>
        // Add flickering effect to Christmas lights
        setInterval(() => {
            const lights = document.querySelector('.christmas-lights');
            if (lights) {
                lights.style.opacity = 0.3 + Math.random() * 0.7;
            }
        }, 200);
    </script>
    """)
    
    submit_btn.click(fn=handle_complaint, inputs=[complaint_input, tool_dropdown], outputs=output)

if __name__ == "__main__":
    demo.launch(share=True)