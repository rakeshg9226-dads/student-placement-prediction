import streamlit as st


def load_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                135deg,
                #eef5ff 0%,
                #f7f9fc 55%,
                #e8fff7 100%
            );
        }

        .block-container {
            padding-top: 1.6rem;
            max-width: 1200px;
        }

        .hero {
            padding: 1.4rem 1.7rem;
            border-radius: 18px;
            color: white;
            background: linear-gradient(
                110deg,
                #123b70,
                #1769aa,
                #12a88a
            );
            margin-bottom: 1rem;
        }

        .hero h1 {
            margin: 0;
            font-size: 2.25rem;
        }

        .hero p {
            margin: .4rem 0 0 0;
            opacity: .92;
        }

        .metric-card {
            background: white;
            border: 1px solid #dce7f2;
            padding: 1rem;
            border-radius: 14px;
            box-shadow: 0 4px 16px rgba(18,59,112,.06);
        }

        div[data-testid="stForm"] {
            background: rgba(255,255,255,.8);
            padding: 1rem;
            border-radius: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_header():
    st.markdown(
        """
        <div class="hero">
            <h1>🎓 Student Placement Prediction</h1>
            <p>
                Machine Learning + Streamlit |
                Estimate placement likelihood from academic
                and skill indicators
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

