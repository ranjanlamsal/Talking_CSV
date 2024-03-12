# Talking CSV

<img src="Screenshot from 2024-03-12 16-58-25.png" alt="Talking CSV">


Talking CSV is a mini project designed to facilitate interaction with CSV data through speech. It allows users to upload a CSV file, record their voice, transcribe the audio, and generate voice responses based on the transcribed text and the data from the CSV file.

## Features
### CSV Data Interaction
Users can upload a CSV file containing data that they want to interact with.
### Voice Recording
The application enables users to record their voice using a microphone.
### Speech-to-Text Transcription
It transcribes the recorded audio into text using OpenAI's Whisper AI technology.
### Response Generation
Based on the transcribed text and the data from the CSV file, the application generates voice responses to user queries.
### User-Friendly Interface
The project utilizes Streamlit, a user-friendly web application framework, for the interface, making it easy for users to interact with the application.

<!-- GETTING STARTED -->
## Getting Started

To get started with the Talking CSV, follow these simple steps:

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

* Python 3
* Streamlit
* langchain_openai
* dotenv

## Installation

### 1. Cloning Repository

To clone this repository, use the following command:

```bash
git clone https://github.com/your-username/talking-csv.git
```

 ### 2. Setting Up Virtual Environment
First, let's create a virtual environment to isolate our project dependencies.

  #### Windows
  ```sh
  # Install virtualenv using pip
  pip install virtualenv

  # Create a virtual environment named 'env'
  virtualenv env

  # Activate the virtual environment
  .\env\Scripts\activate
  ```
  #### Mac & Linux
  ```sh
  # Install virtualenv using pip
  pip install virtualenv

  # Create a virtual environment named 'env'
  virtualenv env

  # Activate the virtual environment
  source env/bin/activate
  ```
## 3. Installing Required Packages
Now, let's install the required Python packages listed in the requirements.txt file.

  ```sh
  pip install -r requirements.txt
  ```

## 4. Setting Up Environment Variables
The application requires an OpenAI API key to interact with the language model. You need to set up this API key as an environment variable.

  #### In Windows
  ```sh
  set OPENAI_API_KEY=your_openai_api_key
  ```

  #### In Mac & Linux
  ```sh
  export OPENAI_API_KEY=your_openai_api_key
  ```

  Replace your_openai_api_key with your actual OpenAI API key obtained from the OpenAI website.

## 5. Running the Application
Finally, you can run the Python Langchain Simple Prompt Chain using Streamlit.

  ```sh
  streamlit run speech_to_text.py
```

