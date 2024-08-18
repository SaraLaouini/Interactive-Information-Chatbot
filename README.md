# Interactive-Information-Chatbot

This project involves a chatbot that interacts with users to answer questions based on content extracted from a website. The chatbot utilizes a Large Language Model (LLM) hosted on AWS Bedrock to provide intelligent responses.

## Project Structure

* **Backend**
    * `lambda_function.py` (AWS Lambda function code for extracting website text and interacting with the LLM)
* **Frontend**
    * `index.html` (Main HTML file for the user interface)
    * `script.js` (JavaScript for client-side logic)
    * `styles.css` (CSS for styling the UI)


### Backend
- **`lambda_function.py`**: 
  - This script handles:
    - Extracting text content from a specified website using `requests` and `BeautifulSoup`.
    - Invoking an LLM (Claude 3 Sonnet) via AWS Bedrock to generate answers to user questions based on the extracted website content.
    - Returning the chatbot's responses to be displayed on the frontend.

### Frontend
- **`index.html`**: The main HTML file that provides the structure for the user interface where users can interact with the chatbot.
- **`script.js`**: Manages client-side logic, including capturing user input, sending it to the backend, and displaying the chatbot's responses.
- **`styles.css`**: Provides styling to the user interface, ensuring a clean and user-friendly experience.

## Features
- **Website Content Extraction**: Automatically scrapes text content from a specified website to provide relevant information.
- **Interactive Chatbot**: A user-friendly chatbot interface that allows users to ask questions and receive intelligent responses based on website content.
- **Scalable and Serverless**: The backend is powered by AWS Lambda, providing scalability and ease of management without the need for server infrastructure.

## Getting Started

### Prerequisites
- An AWS account with access to Lambda and Bedrock services.
- Basic knowledge of Python, HTML, JavaScript, and CSS.

### Installation

1. **Deploy the Backend**:
   - Upload `lambda_function.py` to an AWS Lambda function.
   - Ensure necessary IAM roles and permissions for the Lambda function to interact with AWS Bedrock.

2. **Set Up the Frontend**:
   - Place the contents of the `Frontend/` directory on your web server or local machine.
   - Update the endpoints in `script.js` to point to your deployed AWS Lambda function.

3. **Run the Project**:
   - Open `index.html` in your web browser to access the chatbot interface.
   - Interact with the chatbot by asking questions about the content of a specified website.


