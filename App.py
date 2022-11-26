from AnalizadorLexico import AnalizadorLexico
lexico = AnalizadorLexico()
lexico.analizar('TOP INFERIOR TEMPORADA <1999-2000> -n 3')
lexico.verTokens()
lexico.verErrores()