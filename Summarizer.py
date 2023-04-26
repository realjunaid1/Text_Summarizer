import tkinter as tk
import openai
import pyperclip

API_KEY = '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'
openai.api_key = API_KEY
model_id = 'text-davinci-002'

def summarize_text(prompt, text):
    try:
        response = openai.Completion.create(
            model=model_id,
            prompt=prompt + '\n\n' + text,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        summary = response.choices[0].text
        return summary.strip()
    except Exception as e:
        print(f"Error: {e}")
        return ""

def summarize_text_gui():
    prompt = prompt_entry.get()
    text = text_entry.get("1.0", "end-1c")
    
    # Check if the input is empty
    if not prompt or not text:
        summary_label.config(text="Please enter both prompt and text.")
        return
    
    # Show a loading indicator
    summary_label.config(text="Summarizing...")
    window.update()
    
    # Summarize the text
    summary = summarize_text(prompt, text)
    summary_label.config(text=summary)
    
    # Reset the copy button state and hide the loading indicator
    copy_button.config(state=tk.NORMAL)
    window.update()

def copy_to_clipboard():
    summary = summary_label.cget("text")
    pyperclip.copy(summary)

def clear_fields():
    prompt_entry.delete(0, tk.END)
    text_entry.delete("1.0", tk.END)
    summary_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Text Summarizer")
window.geometry("800x600")

# Create the input widgets
prompt_label = tk.Label(window, text="Enter prompt:")
prompt_entry = tk.Entry(window, width=70)
text_label = tk.Label(window, text="Enter text:")
text_entry = tk.Text(window, height=20, width=70, padx=5, wrap="word")
summarize_button = tk.Button(window, text="Summarize", command=summarize_text_gui)
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
clear_button = tk.Button(window, text="Clear", command=clear_fields)

# Create the output widgets
summary_label = tk.Label(window, text="", wraplength=500)

# Layout the widgets using grid
prompt_label.grid(row=0, column=0, sticky="w")
prompt_entry.grid(row=0, column=1, sticky="w")
text_label.grid(row=1, column=0, sticky="w")
text_entry.grid(row=1, column=1, sticky="w")
summarize_button.grid(row=2, column=0, sticky="w")
copy_button.grid(row=2, column=1, sticky="e")
clear_button.grid(row=2, column=2, sticky="e")
summary_label.grid(row=3, column=0, columnspan=3)

# Start the event loop
window.mainloop()
