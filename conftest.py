import sys
from pathlib import Path

# Add project root to sys.path so src_ViBR and src_llm can be imported in tests
sys.path.insert(0, str(Path(__file__).parent))
