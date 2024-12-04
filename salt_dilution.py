import streamlit as st

# Streamlit App
st.title("Saltwater Dilution Calculator")
st.write("This app calculates the intermediate salinity (Mm) and the required volume of stock solution (Vi) for saltwater dilution.")

# Input parameters
st.header("Input Parameters")
Mi = st.number_input("Stock Solution Salinity (Mi) (%)", min_value=0.0, value=10.0, step=0.1)
Mf = st.number_input("Final Salinity (Mf) (%)", min_value=0.0, value=0.5, step=0.1)
Vm = st.number_input("Intermediate Volume (Vm) (mL)", min_value=0.0, value=500.0, step=1.0)
Vf = st.number_input("Final Volume (Vf) (mL)", min_value=0.0, value=1000.0, step=1.0)

# Calculate Mm and Vi
if Vm > 0 and Vf > 0 and Mi > 0 and Mf > 0:
    Mm = Mf * Vf / Vm  # Intermediate salinity calculation
    Vi = Mm * Vm / Mi  # Volume of stock solution calculation
    
    st.header("Results")
    st.write(f"Intermediate Salinity (Mm): **{Mm:.2f}%**")
    st.write(f"Required Volume of Stock Solution (Vi): **{Vi:.2f} mL**")
else:
    st.warning("Please ensure all input values are greater than 0.")

# Display calculation equations for reference
st.header("Equations Used")
st.latex(r"Mi \cdot Vi = Mm \cdot Vm")
st.latex(r"Mm \cdot Vm = Mf \cdot Vf")
st.write("Where:")
st.write("- Mi: Stock solution salinity (%)")
st.write("- Vi: Volume of stock solution (mL)")
st.write("- Mm: Intermediate salinity (%)")
st.write("- Vm: Intermediate volume (mL)")
st.write("- Mf: Final salinity (%)")
st.write("- Vf: Final volume (mL)")

# Add footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
