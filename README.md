# 🗂️ Document Conversation (RAGs)

**Document Conversation** is a Python-based application that enables users to interact with documents through a conversational interface. Utilizing **Streamlit** for the user interface and **Large Language Models (LLMs)** for natural language understanding, this tool allows for efficient querying and summarization of document content.

## 📁 Project Structure

- `main.py`: Launches the Streamlit application.
- `models.py`: Handles the loading and management of LLMs.
- `templates.py`: Contains prompt templates and processes user input for the models.
- `tasks.py`: Implements specific tasks the assistant can perform.
- `requirements.txt`: Lists all project dependencies.

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/denisbvnt/document_conversation.git
   cd document_conversation

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run main.py
   ```

4. The app will automatically open in your default browser (usually at `http://localhost:8501`).

## 🧠 Features

- Interactive interface built with Streamlit.
- Natural language processing powered by LLMs.
- Dynamic prompt generation based on user input.
- Execution of document-related tasks through conversational commands.

## 🛠️ Technologies Used

- **Python** – Core programming language used throughout the project
- **Streamlit** – Lightweight framework for building the interactive web interface
- **LangChain** – Framework for chaining together components to build LLM-powered applications
- **LLMs** – Used for natural language understanding and response generation
- Additional libraries and tools are listed in `requirements.txt`

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/79a043e4-7d6f-4d29-85a7-3055bf3366d5)

![image](https://github.com/user-attachments/assets/ce7d713c-f9a8-4f9e-8bec-dc359a5de59b)

  
## 📄 License

This project is licensed under the [MIT License](LICENSE).
```
