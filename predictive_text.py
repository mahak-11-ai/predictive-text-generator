import random

# Load training data
with open("data.txt", "r") as f:
    text = f.read().lower().strip()  # lowercased for matching

# Step 1: Split text into words
words = text.split()
print("Total words loaded:", len(words))  # debug check

# Step 2: Create a dictionary of word pairs (bigram model)
pairs = {}
for i in range(len(words) - 1):
    if words[i] not in pairs:
        pairs[words[i]] = []
    pairs[words[i]].append(words[i + 1])

# Step 3: Prediction function (Top 3 suggestions)
def predict_next_word(word, n=3):
    word = word.lower()
    if word in pairs:
        return random.sample(pairs[word], min(n, len(pairs[word])))
    else:
        return ["No prediction available."]

# Step 4: Generate a full sentence
def generate_sentence(start_word, length=5):
    word = start_word.lower()
    sentence = [word]
    for _ in range(length):
        if word in pairs:
            word = random.choice(pairs[word])
            sentence.append(word)
        else:
            break
    return " ".join(sentence)

# Step 5: Chat-like interaction
print("\n✨ Predictive Text Generator ✨")
print("Type a word and I will guess the next word or complete a sentence!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    # Get predictions
    predictions = predict_next_word(user_input)
    print("🔮 Predictions:", ", ".join(predictions))

    # Generate a full sentence
    sentence = generate_sentence(user_input)
    print("📝 Generated sentence:", sentence)

    # Save interaction to history.txt
    with open("history.txt", "a") as log:
        log.write(f"You: {user_input}\nPredictions: {', '.join(predictions)}\nGenerated: {sentence}\n\n")
