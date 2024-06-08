# Chess Notation Analyzer

The Chess Notation Analyzer is a Flask-based web application designed to convert handwritten chess notations from images into a .pgn (Portable Game Notation) file format. This allows users to easily digitize and analyze handwritten chess games using popular chess analysis tools and viewers.

## Features

- **Image Input**: Accepts input images containing handwritten chess notations.
- **Google Gemini AI**: Utilizes the latest Google Gemini AI for accurate recognition and conversion.
- **PGN File Output**: Generates a .pgn file from the recognized chess notations.
- **Web Interface**: Provides a user-friendly web interface for uploading images and downloading the converted .pgn file.
- **Compatibility**: Viewable with various .pgn viewers and chess analysis software.

## Requirements

- Python 3.12.3
- Flask
- Google Gemini AI API key


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Bhavish5/chess-notation-analyzer.git
    ```

2. Install dependencies:

    ```bash
    cd chess-notation-analyzer
    pip install -r requirements.txt
    ```

3. Obtain a Google Gemini AI API key and configure it in the application.

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Upload an image containing handwritten chess notations.
2. Wait for the AI to process the image and convert the notations.
3. Download the generated .pgn file.
4. Open the .pgn file in your favorite .pgn viewer or chess analysis software for further analysis.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
