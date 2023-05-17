# Codeacademy Bot

Codeacademy Bot is a Telegram bot that registers users and stores their information in a JSON database. It collects the user's name, last name, Telegram username, residential address, educational background, and current level of study.

## Description

This bot allows users to sign up by providing their personal information and educational details. It serves as a registration platform for Codeacademy, facilitating the enrollment process and storing the necessary data for administrative purposes.

## Features

- User Registration: Users can sign up by providing their name, last name, Telegram username, residential address, educational background, and current level of study.
- JSON Database: User information is stored in a JSON file for easy retrieval and management.
- Data Validation: The bot can validate user inputs to ensure the accuracy and completeness of the provided information.
- User Inquiry: The bot can inquire about the user's study level, prompting them to enter the current stage of their studies.
- Data Storage and Retrieval: The bot can store user information in the JSON database and retrieve it when needed.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Obtain a Telegram Bot API token by creating a bot on the Telegram BotFather platform.

4. Configure the bot settings:

- Open the `config.json` file.
- Replace the placeholder value `<TELEGRAM_TOKEN>` with your Telegram Bot API token.

5. Run the bot:

    ```bash
    python main.py
    ```

Your Codeacademy Bot is now up and running! Users can interact with it via Telegram and register by providing the required information.

## Usage

1. Start the bot on Telegram by searching for your bot username.

2. The bot will guide users through the registration process, prompting them to enter their name, last name, Telegram username, residential address, educational background, and current level of study.

3. Once users provide all the required information, the bot will store it in the JSON database.

4. You can access and manage the user data in the JSON database as needed.

## Future Improvements

- Add user authentication and authorization for enhanced security.

- Implement data validation to ensure the correctness of user inputs.

- Add additional features such as user profile management and course enrollment.

- Support multiple languages for a wider user base.

- Deploy the bot on a cloud server for 24/7 availability.


## Contributing

Contributions to the Codeacademy Bot project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Develop your feature or bug fix.

4. Commit your changes and push them to your forked repository.

5. Submit a pull request detailing your changes.
