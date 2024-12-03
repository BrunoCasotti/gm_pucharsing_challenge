import bd;

def insert_forecast(buyer_code, team_code, region, piece_code, description, sup_country, sup_code, year, price, volume):
    
    command = f'''INSERT INTO forecast 
    (buyer_code, team_code, region, piece_code, description, sup_country, sup_code, year, price, volume)  
                 VALUES ("{buyer_code}",{team_code},"{region}","{piece_code}","{description}",
                        "{sup_country}",{sup_code},{year},{price},{volume})'''
    bd.cursor.execute(command)
    bd.connection.commit()

def read_all_forecast():

    command = '''SELECT id as Id,
                        buyer_code as "Buyer code", 
                        team_code as "Team code",
                        region as "Region", 
                        piece_code as "Piece code", 
                        description as "Description",
                        sup_country as "Sup country",
                        sup_code as "Sup code", 
                        year as "Year", 
                        price as "Price",
                        volume as "Volume" 
                FROM forecast'''
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()
    return result

def read_forecast_by_id(id):

    command = f"SELECT * FROM forecast WHERE id = {id}"
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()
    return result

def read_column_forecast():
    
    command = '''SELECT 
                        CASE 
                            WHEN COLUMN_NAME = 'id' THEN 'Id'
                            WHEN COLUMN_NAME = 'buyer_code' THEN 'Buyer code'
                            WHEN COLUMN_NAME = 'team_code' THEN 'Team code'
                            WHEN COLUMN_NAME = 'region' THEN 'Region'
                            WHEN COLUMN_NAME = 'piece_code' THEN 'Piece code'
                            WHEN COLUMN_NAME = 'description' THEN 'Description'
                            WHEN COLUMN_NAME = 'sup_country' THEN 'Sup country'
                            WHEN COLUMN_NAME = 'sup_code' THEN 'Sup code'
                            WHEN COLUMN_NAME = 'year' THEN 'Year'
                            WHEN COLUMN_NAME = 'price' THEN 'Price'
                            WHEN COLUMN_NAME = 'volume' THEN 'Volume'
                        END AS Renamed_Column
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = 'forecast' 
                     AND TABLE_SCHEMA = 'gm_pucharse_case' '''
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()
    column_names = [row[0] for row in result]
    return column_names

def delete_forecast(id):

    command = f"DELETE FROM forecast WHERE id = {id}"
    bd.cursor.execute(command)
    bd.connection.commit()

def update_forecast(id, buyer_code, team_code, region, piece_code, description, sup_country, sup_code, year, price, volume):
    command = f'''
        UPDATE forecast
        SET 
            buyer_code = "{buyer_code}",
            team_code = {team_code},
            region = "{region}",
            piece_code = "{piece_code}",
            description = "{description}",
            sup_country = "{sup_country}",
            sup_code = {sup_code},
            year = {year},
            price = {price},
            volume = {volume}
        WHERE 
            id = {id}
    '''
    bd.cursor.execute(command)
    bd.connection.commit()