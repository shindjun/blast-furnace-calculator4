import streamlit as st

# 제목
st.title("고로 출선 작업 계산기")

# 사용자 입력 받기
ore_coke_ratio = st.number_input("Ore/Coke 비율:", min_value=0.0, step=0.01)
air_flow = st.number_input("풍량 (Nm³/min):", min_value=0.0)
air_pressure = st.number_input("풍압 (kg/cm²):", min_value=0.0)
furnace_pressure = st.number_input("노정압 (kg/cm²):", min_value=0.0)
furnace_temperature = st.number_input("용선온도 (°C):", min_value=0.0)
oxygen_injection = st.number_input("산소부화량 (Nm³/hr):", min_value=0.0)
moisture_content = st.number_input("조습량 (g/Nm²):", min_value=0.0)
tfe_percent = st.number_input("T.Fe (%)", min_value=0.0)
daily_production = st.number_input("일일생산량 (ton):", min_value=0.0)

# 슬래그량 예측
def predict_slag_amount():
    return daily_production * (1 - (tfe_percent / 100))

# 용선량 예측
def predict_blast_furnace_output():
    return daily_production * ore_coke_ratio * 0.8

# 용선 저선량 계산 (ton 단위)
def calculate_blast_furnace_radiation(blast_furnace_output):
    # 예시: 저선량 비율 0.05 사용 (실제 값은 고로 설비에 따라 다를 수 있습니다)
    radiation_factor = 0.05
    return blast_furnace_output * radiation_factor

# 슬래그 저선량 계산 (ton 단위)
def calculate_slag_radiation(slag_amount):
    # 예시: 슬래그 저선량 비율 0.02 사용 (실제 값은 고로 설비에 따라 다를 수 있습니다)
    radiation_factor = 0.02
    return slag_amount * radiation_factor

# 결과 출력
if st.button("계산하기"):
    slag_amount = predict_slag_amount()
    blast_furnace_output = predict_blast_furnace_output()
    
    slag_radiation = calculate_slag_radiation(slag_amount)
    blast_furnace_radiation = calculate_blast_furnace_radiation(blast_furnace_output)
    
    total_radiation = slag_radiation + blast_furnace_radiation

    st.subheader("예상 결과")
    st.write(f"용선 저선량: {blast_furnace_radiation:.2f} ton")
    st.write(f"슬래그 저선량: {slag_radiation:.2f} ton")
    st.write(f"노내 예상 총 저선량: {total_radiation:.2f} ton")