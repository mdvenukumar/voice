import streamlit as st
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    # Set the rate to control the speed (default is 200)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # You can adjust this value

    # Save the speech as a temporary file
    tmp_filename = "temp_audio.mp3"
    engine.save_to_file(text, tmp_filename)
    engine.runAndWait()

    return tmp_filename

def main():
    st.title("Text-to-Speech")

    # Get user input
    user_text = st.text_area("Enter text:", "")

    if st.button("Convert to Speech"):
        if user_text:
            # Convert text to speech and get the filename
            tmp_filename = text_to_speech(user_text)

            # Play the audio using st.audio
            st.audio(tmp_filename, format="audio/mp3", start_time=0)

            # Optionally, display a download link
            st.markdown(f"Download the audio: [temp_audio.mp3](sandbox:/path/{tmp_filename})")

if __name__ == "__main__":
    main()
