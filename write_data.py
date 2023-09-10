from architecture import Dados_Repositorios

amazon_rep = Dados_Repositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = Dados_Repositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = Dados_Repositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

#salvando os dados

ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')