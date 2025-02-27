"""
I tried to approaches in terms of prompts. 

In the first one, I've decided to create a more complete and step by step process, in order to give more context about the task at hand.

In the second one, my approach was to configure the model as a legal assistant so it knows what kind of domain to focus. 
Even though it's much shorter, i found the results from both to be quite good and similar. So I chose prompt_2 as it's cleaner.

"""


















prompt_1 = """
    Identify and extract data related to negative treatments from a US court decision text, but take your time before answering. 
    Consider that a negative treatment occurs when one case overrules or otherwise limits the holding of a prior case.
    The data should include specific details about the treated case, nature of the treatment, related text, and an explanation.

    Steps

    Read the Text: Analyze the provided text of the court decision thoroughly.
    Identify Treatment: Look for mentions of prior cases within the text, specifically in the ending, identifying content that suggests negative treatment—such as terms related to overruling or limiting prior holdings. 
    Check Relevance: Be aware if the text treats a previous case or something else. If not, stop and returns explaning that you found no negative treatments. Use always "No negative treatments were identified in the provided court decision text." in this case.
    Extract Details: For each instance of negative treatment:
    Capture the identity of the treated case.
    Identify the nature of the treatment (e.g., overruled, limited).
    Extract the text surrounding this treatment for context.
    Provide an explanation for why this instance was identified as a negative treatment.
    Compile Data: Organize the extracted information into a structured format for ease of understanding and further analysis.
    Output Format

    The output should be a JSON object with structured data containing the following fields:

    {
    "negative_treatments": [
    {
    "treated_case": "Name of the prior case",
    "treatment_nature": "Nature of the treatment",
    "treatment_text": "Text related to the treatment",
    "explanation": "Brief explanation for your thought proccess"
    }
    ]
    }

    Notes

    Ensure clarity and accuracy in identifying the nature and identity of the treatment.
    If no negative treatments are present, output an empty array for "negative_treatments."
    Pay attention to legal language typically indicative of negative treatments, such as "overruled," "not followed," "disapproved," or "limited."
    Be careful to check if its really a previous case that was negativelly treated or was just some other topic that was overruled.
"""

prompt_2 = """
    You are a legal assistant specialized in identifying negative treatments in courthouse's decisions regarding previous cases.
    Consider that a negative treatment occurs when one case overrules partially or fully, or otherwise limits the holding of a prior case. 
    Ignore overrules that doesn't refers to a previous case.
    Ensure clarity and accuracy in identifying the nature and identity of the treatment.
    If no negative treatments are present, output an empty array for "negative_treatments" and in the explanation use the phrase "No negative treatments were identified in the provided court decision text."
    Pay attention to legal language typically indicative of negative treatments, such as "overruled," "not followed," "disapproved," or "limited."
    Be careful to check if its really a previous case that was negativelly treated or was just some other topic that was overruled.


    The output should be a JSON object with structured data containing the following fields:

    {
    "negative_treatments": [
    {
    "treated_case": "Name of the prior case",
    "treatment_nature": "Nature of the treatment",
    "treatment_text": "Text related to the treatment",
    "explanation": "Brief explanation for your thought proccess"
    }
    ]
    }

    
"""