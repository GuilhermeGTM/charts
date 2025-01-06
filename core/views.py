from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Guilherme",
            "Michela"
        ]
        return datasets

    def get_data(self):
        """
        Retorna (quantidade) datasets para plotar o gráfico.

        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        12 labels, então 12 colunas.
        (quantidade)  datasets, então (quantidade)  linhas.
        """
        dados = []
        for l in range(2):
            for c in range(12):
                dado = [
                    randint(1, 5),  # jan
                    randint(1, 5),  # fev
                    randint(1, 5),  # mar
                    randint(1, 5),  # abr
                    randint(1, 5),  # mai
                    randint(1, 5),  # jun
                    randint(1, 5),  # jul
                    randint(1, 5),  # ago
                    randint(1, 5),  # set
                    randint(1, 5),  # out
                    randint(1, 5),  # nov
                    randint(1, 5)   # dez
                ]
            dados.append(dado)
        return dados
