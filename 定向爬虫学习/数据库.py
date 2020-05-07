import pymysql
if __name__ == '__main__':
    db = pymysql.connect('localhost', 'root', '123456', 'avIdol')
    cursor = db.cursor()

    sql = """
        INSERT INTO beautyGirls(name,age)
        VALUES("lisi",20),
        ("xiaowang",18);
    """
    sql1 = """
        SELECT * FROM beautyGirls
    """
    try:
        cursor.execute(sql1)

        results = cursor.fetchall()
        for re in results:
            name = re[0]
            age = re[1]
            print(name, age)
    except Exception as e:
        raise e

    db.close()
