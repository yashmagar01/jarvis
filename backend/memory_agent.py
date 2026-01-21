"""
MemoryAgent - Long-term memory for Jarvis using Supermemory API

This agent provides persistent memory capabilities, allowing Jarvis to:
- Remember facts and preferences about the user
- Recall relevant context from past conversations
- Build a dynamic user profile over time
"""

import os
from dotenv import load_dotenv

load_dotenv()

class MemoryAgent:
    """
    Wraps the Supermemory SDK to provide long-term memory for Jarvis.
    """
    
    def __init__(self):
        self.api_key = os.getenv("SUPERMEMORY_API_KEY")
        self.client = None
        self._initialized = False
        
        if not self.api_key:
            print("[MEMORY] Warning: SUPERMEMORY_API_KEY not found in .env")
            print("[MEMORY] Memory features will be disabled. Get a free key at supermemory.ai")
            return
            
        try:
            from supermemory import Supermemory
            self.client = Supermemory(api_key=self.api_key)
            self._initialized = True
            print("[MEMORY] MemoryAgent initialized successfully")
        except ImportError:
            print("[MEMORY] Warning: supermemory package not installed. Run: pip install supermemory")
        except Exception as e:
            print(f"[MEMORY] Error initializing Supermemory client: {e}")
    
    @property
    def is_available(self) -> bool:
        """Check if memory agent is properly initialized."""
        return self._initialized and self.client is not None
    
    async def add_memory(self, content: str, metadata: dict = None) -> dict:
        """
        Store a memory/fact in long-term storage.
        
        Args:
            content: The text content to remember
            metadata: Optional metadata (e.g., category, importance)
            
        Returns:
            Result dict with status and memory_id
        """
        if not self.is_available:
            return {"success": False, "error": "Memory agent not initialized"}
        
        try:
            # Add memory using Supermemory SDK
            result = self.client.memories.add(
                content=content,
                metadata=metadata or {}
            )
            print(f"[MEMORY] Stored memory: {content[:50]}...")
            return {"success": True, "memory_id": result.id if hasattr(result, 'id') else None}
        except Exception as e:
            print(f"[MEMORY] Error storing memory: {e}")
            return {"success": False, "error": str(e)}
    
    async def search_memories(self, query: str, limit: int = 5) -> list:
        """
        Search for relevant memories based on a query.
        
        Args:
            query: Natural language search query
            limit: Maximum number of results to return
            
        Returns:
            List of relevant memory objects
        """
        if not self.is_available:
            return []
        
        try:
            results = self.client.memories.search(
                query=query,
                limit=limit
            )
            print(f"[MEMORY] Found {len(results)} relevant memories for: {query[:30]}...")
            return [
                {
                    "content": r.content if hasattr(r, 'content') else str(r),
                    "relevance": r.score if hasattr(r, 'score') else None
                }
                for r in results
            ]
        except Exception as e:
            print(f"[MEMORY] Error searching memories: {e}")
            return []
    
    async def get_context_for_query(self, query: str) -> str:
        """
        Get a formatted context string of relevant memories for a query.
        
        Args:
            query: The current user query
            
        Returns:
            Formatted context string to inject into the conversation
        """
        memories = await self.search_memories(query, limit=3)
        
        if not memories:
            return ""
        
        context_parts = ["[Relevant memories from past conversations:]"]
        for i, mem in enumerate(memories, 1):
            context_parts.append(f"{i}. {mem['content']}")
        
        return "\n".join(context_parts)
    
    async def remember_conversation(self, user_message: str, assistant_response: str) -> None:
        """
        Automatically store a conversation exchange for future reference.
        
        Args:
            user_message: What the user said
            assistant_response: How Jarvis responded
        """
        if not self.is_available:
            return
        
        # Only store meaningful exchanges (not greetings, etc.)
        if len(user_message) < 20 or len(assistant_response) < 20:
            return
        
        summary = f"User asked: {user_message[:100]}... | Jarvis responded about: {assistant_response[:100]}..."
        
        await self.add_memory(
            content=summary,
            metadata={"type": "conversation", "auto_saved": True}
        )
