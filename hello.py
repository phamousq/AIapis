import os

from dotenv import load_dotenv


def main():
    load_dotenv()
    print(os.getenv("API_KEY"))


if __name__ == "__main__":
    main()
