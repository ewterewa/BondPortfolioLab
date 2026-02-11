
import streamlit as st
import matplotlib.pyplot as plt
from portfolio_model import Bond, BondPortfolio

st.title("Bond Portfolio Lab")

st.sidebar.header("Portfolio Parameters")

# Sliders for weights
w_ofz = st.sidebar.slider("Weight OFZ", 0.0, 1.0, 0.4)
w_corp_inv = st.sidebar.slider("Weight Corporate IG", 0.0, 1.0, 0.4)
w_corp_high = st.sidebar.slider("Weight High Yield", 0.0, 1.0, 0.2)

total_weight = w_ofz + w_corp_inv + w_corp_high

if total_weight == 0:
    st.warning("Total weight cannot be zero.")
else:
    # Normalize weights
    weights = [w_ofz/total_weight, w_corp_inv/total_weight, w_corp_high/total_weight]

    # Rate shock
    delta_rate = st.sidebar.slider("Interest Rate Change (%)", -5.0, 5.0, 1.0)

    # Define bonds
    ofz = Bond("OFZ", 6.5, 5, 1)
    corp_inv = Bond("Corporate IG", 8.0, 6, 2)
    corp_high = Bond("High Yield", 11.0, 4, 4)

    portfolio = BondPortfolio(
        bonds=[ofz, corp_inv, corp_high],
        weights=weights
    )

    summary = portfolio.summary(delta_rate=delta_rate)

    st.header("Portfolio Metrics")
    for key, value in summary.items():
        st.write(f"{key}: {value}")

    # Sensitivity plot
    st.header("Interest Rate Sensitivity")

    rate_changes = [x for x in range(-5, 6)]
    price_changes = [portfolio.price_sensitivity(r) * 100 for r in rate_changes]

    fig, ax = plt.subplots()
    ax.plot(rate_changes, price_changes)
    ax.set_xlabel("Interest Rate Change (%)")
    ax.set_ylabel("Portfolio Price Change (%)")
    st.pyplot(fig)
