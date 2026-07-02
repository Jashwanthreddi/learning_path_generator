# 📚 Learning Path Generator

> Generate structured, logically ordered learning roadmaps for any skill or domain using Generative AI.

# 📖 Overview

Learning Path Generator is a Generative AI application that creates structured learning roadmaps from a single user input.

Given a skill or domain (e.g., **Data Science**, **Python**, **Machine Learning**, **Pandas**), the application generates:

- 📌 Learning stages
- 📚 Key topics
- 📝 Learning progression summary

Unlike free-form text generation, the output follows a predefined **Pydantic schema**, ensuring consistency, validation, and easy integration into APIs or educational platforms.

---

# 🎯 Problem Statement

Many learners know **what they want to learn** but struggle with **how to learn it**.

Common challenges include:

- Not knowing where to begin
- Learning advanced topics too early
- Following random tutorials
- Lack of structured progression

This project addresses these challenges by generating a logically ordered learning roadmap tailored to the input skill.

---

# ✨ Features

- 🤖 AI-generated learning roadmaps
- 📄 Structured JSON output
- ✅ Pydantic schema validation
- 🧠 Logical topic sequencing
- 💻 Interactive Streamlit interface
- ⚡ Powered by Groq Llama 3.3 70B
- 🔄 Consistent outputs using low-temperature generation

---

# 📥 Input

The application accepts a single input.

```text
Skill or Domain
```

Example:

```text
Data Science
```

```text
Machine Learning
```

```text
Pandas
```

---

# 📤 Output

The generated response follows this JSON schema.

```json
{
  "learning_stages": [
    "string"
  ],
  "key_topics": [
    "string"
  ],
  "learning_goal_summary": "string"
}
```

---

# 📝 Example

### Input

```text
Data Science
```

### Output

```json
{
  "learning_stages": [
    "Beginner",
    "Intermediate",
    "Advanced"
  ],
  "key_topics": [
    "Python Programming",
    "Statistics",
    "Data Visualization",
    "Machine Learning",
    "Model Evaluation"
  ],
  "learning_goal_summary": "The roadmap introduces programming fundamentals and statistics before progressing to data analysis, machine learning, and practical model development."
}
```

---

# 🏗️ Architecture

```
                User Input
                     │
                     ▼
           Prompt Template
                     │
                     ▼
           Groq Llama 3.3 70B
                     │
                     ▼
       Structured Output (Pydantic)
                     │
                     ▼
              JSON Response
                     │
                     ▼
             Streamlit Interface
```

---

# 📁 Project Structure

```
learning_path_generator/
│
├── app.py                 # Streamlit UI
├── Generator.py           # LLM pipeline
├── prompt.py              # Prompt template
├── schema.py              # Pydantic schema
├── requirements.txt       # Dependencies
├── .env.example           # Environment variables
│
└── tests/
    └── test_cases.py      # Test cases
```

---

# ⚙️ Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| LLM | Groq (Llama-3.3-70B-Versatile) |
| Framework | LangChain |
| Prompting | ChatPromptTemplate |
| Validation | Pydantic |
| UI | Streamlit |
| Environment | python-dotenv |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/learning_path_generator.git
```

Move into the project

```bash
cd learning_path_generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_api_key
```

---

# ▶️ Running the Application

## Streamlit UI

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## Run from Terminal

```bash
python Generator.py
```

---

# 🧪 Testing

Run the provided test cases.

```bash
python -m tests.test_cases
```

The tests evaluate:

- JSON schema validation
- Structured output generation
- Logical learning progression

---

# 💡 Design Decisions

## Why Structured Output?

Instead of generating plain text, the model directly produces structured JSON validated by Pydantic.

Benefits include:

- Reliable parsing
- Consistent outputs
- Easier API integration
- Automatic validation

---

## Why Low Temperature (0.3)?

This application prioritizes consistency over creativity.

A low temperature helps produce:

- Stable roadmaps
- Consistent stage ordering
- Reduced randomness

---

## Why Not Retrieval-Augmented Generation (RAG)?

This project does not require external knowledge retrieval.

The roadmap is generated solely from the input skill using the model's general knowledge.

Adding retrieval would increase complexity without improving the required functionality.

---

## Why Not Agents or LangGraph?

The workflow is deterministic:

- Single user input
- Single prompt
- No conversation memory
- No tool calling
- No multi-step reasoning

Therefore, an agentic architecture would introduce unnecessary complexity.

---

# 📊 Sample Inputs

| Input | Expected Output |
|--------|-----------------|
| Data Science | Multi-stage roadmap |
| Machine Learning | Structured learning progression |
| Python | Programming roadmap |
| Pandas | Focused roadmap |
| Deep Learning | Advanced roadmap |

---

# 🔮 Future Improvements

- Personalized learning paths
- Resource recommendations
- Course integration
- RAG-based learning resources
- Learning duration estimation
- REST API
- PDF export
- Interactive roadmap visualization
- Multi-language support

---

# ⚠️ Known Limitations

- Roadmaps are generated using the LLM's general knowledge.
- No external resources are referenced.
- Output quality depends on the language model.

---

# 👨‍💻 Author

**Jashwanth Reddy**

B.Tech in Artificial Intelligence & Machine Learning

AI • Generative AI • Machine Learning • LangChain • LLM Applications

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub!
