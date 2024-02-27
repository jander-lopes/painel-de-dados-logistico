def dica_ferramenta():
    return (
        "<span style='font-size: 1rem'><b>Veículo:</b> %{customdata[0]}</span><br><br>"
        + "<span style='font-size: 1rem'><b>Custos abastecimento =</b> %{customdata[1]} - (%{customdata[2]:.0f}%)</span><br><br>"
        + "<span style='font-size: 1rem'><b>Custos Manutenção =</b> %{customdata[3]} - (%{customdata[4]:.0f}%)</span><br><br>"
        + "<span style='font-size: 1rem'><b>Custos Fixos =</b> %{customdata[5]} - (%{customdata[6]:.0f}%)</span><br><br>"
        + "<br><span style='font-size: 1rem'><b>Custos Totais =</b> %{customdata[7]}</span><br>"
        + "<br><span style='font-size: 1rem'>Custos Totais é <b>%{customdata[8]:.0f}%</b> da soma dos <br>custos de todos os tipos de veículos</span><br>"
    )
