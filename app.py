import pandas as p
import pymysql as maria

def lire_csv(nom_fichier: str) -> p.DataFrame:
    """_summary_ : permet de lire un fichier csv et de le convertir en DataFrame

    Args:
        nom_fichier (str): nom du fichier csv à lire "nom_fichier.csv"

    Returns:
        p.DataFrame: DataFrame contenant les données du fichier csv
    """
    table = p.read_csv(nom_fichier)
    print(table)
    return table


# table = lire_csv("clients.csv")


def se_connecter_db(host: str, user: str, password: str, database: str) -> maria.connections.Connection:
    """_summary_ : permet de se connecter à une base de données

    Args:
        host (str): machine sur laquelle se trouve la base de données
            - localhost : si c'est sur la même machine
            - ip : si c'est sur une autre machine exemple: 10.125.22.53
        user (str): login de la base de données
        password (str): password de la base de données
        database (str): nom de la base de données

    Returns:
        maria.connections.Connection: appel vers la base de données
    """
    connexion = maria.connect(host=host, user=user, password=password, database=database)
    return connexion


db_host = "localhost"
db_user = "root"
db_password = "example"
db_database = "exercice"

conn = se_connecter_db(db_host, db_user, db_password, db_database)


