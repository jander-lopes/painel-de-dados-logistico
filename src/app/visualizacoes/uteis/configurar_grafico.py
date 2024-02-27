from plotly.graph_objects import Figure


def configurar_grafico_colunas(fig: Figure) -> None:
    fig.update_layout(
        legend=dict(
            orientation="h",
            xanchor="left",
            yanchor="top",
            y=1.1,
            x=0,
            bgcolor="rgba(0,0,0,0)",
        ),
        legend_itemclick=False,
        legend_itemdoubleclick=False,
        margin=dict(l=0, r=25, b=-0, t=80),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title=None,
            automargin=True,
            rangemode="tozero",
        ),
        xaxis=dict(
            type="category",
            showgrid=False,
            zeroline=False,
            title=None,
            automargin=True,
        ),
        dragmode="pan",
    )


def configurar_grafico_barras(fig: Figure) -> None:
    fig.update_layout(
        legend=dict(
            orientation="h",
            xanchor="left",
            yanchor="top",
            y=1.1,
            x=-0.08,
            bgcolor="rgba(0,0,0,0)",
        ),
        legend_itemclick=False,
        legend_itemdoubleclick=False,
        margin=dict(l=0, r=25, b=-0, t=80, autoexpand=True),
        yaxis=dict(categoryorder="category descending"),
        xaxis=dict(showticklabels=False),
        dragmode="pan",
    )


def configurar_grafico_linha(fig: Figure) -> None:
    fig.update_layout(
        margin=dict(autoexpand=True, l=0, r=25, b=-0, t=80, pad=0),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title=None,
            automargin=True,
            rangemode="tozero",
        ),
        xaxis=dict(type="category", showgrid=False, zeroline=False, title=None, automargin=True),
        dragmode="pan",
    )


def configuracao_grafico_margem(fig: Figure, tamanho_dados: int) -> None:
    configurar_grafico_linha(fig)
    fig.update_layout(
        hovermode="x unified",
        margin=dict(autoexpand=True, l=0, r=25, b=-0, t=80, pad=0),
        dragmode="pan",
    )
    fig.update_xaxes(range=[-0.2, tamanho_dados - 1 + 0.05])


def configurar_barra_ferramenta_grafico():
    return dict(
        config=dict(
            displaylogo=False,
            zoom=False,
            modeBarButtonsToRemove=["autoScale", "zoomin", "zoomout", "select2d", "lasso2d"],
        )
    )
