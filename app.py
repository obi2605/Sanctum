import streamlit as st
import time

st.set_page_config(page_title="Sanctum Hub", page_icon="🛡️", layout="centered")

st.title("🛡️ Sanctum Hub (AMD Powered)")

col1, col2, col3 = st.columns(3)
col1.metric("Hardware", "Ryzen™ AI NPU", "Active")
col2.metric("Power Draw", "2.1W", "-80% vs Cloud")
col3.metric("RAM Buffer", "Rolling", "0 Bytes on Disk")

st.divider()

if st.button("▶️ Start Encrypted Edge Stream"):
    with st.status("Receiving Data from Edge Devices...", expanded=True) as status:
        st.write("📥 Ingesting audio: 'Hey Priyanshu, let's build Electrosplit.'")
        time.sleep(2)
        st.write("⚡ Transcribing & Vectorizing via AMD NPU...")
        time.sleep(2)
        st.write("💾 Embeddings saved. Raw audio flushed from RAM.")
        status.update(label="Stream Processed", state="complete", expanded=False)

if st.button("🛑 Simulate Banking App Opening (Smart Pause)"):
    with st.status("Analyzing Screen...", expanded=True) as status:
        time.sleep(1)
        st.error("🚨 SENSITIVE UI DETECTED: Passwords/Banking")
        st.write("🗑️ RAM Buffer instantly flushed. Recording paused.")
        status.update(label="Smart Pause Activated", state="error", expanded=True)

st.divider()
query = st.text_input("🔍 Universal Recall (Air-Gapped)", placeholder="What startup idea did I mention to Priyanshu?")

if query:
    with st.spinner("Generating answer locally via ROCm Llama-3..."):
        time.sleep(3)
        st.success("🎙️ **Audio Match:** You discussed a bill-splitting app called 'Electrosplit' with Priyanshu.")