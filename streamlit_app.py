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

# 계산: 출선시간 예측
# (간단한 예시로 계산, 실제 공식에 맞춰 계산식 수정 필요)
def predict_casting_time():
    return (air_flow + oxygen_injection) / (ore_coke_ratio + furnace_pressure)

# 계산: 슬래그량 예측
def predict_slag_amount():
    return daily_production * (1 - (tfe_percent / 100))

# 계산: 용선량 예측
def predict_blast_furnace_output():
    return daily_production * ore_coke_ratio * 0.8

# 결과 출력
if st.button("계산하기"):
    casting_time = predict_casting_time()
    slag_amount = predict_slag_amount()
    output_blast_furnace = predict_blast_furnace_output()

    st.subheader("예상 결과")
    st.write(f"출선 시간: {casting_time:.2f} 분")
    st.write(f"슬래그량: {slag_amount:.2f} ton")
    st.write(f"용선량: {output_blast_furnace:.2f} ton")