# SWE / Prompt Engineer Take-Home Assignment - Enrico Ferraz

## Negative Treatment Detection

## Disclaimer

I had some issues with making requests to the endpoints, so I had to manually download the html files and parse them from there. Either way, in the `get_html_from_slug` function, if the response status is 200, the code will try to parse it too.

This project uses a OpenAI's gpt-4o-mini to identify negative treatment within a set of legal opinions.

## Project Structure

```
entities/
functions/
slugs/
.env-template
.gitignore
main.py
README.md
requirements.txt
```

- `entities/`: Contains modules related to the entities used in the project.
- `functions/`: Contains the core functions used in the project.
- `slugs/`: Contains HTML files of the cases to be analyzed.
- `main.py`: The main entry point of the application.
- `test.py`: Contains unit tests for the project.
- `.env-template`: Environment variables template file.
- `requirements.txt`: Lists the dependencies required for the project.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies using `pip`:

   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on the `.env-template` and add your API keys and other configurations.

### Setting up your venv

**Create a virtual environment:**

```sh
python -m venv venv
```

**Activate the virtual environment:**

- On **Windows**:

  ```sh
  .\venv\Scripts\activate
  ```
- On **macOS/Linux**:

  ```sh
  source venv/bin/activate
  ```

## Usage

To run the main application, execute:

```sh
python main.py
```

## Functionality

The main functionality is implemented in the `functions` directory. The key functions are:

- `chatgpt_api.py`: Contains a function to interact with the OpenAI API.
- `get_html_from_slug.py`: Contains functions to fetch HTML content from Casetext using slugs.
