# 🛡️ Sanctum: The Offline-First Life-Log Agent
**Submission for the 2026 AMD Slingshot Hackathon**

[![Built with AMD](https://img.shields.io/badge/Powered_by-AMD_Ryzen_AI-black?logo=amd&style=for-the-badge)](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html)
[![Zero Cloud](https://img.shields.io/badge/Cloud_Dependency-0%25-red?style=for-the-badge)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Sanctum** is a verifiably private, cross-device "Second Brain." It seamlessly records your digital screens and ambient conversations, intelligently filters out sensitive data (like passwords and banking apps), and lets you query your entire life history instantly—all processed 100% locally on an AMD-powered Hub.

## 🚀 The Problem & The AMD Solution
Building a 24/7 Life-Log Agent forces a dilemma: surrender your life to cloud surveillance (OpenAI/AWS API costs) or watch your edge devices overheat trying to process AI locally.

**Sanctum solves this using a distributed Edge-to-Hub architecture:**
1. **Edge Sensors:** Your phone and laptop act purely as low-power recording nodes.
2. **The Sanctum Hub:** A local machine in your home that leverages the **AMD Ryzen™ AI NPU** to handle continuous transcription (`faster-whisper`) at <5 Watts, preventing battery drain and thermal throttling. **AMD Radeon™ Graphics** decode the incoming streams, and **AMD ROCm™** powers the local Llama-3 recall generation.

## ✨ Core Features
* 🧠 **Total Recall:** Ask natural language questions like *"What startup idea did I mention to Priyanshu last week?"*
* 🛑 **Smart Pause Filter:** Edge-vision models scan the rolling RAM buffer. If a password manager or banking UI is detected, the buffer is instantly flushed and recording pauses.
* 🗑️ **Zero-Storage RAM Buffer:** Raw audio and video are never saved to the hard drive. Once context embeddings are extracted to the local Vector DB (ChromaDB), the raw frames are permanently overwritten.
* 🌐 **Air-Gapped Operation:** Sanctum functions flawlessly even if you physically unplug your router's WAN cable. 

## ⚙️ Tech Stack
* **Core:** Python 3.10
* **NPU Acceleration:** ONNX Runtime (`VitisAIExecutionProvider`)
* **Local Models:** Whisper (STT), Llama-3-8B (Reasoning), YOLO-based visual classification.
* **Database:** ChromaDB (Semantic Vector Store)

## 🛠️ Quick Start (Hackathon MVP)
*Note: This repository contains the core processing pipeline and terminal-based simulation for the AMD Slingshot MVP.*

```bash
git clone [https://github.com/yourusername/Sanctum-AMD-Slingshot.git](https://github.com/yourusername/Sanctum-AMD-Slingshot.git)
cd Sanctum-AMD-Slingshot
pip install -r requirements.txt
python main.py