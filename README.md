# AI Storyteller with LangChain

## 📖 Introduction

AI Storyteller is a Python-based storytelling application powered by **LangChain** and **OpenAI's GPT models**. It generates engaging and creative stories based on user prompts, offering an interactive and immersive storytelling experience.

## 🚀 Features

- **AI-Generated Stories**: Generate unique stories with AI based on a given prompt.
- **Customizable Length**: Control the length of the generated story.
- **Character & Genre Selection**: Choose different genres and character types.
- **Streaming Output**: Get the story generated in real-time.
- **Deployable**: Easily deploy using **Hugging Face Spaces** or **Streamlit**.

## 🛠️ Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/ai-storyteller.git
cd ai-storyteller
```

### 2️⃣ Create a Virtual Environment

```sh
python -m venv storyteller_env
source storyteller_env/bin/activate  # Mac/Linux
storyteller_env\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

## 🏗️ Configuration

Before running the application, set up your **OpenAI API Key**.

1. Create a `.env` file in the project root:

```sh
touch .env
```

2. Add the following line:

```
OPENAI_API_KEY=your-api-key-here
```

Alternatively, you can set the API key in your terminal:

```sh
export OPENAI_API_KEY=your-api-key-here  # Mac/Linux
set OPENAI_API_KEY=your-api-key-here  # Windows
```

## 🏃‍♂️ Running the Application

Run the application using Streamlit:

```sh
streamlit run app.py
```

## 📦 Deploying to Hugging Face Spaces

1. Create a new **Hugging Face Space** with **Streamlit** as the SDK.
2. Upload your project files (`app.py`, `requirements.txt`, etc.).
3. Add a `requirements.txt` file with dependencies:

```
streamlit
langchain
openai
dotenv
```

4. Push your code:

```sh
git add .
git commit -m "Initial commit"
git push
```

5. Your Hugging Face Space will automatically build and deploy!

## 🛠️ Troubleshooting

- **ModuleNotFoundError**: Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **API Key Errors**: Double-check that your OpenAI API key is correctly set in `.env` or your environment variables.
- **Dependency Conflicts**: Create a clean virtual environment and reinstall dependencies.

## 🎉 Contributing

Feel free to fork this repository, submit issues, or make pull requests to improve AI Storyteller.

