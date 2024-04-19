# KatzBot - An AI Assistant for Yeshiva University

KatzBot leverages the Katz generative pre-trained transformer (KatzGPT) to enhance communication within university communities, addressing precision gaps observed in existing academic chatbot systems.

## Project Overview

KatzBot aims to revolutionize the academic chatbot experience by using a custom large language model (LLM) tailored specifically to the needs of the Yeshiva University community. It utilizes two meticulously curated datasets comprising sentence completion and question-answer pairs to train the KatzGPT model, thereby improving its accuracy and effectiveness.

## Features

- **Enhanced Communication**: Provides precise and contextually relevant answers to various university-related queries.
- **Data-Driven Insights**: Uses comprehensive datasets specifically tailored to university needs.
- **Custom LLM**: Built on a sophisticated model architecture that learns from university-specific data.

## Data Collection and Processing

### Collection

- Data collected from the university's database, official website, articles, and social media.
- Both automated (using Python libraries like BeautifulSoup) and manual data collection methods employed.

### Processing

- Extensive data cleaning and preprocessing using regular expressions and customized parsing techniques.
- Data organized into sentence pairs and question-answer pairs to facilitate model training.

## Model Training

- **Framework**: PyTorch 2.0.1 with torchvision 0.15.2 and CUDA 12.1.
- **Optimizer**: AdamW with a learning rate of $5e-5$ and weight decay of 5e-4.

## Dataset Overview

- **Sentence Completion Pairs**: 6,280 pairs for knowledge integration.
- **Train QA Pairs**: 7,334 pairs for enhancing detailed understanding.
- **Test QA Pairs**: 2,081 pairs for assessing model consistency.

## Results and Evaluation

- KatzBot, through KatzGPT, matches or exceeds the performance of leading LLMs in specific Rouge metrics, particularly in Rouge-L, which measures the long-form coherence of generated texts.
- The model's performance underscores its capability to understand and reproducing the context and structure of the source texts effectively.

## Conclusion

KatzGPT's development underlines the potential of specialized training and custom LLMs in academic settings. While GPT-2 remains a benchmark of excellence, KatzGPT’s advancements suggest a bright future for further research and applications in AI.

## How to Use KatzBot

To interact with KatzBot, follow these steps:
1. Access the KatzBot interface through the Yeshiva University portal (In the development phase).
2. Input your query in the designated text field.
3. Receive immediate, accurate responses to your questions.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
