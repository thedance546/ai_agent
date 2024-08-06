from dotenv import load_dotenv
load_dotenv()

import os
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")