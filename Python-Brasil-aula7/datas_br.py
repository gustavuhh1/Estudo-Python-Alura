from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada

    def mes_cadastro(self):
        meses_lista = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
                       "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes_cadastro = self.momento_cadastro.month
        return "Mês: {} {}".format(meses_lista[mes_cadastro - 1], mes_cadastro)

    def dia_semana(self):
        semana_lista = ["Segunda", "Terça", "Quarta",
                        "Quinta", "Sexta", "Sabado", "Domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return semana_lista[dia_semana]

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)
                          ) - self.momento_cadastro
        return tempo_cadastro
