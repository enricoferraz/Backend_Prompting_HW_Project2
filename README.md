# SWE / Prompt Engineer Take-Home Assignment


## LLMs Background

Large Language Models (LLMs) unlock many new opportunities in legal applications engineering. Machine learning tasks such as data extraction, classification, summarization, and text generation have traditionally been very time-intensive undertakings. LLMs make these tasks much easier, through the act of “prompting” the model. At their core, LLMs are given some text and then generate a “completion” of words that follow the initial text. This initial text is called the “prompt”. It typically includes instructions for the model as well as whatever text or data we want the model to analyze. For example, the following prompt could be used to translate some text:

```
Please translate the following text from English to Spanish:

“The cat chased the dog.”
```

The model might return the following completion:

```
El gato persiguió al perro.
```

The power of this style of programming is that the prompts are incredibly flexible. A small change to the prompt can do the work of thousands of lines of code and hundreds of hours annotating training data:

```
Please translate the following text from English to Turkish:

“The cat chased the dog.”
```

The model might then return the following completion:

```
Kedi köpeği kovaladı.
```

This power is further exploited through the use of templates, which can dynamically incorporate data provided by a user and other sources:

```
Please translate the following from English to {{to_language}}:

“{{text_to_translate}}”
```

With just a few extra lines of glue code, this template can form the basis of a universal translator application (this is, of course, assuming the underlying LLM has such translation capabilities – but they often do!).


## Assignment

The goal of this project is to use the LLM to identify negative treatment within a set of opinions. Negative treatment occurs when one case overrules or otherwise limits the holding of a prior case. The deliverable is a Python function that can tell the caller whether a particular case on Casetext is negatively treating any other cases.

Casetext has an internal API that can be accessed over the public internet that provides the HTML of opinions:

```
GET https://casetext.com/api/search-api/doc/{SLUG}/html
```

where `SLUG` is Casetext’s proprietary case identifier.

The slugs of the cases to analyze for this assignment are:

- littlejohn-v-state-7
- beattie-v-beattie
- travelers-indem-co-v-lake
- tilden-v-state
- in-re-lee-342013

The function should be called `extract_negative_treatments`, and it should take as its sole argument a slug. It should return some sort of data structure that effectively communicates the presence (or absence) of negative treatments in the case. Effectively communicating negative treatment will include: the identity of the treated case, the nature of the treatment, and potentially the text of the treatment and even an explanation from the model as to why it made such a determination.

For example, once you deliver the function, we should be able to run:

```
treatments = extract_negative_treatments(slug='in-re-lee-342013')
```


## Tips and Hints

- Consider using `requests` and `BeautifulSoup` libraries to fetch the HTML of the case and then to parse the resulting HTML.
- Consider which OpenAI model you will use. They are listed [here](https://platform.openai.com/docs/models). If you’re using your own OpenAI account, `gpt-3.5-turbo` is your best bet.
- Understand [Chat vs. Completions](https://platform.openai.com/docs/guides/chat/chat-vs-completions).
- The project shouldn’t take longer than about 2-6 hours.
- Feel free to ask questions if you get stuck anywhere.
- Do not hard-code any API keys or other secrets.
- Where helpful, split up code into easy-to-understand functions (or classes).
- Consider using [jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) or [f-strings](https://realpython.com/python-f-strings/) to create and use prompt templates.


## Evaluation
 
We will evaluate the code you submit for fitness for purpose and general quality. Furthermore, we will test the effectiveness of the LLM prompts by inputting slugs we have set aside and checking the output of the `extract_negative_treatments` function. Think of this as set-aside test data.
 
While these are not required, feel free to add:
- unit tests
- discussion of different prompting approaches you tried
- a README
- package management, like requirements or poetry files
- anything else that you think might be useful
 
 
## Submitting the assignment
 
Please clone this repository, complete the assignment, and share your repository with github user `cmorbidelli`. Please do not submit iPython/Jupyter notebooks or email the code directly.
