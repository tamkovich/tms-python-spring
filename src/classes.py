import sqlalchemy as sa


class SQLiteDataBase:
    def __init__(self, database_file: str):
        self.db = sa.create_engine(f'sqlite:///{database_file}')

    def get_all_columns(self, table: str) -> '[]':
        columns = self.db.execute(f'''
                        PRAGMA table_info('{table}')
                        ''')
        return [column[1] for column in columns]

    def get_all_items(self, table: str) -> '[{}, {}]':
        columns = self.get_all_columns(table)
        rows = self.db.execute(f'''
                    SELECT * from '{table}'
                    ''')
        all_items = [{column: row[index] for index, column in enumerate(columns)} for row in rows]
        return all_items

    def get_item_by_id(self, table: str, item_id) -> []:
        item = self.db.execute(f'''
                    SELECT * from '{table}'
                    WHERE id = '{item_id}'
                    ''')
        return [elem for elem in item][0]

    def add_item(self, table: str, **attributes: object) -> object:
        columns = self.get_all_columns(table)
        if len(attributes) > len(columns) or not set(attributes.keys()).issubset(columns):
            raise ValueError('Wrong set of attributes for current table!')

        self.db.execute(f'''
            INSERT INTO '{table}' {tuple(attributes.keys())}
            VALUES {tuple(attributes.values())}
            ''')

    def update_item_by_id(self, table: str, item_id, **attributes):
        columns = self.get_all_columns(table)
        if len(attributes) > len(columns) or not set(attributes.keys()).issubset(columns):
            raise ValueError('Wrong set of attributes for current table!')

        self.db.execute(f'''
            UPDATE '{table}'
            SET {tuple(attributes.keys())} = {tuple(attributes.values())}
            WHERE id = '{item_id}'
            ''')

    def delete_item_by_id(self, table: str, item_id):
        self.db.execute(f'''
            DELETE FROM '{table}'
            WHERE id = '{item_id}'
            ''')
