from AnalizadorLexico import AnalizadorLexico
lexico = AnalizadorLexico()
lexico.analizar('PARTIDOS “Real Madrid” TEMPORADA <1999-2000> -ji 1 -jf 18')
lexico.verTokens()
lexico.verErrores()