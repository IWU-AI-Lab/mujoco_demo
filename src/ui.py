# Gradio interface
import gradio as gr

def run_task(instruction):
    # later: call Claude, then execute in MuJoCo
    return f"Received: {instruction}"

demo = gr.Interface(
    fn=run_task,
    inputs=gr.Textbox(label="Task instruction"),
    outputs=gr.Textbox(label="Result"),
    title="Robot Task Planner"
)

demo.launch()
# or demo.launch(server_name="0.0.0.0") for local network access
# or demo.launch(share=True) for a temporary public URL