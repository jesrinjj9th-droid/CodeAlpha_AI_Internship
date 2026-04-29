import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Knowledge Base
faq_data = {
    "What is the internship duration?": "The internship duration is typically 4 weeks.",
    "How do I get my certificate?": "Complete 2-3 tasks and submit the form with your GitHub and LinkedIn links.",
    "What is CodeAlpha?": "CodeAlpha is a software development company focused on real-world training.",
    "Can I complete all 4 tasks?": "Yes, but you only need to complete 2 or 3 to be eligible for a certificate."
}

questions = list(faq_data.keys())

def get_bot_response():
    user_text = user_entry.get().strip()
    if not user_text: return

    # AI Logic: Vectorize text to find similarity
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(questions + [user_text])
    
    # Compare user input against the FAQ list
    scores = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()
    best_match_idx = scores.argsort()[-1]

    # If the match score is high enough, give the answer
    if scores[best_match_idx] > 0.3:
        reply = faq_data[questions[best_match_idx]]
    else:
        reply = "I'm sorry, I don't understand that question yet."

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_text}\nBot: {reply}\n\n")
    chat_display.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI FAQ Chatbot")

chat_display = tk.Text(root, state=tk.DISABLED, width=50, height=20)
chat_display.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=10, pady=10)

tk.Button(root, text="Send", command=get_bot_response).pack(side=tk.LEFT)

root.mainloop()