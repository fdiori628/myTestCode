# import psycopg2
# from Common.logger_until import Logger
#
#
# class DataBaseUntil:
#
#     def __init__(self, host, port, user, pwd, database=None, ):
#         self.conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=pwd)
#         self.cursor = self.conn.cursor()
#         self.log = Logger()
#         self.log.logger(f'connect to {host}:{database} successful')
#
#     def dml_script(self, dml):
#         try:
#             self.cursor.execute(dml)
#             self.log.logger(f'running script {dml}')
#             data = self.cursor.fetchall()
#             self.log.logger(f'get data from database successful')
#             self.log.logger(f'gets data: {data}')
#             self.cursor.close()
#             self.conn.close()
#             self.log.logger('connect closed')
#             return data
#         except Exception as err:
#             self.log.logger_error(err)
#             raise err
#
#
# if __name__ == '__main__':
#     host = "172.20.4.217"
#     port = 5432
#     user = "postgres"
#     pwd = 123456
#     d = DataBaseUntil(host=host, port=port, user=user, pwd=pwd)
#     r = d.dml_script("select datname from pg_database")
