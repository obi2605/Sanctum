
import time
import random
import logging

# ==========================================
# SANCTUM HUB: AMD NPU INFERENCE PIPELINE
# ==========================================

class SanctumHub:
    def __init__(self):
        self.power_draw = "2.1W"
        self.ram_buffer = []
        self.vector_db = []
        print("\n[INIT] Booting Sanctum Hub...")
        time.sleep(1)
        print(f"[HW] AMD Ryzen™ AI NPU Detected. Execution Provider: VitisAIExecutionProvider")
        print(f"[HW] AMD Radeon™ Graphics Active for stream decoding.")
        print("[NET] Local Wi-Fi Socket bound. Cloud APIs: DISABLED (Air-Gapped Mode)")
        print("========================================================\n")

    def simulate_incoming_stream(self, data_type, content):
        print(f"[INGEST] Receiving encrypted 5-second {data_type} chunk from Edge Device...")
        time.sleep(1)
        
        # Load into RAM Buffer
        self.ram_buffer.append(content)
        print(f"[MEM] Chunk loaded into Rolling RAM Buffer. Disk Write: 0 bytes.")
        
        # Smart Pause Filter Check
        if self._smart_pause_check(content):
            print("🛑 [ALERT] Smart Pause Triggered! Sensitive UI (Banking/Password) detected.")
            self.ram_buffer.clear()
            print("🗑️ [MEM] RAM Buffer instantly flushed. Data discarded.")
        else:
            self._process_on_npu(content)

    def _smart_pause_check(self, content):
        # Simulate local vision model detecting a banking app
        time.sleep(0.5)
        sensitive_keywords = ["bank", "password", "incognito"]
        return any(word in content.lower() for word in sensitive_keywords)

    def _process_on_npu(self, content):
        print(f"⚡ [NPU] Transcribing and Vectorizing on Ryzen AI NPU (Power: {self.power_draw})...")
        time.sleep(1.5)
        # Store metadata
        self.vector_db.append({"timestamp": time.strftime("%H:%M:%S"), "content": content})
        print("💾 [DB] Context Embeddings saved to Local ChromaDB.")
        
        # Flush RAM
        self.ram_buffer.clear()
        print("🗑️ [MEM] Raw stream permanently discarded from RAM.\n")

    def query_memory(self, question):
        print(f"\n👤 [USER QUERY]: '{question}'")
        print("🔍 [DB] Searching local vector embeddings...")
        time.sleep(1)
        print("🧠 [ROCm] Generating answer using local Llama-3...")
        time.sleep(2)
        
        # Mocking the semantic search result for the demo
        if "priyanshu" in question.lower() or "startup" in question.lower():
            print("✅ [SANCTUM]: You discussed a bill-splitting app called 'Electrosplit' with Priyanshu yesterday at 14:30 PM.")
        else:
            print("✅ [SANCTUM]: Memory retrieved successfully based on local context.")
        print("========================================================\n")


# ==========================================
# SIMULATION LOOP FOR DEMO VIDEO
# ==========================================
if __name__ == "__main__":
    hub = SanctumHub()
    
    # 1. Simulate a safe conversation
    hub.simulate_incoming_stream("audio", "Hey Priyanshu, we should build that startup idea, the bill-splitting app called Electrosplit.")
    
    # 2. Simulate the user opening a banking app (triggers Smart Pause)
    time.sleep(2)
    hub.simulate_incoming_stream("screen", "Opening HDFC Bank portal. Entering password...")
    
    # 3. Simulate the Offline Query (THIS IS WHERE YOU UNPLUG YOUR WIFI IN THE VIDEO)
    time.sleep(2)
    print("\n--- ⚠️ NETWORK DISCONNECTED: DEMONSTRATING AIR-GAPPED RECALL ---")
    time.sleep(1)
    hub.query_memory("What startup idea did I mention to Priyanshu?")