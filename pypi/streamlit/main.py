import streamlit as st

# 1. Título e Subtítulo da Página
st.title("🚀 A Minha Primeira App com Streamlit")
st.subheader("Exemplo simples e interativo")

# 2. Entrada de Texto (Nome)
nome = st.text_input("Qual é o seu nome?")

# 3. Seletor Numérico (Idade)
idade = st.number_input("Qual é a sua idade?", min_value=1, max_value=120, value=25)

# 4. Caixa de Seleção (Cor Favorita)
cor = st.selectbox(
    "Escolha a sua cor preferida:",
    ["Azul", "Verde", "Vermelho", "Amarelo", "Roxo"]
)

# 5. Botão de Ação
if st.button("Enviar Dados"):
    if nome:
        st.success(f"Olá, **{nome}**! Os teus dados foram recebidos com sucesso.")
        st.write(f"- **Idade:** {idade} anos")
        st.write(f"- **Cor Favorita:** {cor}")
    else:
        st.warning("Por favor, digite o seu nome antes de enviar.")

# 6. Elemento Gráfico / Métrica
st.divider()
st.metric(label="Status do Sistema", value="Online", delta="100% Funcional")