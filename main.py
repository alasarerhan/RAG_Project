from dotenv import load_dotenv
import warnings

warnings.filterwarnings('ignore')
load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "what is the current weather in Izmir"}))