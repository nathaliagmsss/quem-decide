import streamlit as st

from src.interpreter import (
    identificar_intencao,
    identificar_proposicao,
    identificar_decisao,
    buscar_competencia,
    identificar_tema,
)

from src.knowledge import (
    carregar_competencias,
    buscar_proposicao,
    buscar_decisao,
    buscar_fonte,
)


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

    intencao = identificar_intencao(pergunta)

    # ==================================================
    # TRAMITAÇÃO
    # ==================================================

    if intencao == "tramitacao":

        proposicao_id = identificar_proposicao(pergunta)

        if proposicao_id:
            proposicao = buscar_proposicao(proposicao_id)

            if proposicao:

                situacao = proposicao["situacao_atual"]

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

                fonte_id = situacao.get("fonte")
                fonte = buscar_fonte(fonte_id) if fonte_id else None

                if fonte:
                    with st.expander("📚 Evidência e fonte oficial"):
                        st.write(
                            f"**{fonte['instituicao']}**"
                        )
                        st.write(fonte["titulo"])

                        st.link_button(
                            "Consultar fonte oficial ↗",
                            fonte["url"],
                        )

                st.stop()

    # ==================================================
    # DECISÃO
    # ==================================================

    if intencao == "decisao":

        decisao_id = identificar_decisao(pergunta)

        if decisao_id:
            decisao = buscar_decisao(decisao_id)

            if decisao:

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

                fonte_id = decisao.get("fontes", [None])[0]
                fonte = buscar_fonte(fonte_id) if fonte_id else None

                if fonte:
                    with st.expander("📚 Evidência e fonte oficial"):
                        st.write(
                            f"**{fonte['instituicao']}**"
                        )
                        st.write(fonte["titulo"])

                        st.link_button(
                            "Consultar fonte oficial ↗",
                            fonte["url"],
                        )

                st.stop()

    # ==================================================
    # COMPETÊNCIAS
    # ==================================================

    dados = carregar_competencias()

    resultado = buscar_competencia(
        pergunta,
        dados["competencias"],
    )

    if resultado:

        st.caption("COMPETÊNCIA INSTITUCIONAL")
        st.header(resultado["orgao"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                '<div class="label">Ente federativo</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="institution">'
                f'{resultado["ente"]}'
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
                f'{resultado["relacao"].capitalize()}'
                f'</div>',
                unsafe_allow_html=True,
            )

        fundamento = resultado["fundamento"]

        st.markdown("#### Base legal")

        st.write(
            f"{fundamento['norma']} — "
            f"art. {fundamento['artigo']}, "
            f"§ {fundamento['paragrafo']}."
        )

        if "observacao" in resultado:
            st.info(resultado["observacao"])

    elif identificar_tema(pergunta, dados["tema"]):

        st.warning(
            "Essa pergunta envolve um tema com diferentes "
            "competências institucionais."
        )

        st.write("Tente especificar o que você quer saber:")

        for competencia in dados["competencias"]:
            st.write(
                "• "
                + competencia["assunto"]
                .replace("_", " ")
                .capitalize()
            )

    else:

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