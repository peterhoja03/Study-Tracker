"""
db.py — Shared Supabase client helper.

All modules import _sb() from here. Do NOT define _sb() anywhere else.
This ensures the Supabase connection is created once and shared across
the whole session via st.session_state["supabase_client"].
"""

import os
import streamlit as st


def _sb():
    """
    Return the Supabase client, creating it on first call.
    Returns None if credentials are missing or connection fails.
    """
    if "supabase_client" not in st.session_state:
        try:
            from supabase import create_client
            url = st.secrets.get("SUPABASE_URL", "") or os.environ.get("SUPABASE_URL", "")
            key = st.secrets.get("SUPABASE_KEY", "") or os.environ.get("SUPABASE_KEY", "")
            st.session_state["supabase_client"] = create_client(url, key) if url and key else None
        except Exception:
            st.session_state["supabase_client"] = None
    return st.session_state["supabase_client"]
