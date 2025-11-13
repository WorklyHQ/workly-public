"""
Memory System Demo - Workly Public Edition

Demonstrates SQLite-based conversation memory system.
This is a simplified version for educational purposes.

Author: WorklyHQ
License: See LICENSE file
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path


class MemorySystem:
    """Simple conversation memory system using SQLite"""

    def __init__(self, db_path="workly_memory.db"):
        """Initialize memory system"""
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self._connect()
        self._create_tables()

    def _connect(self):
        """Connect to SQLite database"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def _create_tables(self):
        """Create database tables if they don't exist"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                role TEXT NOT NULL,
                message TEXT NOT NULL,
                session_id TEXT,
                metadata TEXT
            )
        """
        )

        # Create indexes for faster queries
        self.cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_timestamp
            ON conversations(timestamp)
        """
        )

        self.cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_role
            ON conversations(role)
        """
        )

        self.cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_session
            ON conversations(session_id)
        """
        )

        self.conn.commit()

    def save_message(self, role, message, session_id=None, metadata=None):
        """Save a message to the database"""
        timestamp = datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None

        self.cursor.execute(
            """
            INSERT INTO conversations (timestamp, role, message, session_id, metadata)
            VALUES (?, ?, ?, ?, ?)
        """,
            (timestamp, role, message, session_id, metadata_json),
        )

        self.conn.commit()
        return self.cursor.lastrowid

    def get_recent_messages(self, limit=10, session_id=None):
        """Get recent messages"""
        if session_id:
            self.cursor.execute(
                """
                SELECT * FROM conversations
                WHERE session_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """,
                (session_id, limit),
            )
        else:
            self.cursor.execute(
                """
                SELECT * FROM conversations
                ORDER BY timestamp DESC
                LIMIT ?
            """,
                (limit,),
            )

        return [dict(row) for row in self.cursor.fetchall()]

    def search_messages(self, keyword):
        """Search messages by keyword"""
        self.cursor.execute(
            """
            SELECT * FROM conversations
            WHERE message LIKE ?
            ORDER BY timestamp DESC
        """,
            (f"%{keyword}%",),
        )

        return [dict(row) for row in self.cursor.fetchall()]

    def get_statistics(self):
        """Get database statistics"""
        # Total messages
        self.cursor.execute("SELECT COUNT(*) as count FROM conversations")
        total = self.cursor.fetchone()["count"]

        # Messages by role
        self.cursor.execute(
            """
            SELECT role, COUNT(*) as count
            FROM conversations
            GROUP BY role
        """
        )
        by_role = {row["role"]: row["count"] for row in self.cursor.fetchall()}

        # Database size
        db_size = (
            Path(self.db_path).stat().st_size if Path(self.db_path).exists() else 0
        )

        return {
            "total_messages": total,
            "by_role": by_role,
            "db_size_bytes": db_size,
            "db_size_kb": round(db_size / 1024, 2),
        }

    def clear_all(self):
        """Clear all messages (use with caution!)"""
        self.cursor.execute("DELETE FROM conversations")
        self.conn.commit()

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


def print_header():
    """Print demo header"""
    print("🧠 Workly Memory System Demo")
    print("═" * 60)
    print()


def print_commands():
    """Print available commands"""
    print("Available commands:")
    print("  - Type a message to save it")
    print("  - 'search <keyword>' to search messages")
    print("  - 'history' to view recent messages")
    print("  - 'stats' to see database statistics")
    print("  - 'clear' to clear all messages")
    print("  - 'quit' to exit")
    print()


def display_messages(messages, title="Messages"):
    """Display list of messages"""
    if not messages:
        print("  No messages found.")
        return

    print(f"\n{title}:")
    print("━" * 60)
    for msg in reversed(messages):
        timestamp = datetime.fromisoformat(msg["timestamp"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        role_emoji = {"user": "👤", "assistant": "🤖", "system": "⚙️"}.get(
            msg["role"], "💬"
        )
        print(
            f"  {role_emoji} [{timestamp}] {msg['message'][:60]}{'...' if len(msg['message']) > 60 else ''}"
        )
    print()


def display_stats(stats):
    """Display database statistics"""
    print("\n📊 Database Statistics:")
    print("━" * 60)
    print(f"  Total messages:   {stats['total_messages']}")
    print(f"  Database size:    {stats['db_size_kb']} KB")
    print(f"\n  Messages by role:")
    for role, count in stats["by_role"].items():
        emoji = {"user": "👤", "assistant": "🤖", "system": "⚙️"}.get(role, "💬")
        print(f"    {emoji} {role.capitalize()}: {count}")
    print()


def main():
    """Main demo function"""
    print_header()

    # Initialize memory system
    memory = MemorySystem("workly_memory.db")
    print(f"📊 Database: workly_memory.db\n")

    # Print commands
    print_commands()

    # Demo loop
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Handle commands
            if user_input.lower() == "quit":
                print("\n👋 Goodbye!")
                break

            elif user_input.lower() == "history":
                messages = memory.get_recent_messages(limit=10)
                display_messages(messages, "📜 Recent messages (last 10)")

            elif user_input.lower() == "stats":
                stats = memory.get_statistics()
                display_stats(stats)

            elif user_input.lower() == "clear":
                confirm = input(
                    "⚠️  Are you sure? This will delete all messages (y/n): "
                )
                if confirm.lower() == "y":
                    memory.clear_all()
                    print("✅ All messages cleared!\n")
                else:
                    print("❌ Cancelled\n")

            elif user_input.lower().startswith("search "):
                keyword = user_input[7:].strip()
                if keyword:
                    messages = memory.search_messages(keyword)
                    display_messages(messages, f"🔍 Search results for '{keyword}'")
                else:
                    print("❌ Please provide a search keyword\n")

            else:
                # Save as user message
                msg_id = memory.save_message("user", user_input, session_id)
                print(f"✅ Message saved (ID: {msg_id})\n")

                # Simulate assistant response
                # In real Workly, this would be AI-generated
                response = f"I received your message: '{user_input[:30]}...'"
                msg_id = memory.save_message("assistant", response, session_id)
                print(f"🤖 {response}\n")

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}\n")

    # Close database
    memory.close()

    print("\n📝 Notes:")
    print("━" * 60)
    print("  This demo shows basic conversation memory.")
    print("  The full Workly Desktop includes:")
    print("    - Semantic search with embeddings")
    print("    - Automatic conversation summarization")
    print("    - Context-aware retrieval")
    print("    - Long-term memory management")
    print()
    print("🔗 Learn more: https://github.com/WorklyHQ/workly-public")
    print()


if __name__ == "__main__":
    main()
