coleccao = "especie"
coleccao_taxinomia = """
    especie,
    familia,
    genero,
    ordem,
    reino,
    filo,
    classe
"""
taxinomia_consulta = """
        familia.idFamilia = genero.idFamilia
        AND ordem.idOrdem = familia.idOrdem
        AND classe.idClasse = ordem.idClasse
        AND filo.idFilo = classe.idFilo
        AND reino.idReino = filo.idReino"""