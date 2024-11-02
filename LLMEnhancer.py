import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()



def transform_text(input_text, complexity_level=3):
    """
    Transform input text into a more sophisticated version using Google's Gemini AI.
    
    Args:
        input_text (str): The original text to transform
        complexity_level (int): Desired complexity level (1-3)
    
    Returns:
        str: Transformed text
    """
    # Configure the Gemini API
    genai.configure(api_key=os.getenv('GOOGLE_AI_API_KEY'))

    # Select the model
    model = genai.GenerativeModel('gemini-pro')
    
    # Create prompts based on complexity level
    complexity_prompts = {
        1: "Rewrite this text using more sophisticated vocabulary while maintaining clarity:",
        2: "Rewrite this text using advanced academic language, complex sentence structures, and specialized terminology:",
        3: "Transform this text into an extremely elaborate academic discourse, employing esoteric terminology, intricate syntactical constructions, and extensive subordinate clauses:"
    }
    
    # Construct the full prompt
    system_context = """You are an expert in transforming simple text into sophisticated academic prose.
    Focus on:
    - Using advanced vocabulary and specialized terminology
    - Creating complex sentence structures with multiple clauses
    - Incorporating academic and philosophical perspectives
    - Adding relevant theoretical frameworks where applicable
    - Maintaining semantic meaning while maximizing linguistic complexity
    
    Original text to transform:
    """
    
    full_prompt = f"{system_context}\n{input_text}\n\n{complexity_prompts[complexity_level]}"
    
    try:
        # Generate content
        response = model.generate_content(full_prompt)
        
        # Check if the response has content
        if response.text:
            return response.text
        else:
            return "Error: No content generated"
            
    except Exception as e:
        return f"Error transforming text: {str(e)}"

def process_text_with_safety(text, safety_settings=None):
    """
    Process text with custom safety settings if provided.
    
    Args:
        text (str): Input text
        safety_settings (dict, optional): Custom safety settings for Gemini
    """
    try:
        model = genai.GenerativeModel(
            model_name='gemini-pro',
            safety_settings=safety_settings
        )
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error with safety settings: {str(e)}"

