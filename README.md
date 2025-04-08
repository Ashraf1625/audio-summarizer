# 🎧 Audio Summarization App

An intuitive web application that transcribes spoken content from audio files and provides concise summaries using state-of-the-art machine learning models.

## 📌 Overview

The Audio Summarization App allows users to upload `.wav` or `.mp3` files, automatically transcribes the speech using **Wav2Vec2** by Facebook, and summarizes the transcript with **DistilBART** from Hugging Face Transformers.

Built with [Streamlit](https://streamlit.io/), this app is ideal for turning meetings, interviews, lectures, and other voice recordings into readable summaries in just a few clicks.

## 🧠 Key Features

- 🎙️ Upload audio files in `.wav` or `.mp3` format
- 🔊 Speech-to-text transcription with `facebook/wav2vec2-base-960h`
- ✍️ Summarization with `sshleifer/distilbart-cnn-12-6`
- ⚡ Fast, responsive interface using Streamlit
- 🧹 Manual cache clearing option for better memory management

## 🔧 Technologies & Models

| Component        | Tool/Model                                   |
| ---------------- | -------------------------------------------- |
| Framework        | Streamlit                                    |
| Speech-to-Text   | Wav2Vec2 (`facebook/wav2vec2-base-960h`)     |
| Summarization    | DistilBART (`sshleifer/distilbart-cnn-12-6`) |
| Audio Processing | Librosa                                      |
| Backend          | PyTorch, Transformers                        |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/audio-summarizer.git
cd audio-summarizer
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the App

```bash
streamlit run app.py
```

> Make sure to replace `app.py` with the actual name of your script if different.

## 📁 Project Structure

```
audio-summarizer/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── ...
```

## ⚠️ Notes

- Best results are achieved with clear, high-quality audio recordings.
- The app supports English-language speech only (as per the pretrained models used).
- Processing time may vary depending on audio length and system performance.

## 🪪 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as needed.

## 🙌 Acknowledgements

- [Facebook AI](https://ai.facebook.com/) for `Wav2Vec2`
- [Hugging Face](https://huggingface.co/) for pre-trained models
- [Streamlit](https://streamlit.io/) for rapid app deployment
