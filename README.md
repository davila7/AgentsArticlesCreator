# CodeGPT Blog Post Generator

This Streamlit application provides an interface to generate technical blog articles about AI agents available in the CodeGPT. It uses the CodeGPT API to fetch agent information and generate article content based on a detailed prompt.

## Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <project_folder>
    ```
    (Replace `<repository_url>` and `<project_folder>` with your actual repository URL and folder name)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  **Open the application in your browser:**
    The command above will typically open the app in your default web browser at `http://localhost:8501`.

3.  **Configure API Keys:**
    In the sidebar, enter your CodeGPT API Key and CodeGPT-Org-Id.

4.  **Load and Select an Agent:**
    Click the "Load agents" button. Once the agents are loaded, select an agent from the dropdown list.

5.  **Create the Article:**
    Click the "Create article" button. The application will generate a blog post based on the selected agent.

6.  **Edit and Preview:**
    You can edit the generated article in the provided text area and see a preview below.

## License

This project is licensed under the [LICENSE Name] - see the [LICENSE.md](LICENSE.md) file for details.
