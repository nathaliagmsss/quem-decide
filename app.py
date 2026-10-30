import streamlit as st

from src.core import processar_pergunta


# --------------------------------------------------
# CONFIGURAÇÃO
# --------------------------------------------------

st.set_page_config(
    page_title="Quem Decide?",
    page_icon="🏛️",
    layout="centered",
)


# --------------------------------------------------
# ESTILO
# --------------------------------------------------

st.markdown(
    """
    <style>
        .block-container {
            max-width: 850px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 2rem;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 0.4rem;
        }

        .hero p {
            font-size: 1.1rem;
            opacity: 0.75;
            max-width: 650px;
            margin: auto;
        }

        .label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            opacity: 0.6;
            margin-bottom: 0.2rem;
        }

        .institution {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        div[data-testid="stTextInput"] input {
            font-size: 1.05rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# CABEÇALHO
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>Quem Decide?</h1>
        <p>
            Entenda quem decide, quem executa e como funcionam
            decisões e responsabilidades das instituições públicas brasileiras.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# PERGUNTA
# --------------------------------------------------

if "pergunta" not in st.session_state:
    st.session_state.pergunta = ""

pergunta = st.text_input(
    "Faça uma pergunta",
    value=st.session_state.pergunta,
    placeholder="Ex.: Quem cuida do policiamento nas ruas?",
)

st.caption("Experimente uma pergunta:")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🚓 Policiamento nas ruas",
        use_container_width=True,
    ):
        st.session_state.pergunta = "quem cuida do policiamento nas ruas?"
        st.rerun()

with col2:
    if st.button(
        "⚖️ PLP 197/2024",
        use_container_width=True,
    ):
        st.session_state.pergunta = "o PLP 197/2024 já foi aprovado?"
        st.rerun()

st.divider()


# --------------------------------------------------
# PROCESSAMENTO
# --------------------------------------------------

if pergunta:

    resposta = processar_pergunta(pergunta)

    # ==================================================
    # TRAMITAÇÃO
    # ==================================================


    if resposta and resposta["tipo"] == "tramitacao":

        proposicao = resposta["proposicao"]
        situacao = resposta["situacao"]
        fonte = resposta["fonte"]

        st.caption("TRAMITAÇÃO LEGISLATIVA")
        st.header(
            f"{proposicao['tipo']} {proposicao['numero']}"
        )

        if situacao["status"] == "aguardando_designacao_de_relator":
            st.warning("Ainda não foi aprovado.")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                '<div class="label">Onde está</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="institution">'
                f'{situacao["sigla_orgao"]}'
                f'</div>',
                unsafe_allow_html=True,
            )
            st.write(situacao["orgao"])

        with col2:
            st.markdown(
                '<div class="label">Situação</div>',
                unsafe_allow_html=True,
            )
            st.write(
                situacao["status"]
                .replace("_", " ")
                .capitalize()
            )

        st.caption(
            f"Situação consultada em "
            f"{situacao['data_consulta']}."
        )

        if fonte:
            with st.expander("📚 Evidência e fonte oficial"):
                st.write(f"**{fonte['instituicao']}**")
                st.write(fonte["titulo"])

                st.link_button(
                    "Consultar fonte oficial ↗",
                    fonte["url"],
                )

        st.stop()


    # ==================================================
    # DECISÃO
    # ==================================================

    if resposta and resposta["tipo"] == "decisao":

        decisao = resposta["decisao"]
        fonte = resposta["fonte"]

        st.caption("DECISÃO INSTITUCIONAL")
        st.header(decisao["sigla_orgao"])

        st.write(
            f"Em **{decisao['data']}**, o "
            f"**{decisao['sigla_orgao']}** analisou "
            "o caso registrado na base."
        )

        if decisao["cria_nova_hipotese_legal"] is False:
            st.success(
                "✓ Não criou uma nova hipótese legal. "
                "O tribunal interpretou e aplicou "
                "uma norma já existente."
            )

        st.markdown("#### Efeito da decisão")
        st.write(decisao["efeito"]["descricao"])

        if fonte:
            with st.expander("📚 Evidência e fonte oficial"):
                st.write(f"**{fonte['instituicao']}**")
                st.write(fonte["titulo"])

                st.link_button(
                    "Consultar fonte oficial ↗",
                    fonte["url"],
                )

        st.stop()

    # ==================================================
    # COMPETÊNCIA
    # ==================================================

    if resposta and resposta["tipo"] == "competencia":

        competencia = resposta["competencia"]
        fundamento = competencia["fundamento"]

        st.caption("COMPETÊNCIA INSTITUCIONAL")
        st.header(competencia["orgao"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                '<div class="label">Ente federativo</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="institution">'
                f'{competencia["ente"]}'
                f'</div>',
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                '<div class="label">Papel</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="institution">'
                f'{competencia["relacao"].capitalize()}'
                f'</div>',
                unsafe_allow_html=True,
            )

        st.markdown("#### Base legal")

        st.write(
            f"{fundamento['norma']} — "
            f"art. {fundamento['artigo']}, "
            f"§ {fundamento['paragrafo']}."
        )

        if "observacao" in competencia:
            st.info(competencia["observacao"])

        st.stop()


    # ==================================================
    # TEMA AMBÍGUO
    # ==================================================

    if resposta and resposta["tipo"] == "tema_ambiguo":

        tema = resposta["tema"]
        competencias = resposta["competencias"]

        st.caption("TEMA AMPLO")
        st.header(tema["nome"])

        st.warning(
            "Esse tema envolve diferentes competências institucionais. "
            "Não existe uma única resposta para quem é responsável."
        )

        st.write("Você pode especificar, por exemplo:")

        for competencia in competencias:
            assunto = (
                competencia["assunto"]
                .replace("_", " ")
                .capitalize()
            )

            st.write(
                f"**{assunto}** — "
                f"{competencia['orgao']} "
                f"({competencia['ente']})"
            )

        st.stop()


    # ==================================================
    # SEM RESPOSTA
    # ==================================================

    if resposta is None:

        st.warning(
            "Ainda não tenho informações suficientes "
            "na minha base para responder a essa pergunta."
        )

        st.caption(
            "O Quem Decide? prefere não responder quando "
            "não possui evidências suficientes."
        )


# --------------------------------------------------
# RODAPÉ
# --------------------------------------------------

st.divider()

st.caption(
    "Quem Decide? • Protótipo experimental • "
    "Respostas baseadas em dados estruturados e fontes institucionais."
)